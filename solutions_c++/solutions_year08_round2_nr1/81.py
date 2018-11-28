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
#define imp 2000000102
#define pi 3.141592653589793
#define bad {printf("NO\n");return 0;}
map<string,int> ma;
map<int,string> ma2;
vector<int> next[100000];
int ek,pid;
int deg[10000];


int ra(int a,int b,int c,int d)
{
	return (a==c)&&(b==d);
}
int main()
{

	ifstream inf("input.txt");
	ofstream outf("output.txt");
	int test,t,na,nb,n;
	inf >>test;
	
	FOR(ii,1,test){
		long long a, b, c, d, x0, y0, m;
		inf >>n >>a>>b>>c>>d>>x0>>y0>>m;
		long long cc[3][3];
		long long anw=0;
		FOR(i,0,2) FOR(j,0,2) cc[i][j]=0;
		long long x=x0;
		long long y=y0;
		cc[x%3][y%3]++;
		FOR(i,1,n-1){
			 x = (a * x + b) % m;
			 y = (c * y + d) % m;
			 cc[x%3][y%3]++;
			 //outf << x<<" "<<y<<endl;
			}
		FOR(xx1,0,2)FOR(yy1,0,2)
			FOR(xx2,0,2)FOR(yy2,0,2)
			FOR(xx3,0,2)FOR(yy3,0,2){
				//check
				if((xx1+xx2+xx3)%3 !=0) continue;
				if((yy1+yy2+yy3)%3 !=0) continue;
				if(ra(xx1,yy1,xx2,yy2)&&ra(xx1,yy1,xx3,yy3)){
					long long t=cc[xx1][yy1];
					anw+= t*(t-1)*(t-2);//c n 3 /// /6
					continue;
				}
				if( (!ra(xx1,yy1,xx2,yy2)) && (!ra(xx1,yy1,xx3,yy3)) && (!ra(xx2,yy2,xx3,yy3))){
					anw+=cc[xx1][yy1]*cc[xx2][yy2]*cc[xx3][yy3];/// /6
					continue;
				}
				if( (ra(xx1,yy1,xx2,yy2)) && (!ra(xx1,yy1,xx3,yy3)) && (!ra(xx2,yy2,xx3,yy3))){
					anw+=cc[xx1][yy1]*(cc[xx1][yy1]-1)*cc[xx3][yy3]*3;   /// /2
					continue;
				}



				


				}

		        anw=anw/6;
				outf <<"Case #"<<ii <<": "<< anw<<endl;
		//printf("Case #%d: \n",ii);

	}


	outf.close();  
   return 0;
}