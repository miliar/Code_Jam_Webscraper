#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
using namespace std;

double circle(double x) {
  return sqrt(1-x*x);      
};

double slice(double h) {
  double a, a2, sina2;
  sina2 = h/2;  
  a2 = asin(sina2);
  a = a2*2;    
  return 0.5*(a-sin(a));      
};

int main(int argc, char *argv[])
{
  ifstream inFile;      
  ofstream outFile; 

  int n, in, i;
  string str;
  
  double f, R, t, r, g;
  double result;
  char print_buff[20];
  
  double a;  // all
  double h;  
  double d;  // death
  double l;  // life
  double o;
  
  double x,y,pa,pb;               
  
  inFile.open("C-large.in");  
  outFile.open("results.txt");  

  if (!inFile) {
    cerr << "Unable to open file datafile.txt";
    exit(1);   
  };  
  if (!outFile) {
    cerr << "Unable to open file results.txt";
    exit(1);   
  };  

  getline(inFile, str);   
  n = atoi(str.c_str());
  for (in=0; in<n; in++) {
    // load data  
    result = 0.0;  
    getline(inFile, str, ' ');
    f = atof(str.c_str());
    getline(inFile, str, ' ');
    R = atof(str.c_str());
    getline(inFile, str, ' ');
    t = atof(str.c_str());
    getline(inFile, str, ' ');
    r = atof(str.c_str());
    getline(inFile, str);
    g = atof(str.c_str());
    // test gap
    if (2*f >= g) {
      result = 1.0;    
    }
    else {
      // normalize
      o = R-t-f;
      f /= o; t /= o; r /= o; g /= o; R /= o;  
      // 1/4 circle
      a = R*R*M_PI/4.0;
      h = 0.0;
      d = r + f;
      
      l = g - 2*f;
      for (y=d; y<1; y+=l+2*d) {
        for (x=d; sqrt(y*y+x*x)<1; x+=l+2*d) {
           if (sqrt((x+l)*(x+l)+(y+l)*(y+l)) < 1) {
             h += l*l;
           }
           else if ( y+l > circle(x) && x+l > circle(y)) {
             h += (circle(x)-y)*(circle(y)-x)/2.0;
             pa = circle(x)-y;
             pb = circle(y)-x;
             h +=  slice(sqrt(pa*pa + pb*pb));
           }
           else if ( y+l > circle(x) && y+l > circle(x+l)) {
             h += (((circle(x)-y)+(circle(x+l)-y))/2.0)*l;
             pa = circle(x)-circle(x+l);
             pb = l;
             h +=  slice(sqrt(pa*pa + pb*pb));
           }
           else if ( x+l > circle(y+l) && x+l > circle(y)) {
             h += (((circle(y)-x)+(circle(y+l)-x))/2.0)*l;
             pa = l;
             pb = circle(y)-circle(y+l);
             h +=  slice(sqrt(pa*pa + pb*pb));
           }
           else if ( x+l > circle(y+l) && y+l > circle(x+l)) {
             h += l*l-(y+l-circle(x+l))*(x+l-circle(y+l))/2.0;
             pa = y + l - circle(x+l);
             pb = x + l - circle(y+l);;
             h +=  slice(sqrt(pa*pa + pb*pb));
           } 
        }  
      }
      result = 1 - h/a;   
    }
    sprintf(print_buff, "%8.6f", result);  
    outFile << "Case #" << in+1  << ": " << print_buff << endl;
  }
 
  inFile.close();    
  outFile.close();    
  
  return EXIT_SUCCESS;
}
