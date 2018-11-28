#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <fstream>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

int T,t;
long long n,A,B,C,D,x_0,y_0,M;

struct P {
	long long x,y;
};

int main() {
	fin>>T;
	vector<P> pts;
	int i,j,k;P tmp;
	int ret;
	for(t=1;t<=T;t++) {
		fout<<"Case #"<<t<<": ";
		fin>>n>>A>>B>>C>>D>>x_0>>y_0>>M;
		pts.resize(n);
		tmp.x=x_0;tmp.y=y_0;
		pts[0]=tmp;
		for( i = 1;i<= n-1;i++) {
				tmp.x = (A * tmp.x + B) % M;
				tmp.y = (C * tmp.y + D) % M;
				pts[i]=tmp;
		}
		ret=0;
		for(i=0;i<pts.size();i++) {
			for(j=i+1;j<pts.size();j++) {
				for(k=j+1;k<pts.size();k++) {
					if(pts[i].x==pts[j].x && pts[i].y==pts[j].y)continue;
					if(pts[i].x==pts[k].x && pts[i].y==pts[k].y)continue;
					if(pts[j].x==pts[k].x && pts[j].y==pts[k].y)continue;
					if( (pts[i].x+pts[j].x+pts[k].x)%3==0 && (pts[i].y+pts[j].y+pts[k].y)%3==0  )ret++;
				}
			}
		}
		fout<<ret<<endl;
		
	}
	return 0;
}