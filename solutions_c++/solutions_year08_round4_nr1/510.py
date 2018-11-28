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

#define INF 10000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

#define MAXN 30000
int n,m,N,M,P,T,K,V;
int dp[MAXN][2];

struct node{	int leaf,change,value,andor; 	};
node tree[MAXN];

int solve(int at,int val)
{
	int &ret=dp[at][val];
	if (ret!=-1) return ret;
	if (tree[at].leaf) return ret=((val==tree[at].value)?0:INF);
	
	ret=INF; int t1,t2;
	
if (val)
{
 		    t1=solve(at<<1,1); t2=solve((at<<1)+1,1);
			if (tree[at].andor)
			   {
			     ret=min(ret,t1+t2);
			   //  cout<<" in "<<at<<" - case 1 "<<t1<<"+"<<t2<<endl;
			     if (tree[at].change)
			      {
			         ret=min(ret,min(t1,t2)+1);
			    //     cout<<" in "<<at<<" - case 2 "<<t1<<"/"<<t2<<" +1 "<<endl;
				  }
			   }
			else
			   {
			     ret=min(ret,min(t1,t2));
			 //    cout<<" in "<<at<<" - case 3 "<<t1<<"/"<<t2<<endl;
			     if (tree[at].change)
			      {
			        ret=min(ret,t1+t2+1);
  			  //      cout<<" in "<<at<<" - case 4 "<<t1<<"+"<<t2<<"+1"<<endl;
				  }
			   }
}
else
{
 		    t1=solve(at<<1,0); t2=solve((at<<1)+1,0);
			if (tree[at].andor)
			   {
			     ret=min(ret,min(t1,t2));
			     if (tree[at].change)
			      ret=min(ret,t1+t2+1);
			   }
			else
			   {
			     ret=min(ret,t1+t2);
			     if (tree[at].change)
			      ret=min(ret,min(t1,t2)+1);
			   }
}

//cout<<" "<<at<<" "<<val<<" = "<<ret<<endl;
return ret;
}

int main()
{
    scanf("%d",&T); int id=0;
    for(;T;T--)
    {
	//	cout<<" CASE "<<id<<endl;
		id++;
		scanf("%d%d",&M,&V);
		for (int i=1;i<=((M-1)>>1);i++)
		 {
				scanf("%d %d",&tree[i].andor,&tree[i].change);
				tree[i].leaf=0;
		//		cout<<"INP "<<i<<" : "<<tree[i].andor<<" "<<tree[i].change<<endl;
		 }
		for (int i=((M-1)>>1)+1;i<=M;i++)
		 {
				scanf("%d",&tree[i].value);
				tree[i].leaf=1;
			//	cout<<tree[i].value<<endl;
		 }
		
		memset(dp,-1,sizeof(dp));
		if (solve(1,V)<INF)
		 {
				printf("Case #%d: %d\n",id,dp[1][V]);
		 }
		else
		 printf("Case #%d: IMPOSSIBLE\n",id);
	}
    
    return 0;
}
