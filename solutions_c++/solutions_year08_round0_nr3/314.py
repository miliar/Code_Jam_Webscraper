#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

const double PI = acos(-1.0);

//(x1,y1) < (x2,y2)
double segment_area(double x1,double y1,double x2,double y2){
  double rR = sqrt(x1*x1+y1*y1);
  double rR2 = x1*x1+y1*y1;
  if(rR<=0)
    return 0;
  double a1 = acos(x1/rR);
  double a2 = acos(x2/rR);
  double a = a2-a1;
  double lXY = sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
  double lXY2 = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
  double p = (2*rR+lXY)/2.0;
  double triA = (lXY2*sqrt(rR2/lXY2-0.25))/2.0;//sqrt((p*(p-rR)*(p-rR)*(p-lXY)));
  double sliceA = ((a/2.0)*rR*rR);
  double segmentA = sliceA-triA;
  return segmentA;
}

int main(){

  int N;
  cin >> N;
  for(int i=1;i<=N;i++){
    double f,R,t,r,g;    
    cin >> f >> R >> t >> r >> g;
    double iR = R-t;
    double rR = iR-f;
    double A=(PI*R*R)/4.0;
    double gA = 0.0;
    double tX,tY;
    for(int x=0;(tX=r+x*g+2*x*r)<=rR;x++)
      for(int y=0;(tY=r+y*g+2*y*r)<=rR;y++){
	tX = r+x*g+2*x*r+f;
	tY = r+y*g+2*y*r+f;
	double nG = g-2*f;
	if(nG<0)
	  continue;
	double c = nG*nG;
	if(sqrt(tX*tX+tY*tY)>=rR)
	  continue;
	if(sqrt((tX+nG)*(tX+nG)+(tY+nG)*(tY+nG))<=rR){
	  gA+=c;
	  continue;
	}
	double oX = min(rR*cos(asin(tY/rR)),tX+nG);
	double lX = sqrt(oX*oX+tY*tY);
	double oY = min(rR*sin(acos(tX/rR)),tY+nG);
	double lY = sqrt(tX*tX+oY*oY);
	double noX = cos(asin(oY/rR))*rR;
	double noY = sin(acos(oX/rR))*rR;
	c=segment_area(oX,noY,noX,oY)+(noX-tX)*(oY-tY)+(oX-noX)*(noY-tY)+
	  ((oX-noX)*(oY-noY))/2.0;
	if(c<0)
	  c=0;
	gA+=c;
      }
    double res = (1.0-(gA/A));
    if(res<1.E-7)
      res=0.0;
    cout << fixed << setprecision(6) << "Case #" << i << ": " << res << "\n";
    
  }

}
