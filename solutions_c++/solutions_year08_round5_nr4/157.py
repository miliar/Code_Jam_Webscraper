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

int anw2;
#define bad {printf("NO\n");return 0;}
int dp[200][200];
int imp=100000;


int main()
{

	ifstream inf("input.txt");
	ofstream outf("output.txt");
	int test;
	
	inf >>test;




	
	FOR(ii,1,test){
			int n,h,w,r;
			int rx[2][15];
			int p=10007;
			int anw;
			inf >>h>>w>>r;
			FOR(i,1,r) inf>>rx[0][i]>>rx[1][i];
			dp[1][1]=1;
			FOR(x,1,h) FOR(y,1,w){
				if((x==1) && (y==1)) continue;
				//dp[x,y]do
				dp[x][y]=-1;
				FOR(j,1,r) if((x==rx[0][j])  && (y==rx[1][j])){
					dp[x][y]=0;
				}
				if(dp[x][y]==0) continue;
				dp[x][y]=0;
				int a,b;
				a=x-2;b=y-1;
				if((a>=1) && (b>=1))dp[x][y]=dp[a][b];
				a=x-1;b=y-2;
				if((a>=1) && (b>=1))dp[x][y]+=dp[a][b];
				dp[x][y]=dp[x][y]%p;

			}
			

			anw=dp[h][w];
			outf << "Case #"<<ii<<": "<<abs(anw)<<endl;
			//outf << "Case #"<<ii<<": "<<anw<<endl;
	
		//outf <<endl;
		//printf("Case #%d: \n",ii);

	}


	outf.close();  
   return 0;
}