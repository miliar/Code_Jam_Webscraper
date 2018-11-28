#define wru 0
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <cassert> 
#include <cmath> 
#include <vector> 
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std; 

typedef double LD;
typedef long long LL;
typedef  vector<int> VI;
typedef  vector<string> VS;
ifstream inf ;
ofstream outf ;

/*template  */

#define FOR(i,a,b) for( int i=(a),_b=(b); i<=(_b); i++) 
#define FORD(i,a,b) for( int i=(a),_b=(b); i>=(_b); i--) 
#define FORIT(i,a,type) for(type::iterator i=((a).begin()); i<((a).end()); i++) 
#define bend(x) x.begin(),x.end()
#define SORT(x) sort(bend(x))
#define pf(a) outf<< #a <<" = " <<a <<endl;
#define clr(t) memset((t),0,sizeof(t))
#define mnn 71234
#define pi 3.141592653589793
		
	
int main()
{

	ifstream inf("input.txt");
	ofstream outf("output.txt");
	/*
	freopen("input.txt","rt",stdin);
	
	int a;
	scanf("%d",&a);
	printf("%d",a+22);
	*/
	freopen("output.txt","wt",stdout);
		double x1[4];
		double y1[4];
		double x2[4];
		double y2[4];
		double dx,dy;
		int test;
	inf >>test;
	//test=1;
	FOR(ii,1,test){
		
		inf>>x1[1]>>y1[1]>>x1[2]>>y1[2]>>x1[3]>>y1[3];
		inf>>x2[1]>>y2[1]>>x2[2]>>y2[2]>>x2[3]>>y2[3];
		double sx=x1[1];
		double sy=y1[1];//zzero
		FOR(i,1,3) {y2[i]-=sy; x2[i]-=sx;}
		FOR(i,1,3) {y1[i]-=sy; x1[i]-=sx;}

		
		dx=x2[1]-x1[1];
		dy=y2[1]-y1[1];
		FOR(i,1,3) {y2[i]-=dy; x2[i]-=dx;}
		double a,b,c,d;
		double a2,b2,c2,d2;
		double a1,b1,c1,d1;
		a=x1[2];b=x1[3];c=y1[2];d=y1[3];
		a1=d;b1=-b;c1=-c;d1=a;
		double di=(a*d-b*c);
		int fl=0;
		//if(di<0) {di=-di; fl=1;}
		//di=sqrt(di);
		//if (fl) { a1=-a1;b1=-b1;c1=-c1;d1=-d1;}
		a1=a1/di;b1=b1/di;c1=c1/di;d1=d1/di;
		a2=a1*x2[2]+c1*x2[3];
		c2=a1*y2[2]+c1*y2[3];
		b2=b1*x2[2]+d1*x2[3];
		d2=b1*y2[2]+d1*y2[3];
/*
		a2=a1*x2[2]+b1*y2[2];
		b2=a1*x2[3]+b1*y2[3];
		c2=c1*x2[2]+d1*y2[2];
		d2=c1*x2[3]+d1*y2[3];
*/		
		//now i have matrix;
		double x0,y0;
		x0=0;y0=0;
		FOR(i,1,900000){
			double x0a,y0a;
				x0a=x0*a2+y0*b2;
				y0a=x0*c2+y0*d2;
				x0a+=dx;
				y0a+=dy;
				x0=x0a;y0=y0a;
		}




		x0=x0+sx;y0=y0+sy;	

		outf.precision(12);
		outf << "Case #"<<ii<<": "<<x0<<" "<<y0<<endl;
	//	printf("Case #%d: %l %l\n",ii,single(x0),single (y0));
	}


	outf.close();  
   return 0;
}