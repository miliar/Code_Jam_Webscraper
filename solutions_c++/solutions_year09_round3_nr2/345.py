#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<vector>
#include<cmath>
#include<ctime>
#include<algorithm>
#include <map>

using namespace std;
#define SZ(v) ((int)v.size())
#define FOR(i,b,e) for(int i = b;i < e; ++i)
#define REP(i,v) FOR(i,0,SZ(v))
typedef vector<int> VI; 
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<char> VC;

const double pi=acos(-1.0);
const double eps=1e-11;
#define zero(x) memset(&x, 0, sizeof x);

int pos[128];
int npos[128];

int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	

	int T;
	cin>>T;

	FOR(k,0,T){
		double x=0,y=0,z=0,vx=0,vy=0,vz=0;
		int N;
		double x_,y_,z_,vx_,vy_,vz_;
		cin>>N;
		FOR(i,0,N){
			cin>>x_>>y_>>z_>>vx_>>vy_>>vz_;
			x+=x_/double(N);
			y+=y_/double(N);
			z+=z_/double(N);
			vx+=vx_/double(N);
			vy+=vy_/double(N);
			vz+=vz_/double(N);
		}


		double a,b,c;

		a=vx*vx+vy*vy+vz*vz;
		b=2*x*vx+2*y*vy+2*z*vz;
		c=x*x+y*y+z*z;
		
		double mind,mint;
		if (a>0.000000001){
			if (b<0) mint=-b/2/a;
			else mint=0;
			double temp=a*mint*mint+b*mint+c;
			if (temp>-0.000000001&&temp<0.000000001) temp=0;
			mind=sqrt(temp);
		}
		else{
			mind=sqrt(c);
			mint=0;
		
		}


		cout<<"Case #"<<k+1<<": ";
		printf("%.7lf %.7lf",mind,mint);
		cout<<endl;
//		cout<<a<<" "<<b<<" "<<c<<" "<<endl;
	}
	return 0;

}