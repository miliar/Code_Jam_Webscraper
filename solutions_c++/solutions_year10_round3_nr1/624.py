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
bool in(int x,int y,int X,int Y)
{
	if (x<X&&y>Y) return true;
	if (x>X&&y<Y) return true;
	return false;
}
int a[10000],b[10000];
int n;
int main ()
{
	int c,M,C;
	scanf ("%d",&c);
	
	FOR(cas,1,c)
	{
		int res=0;
		scanf ("%d",&n);
		REP(i,n)
		{
			scanf ("%d%d",&a[i],&b[i]);
		}
		REP(i,n)
		REP(j,i)
		{
			if (in(a[i],b[i],a[j],b[j]))
				res++;
		}
		printf ("Case #%d: %d",cas,res);
		
		printf ("\n");
	}
	return 0;
}
