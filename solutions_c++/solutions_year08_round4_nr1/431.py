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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b_);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1LL<<50
#define DEB(x) cerr<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
int Tree[10000];
int m,v,Type[10000],Ch[10000],Val[10000];
long long DP[10000][3];
long long go (int pos,int val)
{
	if (pos>m)
	{
		DEB("NOP");
		return INF;
	}
	if (Type[pos]==-1)
	{
		return Val[pos]!=val?INF:0;
	}
	
//	long long &y=DP[pos][val];
//	if (y!=-1)
//		return y;
	
	long long y1,y2,y3;
	long long y=INF;
	//if (!Ch[pos])
	{
		if (Type[pos])
		{
		  if (val==1)
		  {
				y= min (go(pos*2,1)+go (pos*2+1,1),y);
			}
			else
			{
				y1= go(pos*2,0)+go (pos*2+1,1);
				y2= go(pos*2,1)+go (pos*2+1,0);
				y3= go(pos*2,0)+go (pos*2+1,0);
				y= min (y,y1);
				y= min (y,y2);
				y= min (y,y3);
			}
		}
		else
		{
			if (val==0)
		  {
				y= min (go(pos*2,0)+go (pos*2+1,0),y);
			}
			else
			{
				y1= go(pos*2,0)+go (pos*2+1,1);
				y2= go(pos*2,1)+go (pos*2+1,0);
				y3= go(pos*2,1)+go (pos*2+1,1);
				y= min (y,y1);
				y= min (y,y2);
				y= min (y,y3);
			}
		}
		
	}
	
	
	if (Ch[pos])
	{
		if (!Type[pos])
		{
		  if (val==1)
		  {
				y= min (go(pos*2,1)+go (pos*2+1,1)+1,y);
				
			}
			else
			{
				y1= go(pos*2,0)+go (pos*2+1,1)+1;
				y2= go(pos*2,1)+go (pos*2+1,0)+1;
				y3= go(pos*2,0)+go (pos*2+1,0)+1;
				y= min (y,y1);
				y= min (y,y2);
				y= min (y,y3);
			}
		}
		else
		{
			if (val==0)
		  {
				y= min (go(pos*2,0)+go (pos*2+1,0)+1,y);
			}
			else
			{
				y1= go(pos*2,0)+go (pos*2+1,1)+1;
				y2= go(pos*2,1)+go (pos*2+1,0)+1;
				y3= go(pos*2,1)+go (pos*2+1,1)+1;
				y= min (y,y1);
				y= min (y,y2);
				y= min (y,y3);
			}
		}
		
	}
	
	return y;
	
	
}
int main ()
{
	int c,cas=1;
	scanf ("%d",&c);
	freopen ("output","w",stdout);
	
	
	while (c--)
	{
		memset(Type,-1,sizeof Type);
//		memset(Ch,-1,sizeof Ch);
//		memset(Val,-1,sizeof Val);
		
		scanf ("%d%d",&m,&v);
		
		int q=0;
		REP(i,(m-1)/2)
		{
			scanf ("%d%d",&Type[i+1],&Ch[i+1]);
			//Val[i+1]=-1;
			q++;
		}
		REP(i,(m+1)/2)
		{
			//Type[i+q+1]=-1;
			scanf ("%d",&Val[i+q+1]);
		}	
		DEB("asd");
		memset(DP,-1,sizeof DP);
		printf ("Case #%d: ",cas++);
		long long y=go (1,v);
		if (y>=INF)
			printf ("IMPOSSIBLE");
		else
			printf ("%lld",y);
		
		printf ("\n");
	}
	fclose(stdout);
}


