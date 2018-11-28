#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

int n,m,N,M,P,T,K;
int dp[128];
char tmp[128];
string name[128];
string qry[1024];


int main()
{
	string s;
	FILE *f=fopen("A-large.in","r");
	fscanf(f,"%d\n",&T);
	Repi(T)
	 {
			fscanf(f,"%d\n",&N);
			memset(dp,0,sizeof(dp));
			Repj(N)
			 {
			       fgets(tmp,128,f); name[j].assign(tmp);
		//	       cout<<"                     name "<<name[j];
		 	 }
		 //	cout<<" --- \n";
		 	fscanf(f,"%d\n",&M);
		 	Repj(M)
		 	 {
					fgets(tmp,128,f); s.assign(tmp);
					int v,mi=INF;
			//		cout<<"                       qry "<<s;
					Repk(N)
					 { 
					 if (name[k]==s) v=k;
					 else mi=MIN(mi,dp[k]);
					}
					dp[v]=mi+1;
				 // Repk(N) cout<<dp[k]<<" "; cout<<endl;
			 }
			int ans=INF;
			Repj(N)
			 ans=min(ans,dp[j]);
			printf("Case #%d: %d\n",i+1,ans);
		//	cout<<endl;
	 }
	fclose(f);
    return 0;
}
