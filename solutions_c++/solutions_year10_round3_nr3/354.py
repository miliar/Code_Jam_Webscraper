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
#include <string.h>
using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cerr<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define i64 long long 
#define CLEAR(V,v) memset(V,v,sizeof V)
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define OUT(a,b,c) ((a)<(b)||(a)>(c))
#define IN(a,b,c) ((a)>=(b)&&(a)<=(c))
vector<int> SplitInt(string &s)
{
	vector<int>Res;int tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;
}

vector<string> SplitStr(string &s)
{
	vector<string>Res;string tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;
}

//////////////////////////////////////////////////////////////
vector<string> P;
bool test(int x,int y,int s)
{
	
	if (x+s-1>=SZ(P)) return false;
	if (y+s-1>=SZ(P[0])) return false;
	char c=P[x][y]-'0';
	REP(i,s)
	{
		
		REP(j,s)
		{
			if (P[i+x][j+y]=='2')
				return false;
			if (j%2==0&&P[i+x][j+y]-'0'==c)  continue;
			if (j%2==1&&P[i+x][j+y]-'0'==(!c))  continue;
			return false;
		}
		c=!c;
	}
	return true;
}
bool left(int &x,int &y,int &s)
{
	int n=SZ(P),m=SZ(P[0]);
	int best=0;
	REP(i,n)
	REP(j,m)
	{
		FOR(size,best+1,n)
		if (test(i,j,size))
		{
			if (size>best)
			{
				best=size;
				x=i;
				y=j;
			}
		}
	}
	if (best>=1)
	{
		REP(i,best)
		REP(j,best)
		{
			P[i+x][j+y]='2';
		}
		s=best;
		return true;
	}
	return false;
}
string toB(long long t,int n)
{
	string b;
	REP(i,n)
	{
		if (t&(1<<i))
			b+='1';
		else
			b+='0';
	}
	reverse(ALL(b));
	return b;
}
string tobin(string s,int n)
{
	string t;
	long long r=0;
	long long y=1;
	FORD(i,SZ(s)-1,0)
	{
		int val;
		if (isdigit(s[i]))
			val=s[i]-'0';
		else
			val=s[i]-'A'+10;
		r+=val*y;
		y*=16;
	}
	
	return toB(r,n);
}
char Pal[1123];
int main ()
{
	int c,M,C;
	scanf ("%d",&c);
	
	FOR(cas,1,c)
	{
		int res=0,n,m;
		P.clear();
		scanf ("%d%d",&n,&m);
		REP(i,n)
		{
			scanf ("%s",Pal);
			P.PB(tobin(Pal,m));
//			DEB(P.back());
		}
		vector<pair<int,int> > R;
		int H[50]={0};

		while (1)
		{
			int x,y,s1;
			if (left(x,y,s1))
			{
				R.PB(make_pair(x,y));
				H[s1]++;
//				REP(i,SZ(P))
//					DEB(P[i]);
//				DEB(s);
//				DEB(x);
//				DEB(y);
//				if(SZ(R)==8)
//				while(1);
			} 
			else
				break;
		}
		vector<pair<int,int> > TT;
		REP(i,50)
		if (H[i])
			TT.PB(make_pair(i,H[i]));
		reverse(ALL(TT))	;
		printf ("Case #%d: %d\n",cas,SZ(TT));
//		
//		FOREACH(it,T)
//		{
//			TT.PB(make_pair((*it).first,(*it).second));
//		}
		REP(i,SZ(TT))
			printf ("%d %d\n",TT[i].first,TT[i].second);
	}
	return 0;
}
