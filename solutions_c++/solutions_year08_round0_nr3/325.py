//Compile Command:
//        g++ C.cpp -o C
//Run Command:
//        ./C C-small.in C-small.out
//        ./C C-large.in C-large.out

#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <cstdlib>
#include <sstream>
#include <iomanip>
using namespace std;

class Square
{
public:
  double _x;
  double _y;
  double _s;
};

double calculate(double f, double R, double t, double r, double g)
{
  double P;
  if (2*f>=g) { P = 1.0; return P;}
  double rNew = r+f;
  double gNew = g-2*f;
  double RNew = R-t-f;
  const double PI = 3.141592653589;
  int n=0; //quarter
  n = ceil((RNew+rNew)/(gNew+2*rNew));
  Square *pSquares = new Square[n*(n+1)/2];
  int index=-1;
  double x,y;
  bool a,b,c,d;
  for (int i = 0; i < n; i++){
    for(int j = 0; j <= i; j++){
      index++;
      x = rNew+i*(gNew+2*rNew); 
      y = rNew+j*(gNew+2*rNew);
      pSquares[index]._x = x;
      pSquares[index]._y = y; 
      a = x*x+y*y < RNew*RNew ? true : false;
      b = (x+gNew)*(x+gNew)+y*y < RNew*RNew ? true : false;
      c = (x+gNew)*(x+gNew)+(y+gNew)*(y+gNew) < RNew*RNew ? true : false;
      d = x*x+(y+gNew)*(y+gNew) < RNew*RNew ? true : false;

      if(a && b && c && d){
	pSquares[index]._s = gNew*gNew;
      }
      else if(a && b && ~c && d){
	double y1 = y+gNew;
	double x1 = sqrt(RNew*RNew-y1*y1);
	double x2 = x+gNew;
	double y2 = sqrt(RNew*RNew-x2*x2);
	double s1 = gNew*gNew-(x+gNew-x1)*(y+gNew-y2)/2;
	double d1 = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))/2;
	double d2 = sqrt((x1+x2)*(x1+x2)+(y1+y2)*(y1+y2))/2;
	double s2 = d1*d2;
	double theta = atan(d1/d2);
	double s3 = theta * RNew* RNew;
	pSquares[index]._s = s1+s3-s2;
      }
      else if(a && b && ~c && ~d){
	double x1 = x;
	double y1 = sqrt(RNew*RNew-x1*x1);
	double x2 = x+gNew;
	double y2 = sqrt(RNew*RNew-x2*x2);
	double s1 = (y1-y+y2-y)*gNew/2;
	double d1 = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))/2;
	double d2 = sqrt((x1+x2)*(x1+x2)+(y1+y2)*(y1+y2))/2;
	double s2 = d1*d2;
	double theta = atan(d1/d2);
	double s3 = theta * RNew* RNew;
	pSquares[index]._s = s1+s3-s2;
      }
      else if(a && ~b && ~c && d){
	double y1 = y+gNew;
	double x1 = sqrt(RNew*RNew-y1*y1);
	double y2 = y;
	double x2 = sqrt(RNew*RNew-y2*y2);
	double s1 = (x1-x+x2-x)*gNew/2;
	double d1 = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))/2;
	double d2 = sqrt((x1+x2)*(x1+x2)+(y1+y2)*(y1+y2))/2;
	double s2 = d1*d2;
	double theta = atan(d1/d2);
	double s3 = theta * RNew* RNew;
	pSquares[index]._s = s1+s3-s2;
      }
      else if(a && ~b && ~c && ~d){
	double x1 = x;
	double y1 = sqrt(RNew*RNew-x1*x1);
	double y2 = y;
	double x2 = sqrt(RNew*RNew-y2*y2);
	double s1 = (y1-y)*(x2-x)/2;
	double d1 = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))/2;
	double d2 = sqrt((x1+x2)*(x1+x2)+(y1+y2)*(y1+y2))/2;
	double s2 = d1*d2;
	double theta = atan(d1/d2);
	double s3 = theta * RNew* RNew;
	pSquares[index]._s = s1+s3-s2;
      }
      else{
	pSquares[index]._s = 0;
      }
    }
  }
  double s =0;
  index = -1;
  for (int i = 0; i < n; i++){
    for(int j = 0; j <= i; j++){
      index++;
      if (j == i){
	s += pSquares[index]._s;
      }
      else{
	s+= 2*pSquares[index]._s;
      }
    }
  }

  s = s*4;
  P = 1-s/(PI*R*R);

  delete[] pSquares;
  return P;
}

int main(int argc, char ** argv)
{
  ifstream infile(argv[1]);
  ofstream outfile(argv[2], ios::app);

  string aline("");
  int num;
  const int SIZE = 5;
  if (getline(infile,aline)) {
    num = atoi(aline.c_str());
  }
  for (int i=0; i < num; i++) {
    double f,R,t,r,g,P;
    P = 0;
    string::size_type index;
    getline(infile,aline);

    string subs[SIZE];
    for(int j = 0; j < SIZE-1; j++){
      index = aline.find(" ", 0);
      subs[j] = aline.substr(0, index);
      aline = aline.substr(index+1, aline.length());
    }
    subs[SIZE-1]=aline;
    f = atof(subs[0].c_str());
    R = atof(subs[1].c_str());
    t = atof(subs[2].c_str());
    r = atof(subs[3].c_str());
    g = atof(subs[4].c_str());

    P = calculate(f,R,t,r,g);

    outfile << "Case #" << i+1 << ": "<< fixed << P << endl;
    cout << "Case #" << i+1 << ": " << fixed << P << endl;
  }
  outfile.close();
  infile.close();
  return 0;
}
