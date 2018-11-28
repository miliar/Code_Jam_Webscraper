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
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

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
vector<string>  rotate(vector<string> &s)
{
	vector<string> T;
	REP(i,SZ(s[0]))
	{
		string r;
		REP(j,SZ(s))
			r+=s[j][i];
		T.PB(r);
	}
	REP(i,SZ(T))
		reverse(ALL(T[i]));
	//reverse(ALL(T));
	REP(i,SZ(T[0]))
	{
		int m=SZ(T)-1;
		string h;
		FORD(j,m,0)
			if (T[j][i]!='.')
				h+=T[j][i];
		while (SZ(h)<SZ(T))
			h+='.';
		reverse(ALL(h));
		FORD(j,m,0)
			T[j][i]=h[j];
		
	}
//	REP(i,SZ(T))
//		DEB(T[i]);
	return T;
}
int K;
bool dfs(char c,int x,int y,int cont,int dx,int dy,vector<string> &P)
{
//	DEB(cont);
	if (cont==K)
		return true;
	int nx=x+dx;
	int ny=y+dy;
	if (nx<0||ny<0||nx>=SZ(P)||ny>=SZ(P[0]))
		return false;
	if (P[nx][ny]==c)
	{
		return dfs(c,nx,ny,cont+1,dx,dy,P);
	}
	return false;
}
bool test(char c,vector<string> &P)
{
//	DEB(K);
	REP(i,SZ(P))
	REP(j,SZ(P[0]))
	{
		if (c==P[i][j])
		{
			FOR(dx,-1,1)
			FOR(dy,-1,1)
			{
				if (abs(dx)||abs(dy))
				if (dfs (c,i,j,1,dx,dy,P))
				return true;

			}
		}
		
	}
}
char Pal[123];
int main ()
{
	int c,M,C;
	scanf ("%d",&c);
	
	FOR(cas,1,c)
	{
		string res;
		int n,m;
		scanf ("%d%d",&n,&K);
		vector<string> T;
		REP(i,n)
		{
			scanf ("%s",Pal);
			T.PB(Pal);
		}
		T=rotate(T);
		bool r=test('R',T);
		bool b=test('B',T);
		if (b&&r)
			res="Both";
		if (b&&!r)
			res="Blue";
		if (!b&&r)
			res="Red";
		if (!b&&!r)
			res="Neither";	
		printf ("Case #%d: %s",cas,res.c_str());
		
		printf ("\n");
	}
	return 0;
}
