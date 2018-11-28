#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define SIZE(X) ((int)(X.size()))
#define MP(X,Y) make_pair(X,Y)
#define two(X) (1<<(X))
#define contain(S,X) (((S)&two(X))!=0)
typedef pair<int,int> ipair;
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T euclide(T a,T b,T &x,T &y)
  {if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}
   if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}
   if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}

const int MODE=10007;
const int maxsize=2000000+5;

int G[maxsize];

int level(int n)
{
	if (n<MODE) return 0;
	return n/MODE+level(n/MODE);
}
int div2(int a,int b)
{
	int x,y;
	euclide(MODE,b,x,y);
	y=((y*a)%MODE+MODE)%MODE;
	return y;
}
int getC(int n,int m)
{
	int l=level(n)-level(m)-level(n-m);
	if (l!=0) return 0;
	int t1=G[n];
	int t2=G[m];
	int t3=G[n-m];
	return div2(div2(t1,t2),t3);
}
int solve(int n,int m)
{
	if (n>m) swap(n,m);
	int x=(2*m-n)/3;
	int y=(n-x)/2;
	if (x+2*y==n && 2*x+y==m)
		return getC(x+y,x);
	return 0;
}
int main()
{
//	freopen("input.txt","r",stdin);
	freopen("D-small-attempt1.in","r",stdin);freopen("D-small-attempt1.out","w",stdout);
//	freopen("D-large.in","r",stdin);freopen("D-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	int X0,Y0,n,X[20],Y[20];
	G[0]=1;
	for (int i=1;i<maxsize;i++)
	{
		int v=i;
		for (;v%MODE==0;v/=MODE);
		G[i]=(G[i-1]*v)%MODE;
	}
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d:",caseId);
		scanf("%d%d%d",&X0,&Y0,&n);
		for (int i=0;i<n;i++) scanf("%d%d",&X[i],&Y[i]);
		int result=0;
		for (int set=0;set<two(n);set++)
		{
			int cnt=1;
			vector<ipair> Q;
			Q.push_back(MP(1,1));
			Q.push_back(MP(X0,Y0));
			for (int i=0;i<n;i++) if (contain(set,i)) Q.push_back(MP(X[i],Y[i]));
			sort(Q.begin(),Q.end());
			for (int i=0;i<SIZE(Q)-1;i++)
			{
				int dx=Q[i+1].first-Q[i].first;
				int dy=Q[i+1].second-Q[i].second;
				if (dx>=0 && dy>=0 && dy<=dx*2 && dx<=dy*2)
				{
					int tmp=solve(dx,dy);
					cnt=(cnt*(tmp%MODE))%MODE;
				}
				else 
					cnt=0;
			}
			if (countbit(set)%2==0) result=(result+cnt)%MODE;
			else result=(result-cnt+MODE)%MODE;
		}
		printf(" %d\n",result);
		fflush(stdout);
	}
	return 0;
}

