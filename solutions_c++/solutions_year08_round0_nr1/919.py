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



int main()
{ 
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int test,s,q;
	char cc[1000];
	int num[2000];
	int inf=100000000;
	int dp[120][1200];
	scanf("%d",&test);
	map <string , int> mm;
	FOR(ii,1,test){
		scanf("%d",&s);
		gets(cc);
		FOR(j,1,s)
		{
			gets(cc);
			mm[cc]=j;
		//printf("%s\n",cc);

		}
		scanf("%d",&q);
		gets(cc);
		FOR(j,1,q){
			gets(cc);
			num[j]=mm[cc];
			//printf("%d\n",num[q]);

		}
		//now solve the problem
		FOR(i,1,s) dp[i][0]=0;
		FOR(j,1,q){
			FOR(i,1,s){
				if (num[j]==i) dp[i][j]=inf;
				else{
					dp[i][j]=dp[i][j-1];
					FOR(k,1,s) {
						int np=dp[k][j-1]+1;if(np<dp[i][j]) dp[i][j]=np;
					}
				}

			}
		
		}
		int anw;
		anw=inf;
		FOR(i,1,s) if (dp[i][q]<anw) anw=dp[i][q];
		printf("Case #%d: %d\n",ii,anw);










	}


   
   return 0;
}