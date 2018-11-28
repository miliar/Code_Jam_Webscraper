#include <iostream>
#include <vector>
#include <fstream>
#include <cmath>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

double pi = 3.14159265358979323846;
double eps = 1e-8;

int n,cas;

int main() {
	fin>>n;
	double f,R,t,r,g;
	int i,j;
	double totalArea,area;
	vector<double> vert;
	//vector<double> hor;
	double curr,tmp;
	double s,e,y,y1,ss,ee,a,b;
	for(cas=1;cas<=n;cas++) {
		//cout<<"------- "<<cas<<endl;
		area=0;
		fout<<"Case #"<<cas<<": "; 
		//cout<<"Case "<<cas<<endl;
		fin>>f>>R>>t>>r>>g;
		//cout<<f<<" "<<R<<" "<<t<<" "<<r<<" "<<g<<endl;
		totalArea = pi*R*R;
		R-=t;R-=f;
		//cout<<"totalArea: "<<totalArea<<endl;
		if(2*f >= g-eps){fout<<"1.0"<<endl;continue;}
		curr=0;
		vert.clear();
		//hor.clear();
		//cout<<"$$$ "<<curr+r+f<<" "<<curr+r+f+g-2*f<<endl;
		while(curr+r+f+g-2*f<R) {
			vert.push_back(curr+r+f);
			vert.push_back(curr+r+f+g-2*f);
			curr = curr+r+g+r;
		}
		if(curr+r+f<R)vert.push_back(curr+r+f);

		//curr=0;
		//while(curr+r+f+g-2*f<R) {
		//	hor.push_back(curr+r+f);
		//	hor.push_back(curr+r+f+g-2*f);
		//	curr = curr+r+g+r;
		//}
		//if(curr+r+f<R)hor.push_back(curr+r+f);
		//for(i=0;i<vert.size();i++) {
		//	cout<<vert[i]<<endl;
		//}
		//cout<<endl;
		//for(i=0;i<hor.size();i++) {
		//	cout<<hor[i]<<endl;
		//}
		//cout<<"hello"<<endl;
		
		for(i=0;i+1<vert.size();i+=2) {
			s = vert[i]; e = vert[i+1];
			//cout<<s<<" "<<e<<endl;
			y = sqrt(R*R - e*e);
			y1 = sqrt(R*R - s*s);
			for(j=0;j+1<vert.size();j+=2) {
				a = vert[j]; b = vert[j+1];
				if(a>=y1)break;
				if(a<=y && b<=y) {
					area += (b-a)*(e-s);
				}
				else if(a<=y && b>=y1) {
					tmp = ((R*R)/2.0)*asin(e/R) + (e*sqrt(R*R - e*e))/2.0;
					tmp -= ((R*R)/2.0)*asin(s/R) + (s*sqrt(R*R - s*s))/2.0;
					tmp -= (e-s)*a;
					area += tmp;
				}
				else if(a>=y && b<=y1) {
					ss = sqrt(R*R - b*b);
					ee = sqrt(R*R - a*a);
					tmp = ((R*R)/2.0)*asin(ee/R) + (ee*sqrt(R*R - ee*ee))/2.0;
					tmp -= ((R*R)/2.0)*asin(ss/R) + (ss*sqrt(R*R - ss*ss))/2.0;
					tmp -= (ee-ss)*a;
					tmp += (b-a)*(ss-s);
					area += tmp;
				}
				else if(a<=y && b>=y && b<=y1) {
					ss = sqrt(R*R - b*b);
					tmp = ((R*R)/2.0)*asin(e/R) + (e*sqrt(R*R - e*e))/2.0;
					tmp -= ((R*R)/2.0)*asin(ss/R) + (ss*sqrt(R*R - ss*ss))/2.0;
					tmp -= (e-ss)*a;
					tmp += (b-a)*(ss-s);
					area += tmp;
				}
				else if(b>=y1 && a>=y && a<=y1) {
					ee = sqrt(R*R - a*a);
					tmp = ((R*R)/2.0)*asin(ee/R) + (ee*sqrt(R*R - ee*ee))/2.0;
					tmp -= ((R*R)/2.0)*asin(s/R) + (s*sqrt(R*R - s*s))/2.0;
					tmp -= a*(ee-s);
					area += tmp;
				}
			}
			if(vert.size()%2==1) {
				a = vert[vert.size()-1];
				if(a<=y) {
					tmp = ((R*R)/2.0)*asin(e/R) + (e*sqrt(R*R - e*e))/2.0;
					tmp -= ((R*R)/2.0)*asin(s/R) + (s*sqrt(R*R - s*s))/2.0;
					tmp -= (e-s)*a;
					area += tmp;
				}
				if(a>=y && a<=y1) {
					ee = sqrt(R*R - a*a);
					tmp = ((R*R)/2.0)*asin(ee/R) + (ee*sqrt(R*R - ee*ee))/2.0;
					tmp -= ((R*R)/2.0)*asin(s/R) + (s*sqrt(R*R - s*s))/2.0;
					tmp -= a*(ee-s);
					area += tmp;
				}
			}
		}

		if(vert.size()%2==1) {
			//cout<<"hello"<<endl;
			s = vert[vert.size()-1];
			y = sqrt(R*R - s*s);
			for(j=0;j+1<vert.size();j+=2) {
				a = vert[j]; b = vert[j+1];
				if(a>=y)break;
				if(a<=y && b<=y) {
					ss = sqrt(R*R - b*b);
					ee = sqrt(R*R - a*a);
					tmp = ((R*R)/2.0)*asin(ee/R) + (ee*sqrt(R*R - ee*ee))/2.0;
					tmp -= ((R*R)/2.0)*asin(ss/R) + (ss*sqrt(R*R - ss*ss))/2.0;
					tmp -= (ee-ss)*a;
					tmp += (b-a)*(ss-s);
					area += tmp;
				}
				else if(a<=y && b>=y) {
					ee = sqrt(R*R - a*a);
					tmp = ((R*R)/2.0)*asin(ee/R) + (ee*sqrt(R*R - ee*ee))/2.0;
					tmp -= ((R*R)/2.0)*asin(s/R) + (s*sqrt(R*R - s*s))/2.0;
					tmp -= a*(ee-s);
					area += tmp;
				}
			}
			if(vert.size()%2==1) {
				a = vert[vert.size()-1];
				//cout<<"$$$$ "<<a<<" "<<y<<endl;
				if(a<=y) {
					ee = sqrt(R*R - a*a);
					tmp = ((R*R)/2.0)*asin(ee/R) + (ee*sqrt(R*R - ee*ee))/2.0;
					tmp -= ((R*R)/2.0)*asin(s/R) + (s*sqrt(R*R - s*s))/2.0;
					tmp -= a*(ee-s);
					area += tmp;
				}
			}
		}

		//cout<<"###### "<<4.0*area<<" "<<totalArea<<endl;
		fout<<1.0 - (4.0*area/totalArea)<<endl;
		//cout<<"--- --- ---"<<endl;
	}
	return 0;
}