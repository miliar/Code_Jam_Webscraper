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
#define bad {printf("NO\n");return 0;}
map<string,int> ma;
map<int,string> ma2;


int isand[50000];
int isch[50000];
int x[50000];
int dp0[50000];
int dp1[50000];
int m;
int imp;
int len;
	int k;
	string s;
	string s1;
int perm[1000];
int used[100];
int anw;


int main()
{

	ifstream inf("input.txt");
	ofstream outf("output.txt");
	int test;
	
	inf >>test;



	
	FOR(ii,1,test){
		long long a,n,m;
		inf>>n>>m>>a;
		long long sx1,sx2,sy1,sy2;
		sx1=-100;
		FOR(x1,0,n)FOR(x2,0,n)
			FOR(y1,0,m)FOR(y2,0,m){
				long long s=x1*y2-x2*y1;
				if(s<0)s=-s;
				if(s==a) {
					sx1=x1;
					sx2=x2;
					sy1=y1;
					sy2=y2;
					goto ll;
				}
		}

ll:


			if(sx1==-100)
			outf << "Case #"<<ii<<": "<<"IMPOSSIBLE"<<endl;
			else
				outf << "Case #"<<ii<<": "<<0<<" "<<0<<" "<<sx1<<" "<<sy1<<" "<<sx2<<" "<<sy2<<endl;




		//outf <<endl;
		//printf("Case #%d: \n",ii);

	}


	outf.close();  
   return 0;
}