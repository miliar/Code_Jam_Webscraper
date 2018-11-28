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
#define DEB(x) cout<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define i64 long long 
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
int DP[1000][100];
string h="welcome to code jam";
string s;
int go (int a,int b)
{
	if (b==SZ(h))
	{
		return 1;
		
	}
	if (a==SZ(s))
		return 0;
	int &y=DP[a][b];
	if (y!=-1)
	{
		return y;
	}
	y=0;
	y+=go (a+1,b);
	if (s[a]==h[b])
	{
		y+=go(a+1,b+1)%10000;
		y%=10000;
	}	
	return y%10000;
}
char Pal[1213];
string toString(int a)
{
//	DEB(a);
	sprintf (Pal,"%d",a%10000);
	string e=Pal;
	while (SZ(e)<4)
		e="0"+e;
	return e;
}
int main ()
{


	int c;
	scanf ("%d",&c);
	gets(Pal);
	FOR(cas,1,c)
	{
		memset(DP,-1,sizeof DP);
		gets (Pal);
		s=Pal;
		int y=go (0,0);
		printf ("Case #%d: %s\n",cas,toString(y).c_str());
	}
	return 0;
}
