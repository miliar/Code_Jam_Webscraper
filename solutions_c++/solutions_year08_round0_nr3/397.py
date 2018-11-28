#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

const int MAXP=200000;
const double PI=3.1415926535898;

int n;
double f,R,t,r,g;
double dy;
double totalArea, leakArea;

int main(){
	freopen("C-small-attempt1.in","r",stdin);
	freopen("test.out","w",stdout);
	cin>>n;
	for(int i=0;i<n;++i){
		cin>>f>>R>>t>>r>>g;
		totalArea=R*R*PI;
		leakArea=0;
		double l=g-2*f;
		double r1=R-f-t;
		double dy=l/MAXP;
		int start=(int)((-R-r-f)/(2*r+g))-5;
		int end=(int)((R-r-f)/(2*r+g))+5;

		for(int vn=start;vn<end;++vn){
			for(int hn=start;hn<end;++hn){

				double x1=vn*(2*r+g)+r+f;
				double y1=hn*(2*r+g)+r+f;
				double x2=x1+l;
				double y2=y1+l;
				
				if(x1*x1+y1*y1<r1*r1 &&
				   x1*x1+y2*y2<r1*r1 &&
				   x2*x2+y1*y1<r1*r1 &&
				   x2*x2+y2*y2<r1*r1){
					   leakArea+=l*l;
					   continue;
				}
				
				for(double y=y1;y<y1+l;y+=dy){
					if(y*y>r1*r1) continue;
					double tmp=sqrt(r1*r1-y*y);
					double through=min(x2,tmp)-max(x1,-tmp);
					if(through<0) through=0;
					leakArea+=through*dy;
				}
			}
		}
		if(leakArea>totalArea) leakArea=totalArea;
		cout<<"Case #"<<i+1<<": "<<1-(leakArea/totalArea)<<endl;
	}
	return 0;
}