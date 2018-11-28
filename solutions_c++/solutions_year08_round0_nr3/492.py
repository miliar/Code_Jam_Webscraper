#include <iostream>
#include <math.h>

using namespace std;


#define _SQUARED(x) ((x)*(x))

double area(double r, double h, double x, double y) {
  // This function calculates  the are a of  a square cut by a  circle. It does
  // not check  wether the square is  actually outside the circle,  and it only
  // works  for  squares  in  the  lower-right quadrant,  under  the  secondary
  // diagonal, i.e. x > 0 && -x > y. This is also not checked.
  
  double r_2 = _SQUARED(r);
  double dd4, dd3, dd2, dd1;
  
  // Squared distance to the nearest vertex.
  dd1 = _SQUARED(x) + _SQUARED(y);
  if (dd1 > r_2)     return 0.0; // The square is completely outside the circle.

  // Squared distance to the most distant vertex.
  dd4 = _SQUARED(x+h) + _SQUARED(y-h);
  if (dd4 < r_2)     return _SQUARED(h); // The square is completely inside the circle.
  
  // There are three possible cases:
  //   a. Only one vertex inside the circle.
  //   b. Two vertices inside, cutting through the vertical edges.
  //   c. Three vertices inside, and one outside.

  dd3 = _SQUARED(x  ) + _SQUARED(y-h);
  dd2 = _SQUARED(x+h) + _SQUARED(y  );
  
  // Gratuitous  nested use  of  the wonderful  ternary conditional  evaluation
  // operator.
  char the_case = (dd2<r_2)?((dd3<r_2)?'c':'b'):'a';

  double ta, tb; // Angles
  double x_sec1, x_sec2, y_sec1, y_sec2; // Interception coordinates

  switch(the_case) {
  case 'a':
    ta = asin(-y/r); tb = acos(x/r);
    // From Pythagoras equation. It's FOSS, trust me!
    x_sec2 = sqrt(r*r-y*y); y_sec2 = -sqrt(r*r-x*x);
    break;
  case 'b':
    ta = acos((x+h)/r); tb = acos(x/r);
    y_sec1 = -sqrt(r_2-(x+h)*(x+h));
    x_sec2 = y*(x+h)/y_sec1; y_sec2 = -sqrt(r*r-x*x);
    break;
  case 'c':
    ta = acos((x+h)/r); tb = asin(-(y-h)/r);
    x_sec1 =  sqrt(r_2-(y-h)*(y-h));
    y_sec1 = -sqrt(r_2-(x+h)*(x+h));
    
    x_sec2 = y*(x+h)/y_sec1;
    y_sec2 = x*(y-h)/x_sec1;
  }

  // Area of  the pizza slice relevant  to out calculation, from  the center of
  // the circle, to the points where it cuts the square. ta is the angle to the
  // point nearer to the x axis, and thus with a smaller absolute value.
  double A =  r_2*( tb-ta )/2;

  // Area of  triangles to subtract from  the pizza slice. They  range from the
  // intercept in the nearest edges, to  the ray from the center to the nearest
  // vertex: (x,y).
  double T1 = -( (y_sec2-y) *x) /2;  // Notice that T1 may be negative in case c.
  double T2 = -( (x_sec2-x) *y) /2;
  
  double Atotal = A-T1-T2;

  // In cases 'b' or 'c', add the triangle over the pizza slice, completing the
  // part of the square inside the circle.
  if (dd2<r_2) Atotal += -(y_sec1-y)  *  ( (x+h) - x_sec2 )/2;

  // In case  'c', add also the  triangle under the pizza  slice. This triangle
  // can lie outside  the square, and have a very large  and negative area when
  // this pizza slice  is too narrow, and  both of its edges cut  the square in
  // the  same (top  horizontal) edge.   This  negative value  works along  the
  // negative value of T1.  Mathematics is so beautiful!...
  if (dd3<r_2) Atotal += -(x_sec1-x)  *  ( (y-h) - y_sec2 )/2;

  return Atotal;

}



double calc_prob_inside(double r, double h) {
  //cout <<r<<" "<< h<<" "<<0<<endl;

  // Given a circle with radius r and squares of height h spaced 1 unit to each
  // other, what is the probability of a hit?

  // If the square if too big (g>1), we can't get the gnat.
  if (h>=1) return 0.0;

  double r_2 = _SQUARED(r);

  int x = 0; // Start iterations at first square.
  int y = -int(floor(r)); // First y-coordinate is taken by truncating radius

  double err0 = r_2 - ( x*x + y*y ); // Initial error, a FP value.
  int err=0;  // Update to the error. It's integer, but the total error is err + err0.
  
  // Cumulative sum of the areas of the little squares.
  double S_aread = 0.0; // The fractional area, from the cut squares.
  int S_areai = 0;      // The area of the  whole squares, plus and excess from
			// outside the secondary diagonal.

  double this_area; // The last area calculated from a cut square.
  do {
    // add the area of the "tip" of the column of squares
    this_area=area(r, h, x+(1-h)/2.0, y-(1-h)/2.0);
    S_aread += this_area; 

    //cout << x << " " <<y<<" " << err+err0 << " "<<this_area<<endl;
    //cout << x << " " <<y<< " " <<this_area<< " "<< S_areai<< endl;

    // Update  the  values  of  the  error in  the  cybernetic,  error-feedback
    // Bresenham-based drawing system.
    // The formula for the error is    
    //   err0 = r_2 - ( x*x + y*y); 
    // But:
    //   err0 = r_2 - ( (x+1)*(x+1) + y*y); 
    //   err0 = r_2 - ( x*x + 2*x + 1 + y*y); 
    //   err0 = err0 - (2*x+1)
    // Notice  that this  error update  needs  the "old"  values of  x, so  the
    // increment is done afterwards.

    err -= (2*x+1);
    x++;    


    // Add the area of the uncut squares.
    S_areai += -x-y+1;
    if ( err<-err0 && y<=-x) {
      // Need to increment y;
      err -= (2*y+1);
      y++;

      // Consider the area of the square over.
      this_area=area(r, h, x-1+(1-h)/2.0, y-(1-h)/2.0);
      S_aread += this_area; 

      //cout << x-1 << " " <<y<<" " << err+err0 << " "<<this_area<<endl;
      //cout << x-1 << " " <<y<< " " << this_area<<" "<<S_areai<<endl;

      S_areai--;
    }


  } while (y <= -x);
  //cout << x << " " <<y<<" "<<err+err0<<endl;

  S_aread -= this_area/2.0;

  double empty_area = _SQUARED(h)*(S_areai*2-(x-1) )*4 + S_aread*8;
  //cout << S_areai << " -"<<x << " "<< S_aread << endl;
  double circle_area = M_PI*r_2;
  return 1 - empty_area/circle_area;
}


double calc_stuff(double R, double t, double g) {
  // If the square has a null width (g<0), it's impossible for the insect to
  // escape.
  if (g<=0) return 1.0;
  
  // The total  probability is the  prob of the  fly hitting the rim,  plus the
  // probability of  it missing the rim  times the probability of  it being hit
  // inside. So:

  double Rin = R-t;
  // If the inner radius is too small (Rin<0), this is a joke
  if (Rin<0) return 1.0;

  double Ain = M_PI*_SQUARED(Rin); // pi R_in^2
  double Atotal = M_PI * _SQUARED(R); // pi (R^2)

  double Pinside = Ain/Atotal;

  return (1-Pinside) + Pinside * calc_prob_inside(Rin, g);
  


}

int main () {
  double f, R, t, r, g;
  double N;
  int n=0;
  
  cin >> N;

  cout.flags( ios::fixed );
  cout.precision(6);
  while (n++<N) {
    // Read input
    cin >> f >> R >> t >> r >> g;

    // This is the space between squares.
    double dx = g+2*r;

    // Consider a  punctual fly, adding its  width to the  other parameters. dx
    // doesn't change, BTW.
    t+=f;
    g-=2*f;
    r+=f;

    // Normalize so that dx is unity.
    R/=dx;
    t/=dx;
    r/=dx;
    g/=dx;

    // So,  now we  must calculate  the probability  of a  certain  vector fall
    // inside a square  with side g, smaller  than a square with size  1, in an
    // array of squares. This array is inside a certain circular crown (?) with
    // inner radius R-t and thickness t.

    //
    // The output at last
    cout << "Case #" << n << ": " << calc_stuff(R, t, g) <<endl;
  }
  return 0;
}




