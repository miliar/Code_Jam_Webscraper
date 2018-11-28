#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

const double pi = 3.1415926535897932;

int main() {
	//cout<<asin(0.5)<<endl;
	freopen("C-large.in","r",stdin);
	int N;
	cin>>N;
	double f,R,t,r,g;
	ofstream fp("C-large.out");
	for(int i = 1; i <= N; i++) {
		cin>>f>>R>>t>>r>>g;
		double res = 0.0;
		double area = pi * R * R;
		R -= t;
		double unhitArea = 0.0;
		double gap = g + 2 * r;
		if(g - 2 * f <= 0) {
			res = 1.0;
			fp<<"Case #"<<i<<": "<<res<<endl;
			continue;
		}
		double unit1 = (g - 2 * f) * (g - 2 * f);
		R -= f;
		double edg = R * R;
		g -= 2 * f;
		for(double x = r + f; x < R; x += gap) {
			for(double y = r + f; y < R; y += gap) {
				if( x * x + y * y >= edg) {
					//cout<<"0000"<<endl;
					continue;//0 points
				}
				double rig = x + g;
				double up = y + g;
				if(rig * rig + up * up <= edg) { //4 points
					unhitArea += unit1;
					//cout<<"4444"<<endl;
					continue;
				}				
				if(rig * rig + y * y <= edg) {
					if(x * x + up * up <= edg) {//3 points
						//cout<<"3333"<<endl;
						unhitArea += g * g;
						double width = sqrt(edg - up * up) - x; 
						double height = sqrt(edg - rig * rig) - y;
						unhitArea -= 0.5 * (g - width) * (g - height);
						double ch = sqrt((g - width) * (g - width) + (g - height) * (g - height) );
						double ang = 2.0 * asin(0.5 * ch / R);
						unhitArea += 0.5 * ang * edg - 0.5 * edg * sin(ang);
					}
					else { //2 points
						//cout<<"2222"<<endl;
						double height1 = sqrt(edg - x * x) - y;
						double height2 = sqrt(edg - rig * rig) - y;
						unhitArea += 0.5 * g * (height1 + height2);
						double ch = sqrt(g * g + (height1 - height2) * (height1 - height2));
						double ang = 2.0 * asin(0.5 * ch / R);
						unhitArea += 0.5 * ang * edg - 0.5 * edg * sin(ang);
					}
				}
				else {
					if(x * x + up * up <= edg) {//2 points
						//cout<<"22 22"<<endl;
						double width1 = sqrt(edg - up * up) - x;
						double width2 = sqrt(edg - y * y) - x;
						unhitArea += 0.5 * g * (width1 + width2);
						double ch = sqrt(g * g + (width1 - width2) * (width1 - width2));
						double ang = 2.0 * asin(0.5 * ch / R);
						unhitArea += 0.5 * ang * edg - 0.5 * edg * sin(ang);
					}
					else { //1 points
						//cout<<"1111"<<endl;
						double xf = x;
						double yf = y;
						double rf = R;
						double width = sqrt(rf*rf - yf*yf) - xf;
						double height = sqrt(rf*rf - xf*xf) - yf;
						unhitArea += 0.5 * width * height;
						double ch = sqrt(width * width + height * height);
						double ang = 2.0 * asin(0.5 * ch / rf);
						unhitArea += 0.5 * ang * rf * rf - 0.5 * rf * rf * sin(ang);
					}
				}
			}
		}
		unhitArea *= 4.0;
		res = 1.0 - unhitArea / area;
		fp<<"Case #"<<i<<": "<<res<<endl;
		//cout<<i<<"   ***   "<<endl;
	}
	fp.close();
	return 0;
}
