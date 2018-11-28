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
#define INF 1073741823
#define DEB(x) cerr<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define DEBV(b) FOREACH(it,b) cerr<<(*it)<<"\n";cerr <<"\n";
char Pal[100][100];
int DP[2000][10];
vector<int> V;
int n,m;
int Count()
{
	int b=0;

	REP(i,n)
	{
		REP(j,m)
		{
			if (V[i]&(1<<j))
			{
				b++;
			}
		}
	}
	return b;
}
bool val(int mask,int pos)
{
	REP(i,m)
	{
		if (mask&(1<<i)&&Pal[pos][i]=='x')
			return false;
	}
	REP(i,m-1)
	{
		if (mask&(1<<i))
		{
			if (mask&(1<<(i+1)))
				return false;
		}
	}
	return true;
}
bool valid(int mask1,int mask2)
{
	REP(i,m)
	FOR(dy,-1,1)
	{
		if (dy==0) continue;
		int y=i+dy;
		if (y<0||y>=m) continue;
		if (mask1&(1<<i)&&mask2&(1<<y)) return false;
	}
	return true;
	
}
bool validsdfasd(int mask,int pos)
{
	REP(i,m)
	{
		if (mask&(1<<i)&&Pal[pos][i]=='x')
			return false;
	}
	return true;
}

int Cont(int pos)
{
	int r=0;
	while (pos)
	{
		if (pos%2==1) r++;
		pos/=2;
	}
	return r;
}
int go (int mask,int pos)
{
	if (pos==n)
	{
		return 0;
	}
	
	if (DP[mask][pos]!=-1)
	{
		return DP[mask][pos];
	}
	int &res=DP[mask][pos];
	res=0;
	//int res=0;
	REP(i,1<<m)
		{
			if (val(i,pos)&&valid(i,mask))
			{
				V.PB(i);
				res=max(res,go (i,pos+1)+Cont(i));
				V.pop_back();
			}
		}
	return res;
}
int main ()
{
	int c,cas=1;
	scanf ("%d",&c);
	
	freopen ("output","w",stdout);
	while (c--)
	{
		
		printf ("Case #%d: ",cas++);
		scanf ("%d%d",&n,&m);
		REP(i,n)
		{	
			scanf ("%s",Pal[i]);
		}
		int res=0;
		memset(DP,-1,sizeof DP);
		REP(i,1<<m)
		{
			if (val(i,0))
			{
				V.PB(i);
				res=max(res,go(i,1)+Cont(i));
				V.pop_back();
			}
		}
		printf ("%d",res);
	
		printf ("\n");
	}
	fclose(stdout);
}
