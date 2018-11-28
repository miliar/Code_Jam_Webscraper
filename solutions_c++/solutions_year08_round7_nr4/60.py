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

map<vector<string>,int>DP[2];
vector<string> make_move(vector<string> &M,int dx,int dy,int &ok)
{
	int x,y;
	REP(i,SZ(M))
	REP(j,SZ(M[0]))
	{
		if (M[i][j]=='K')
		{
			x=i;
			y=j;
			i=1000;
			j=1000;
		}
	}

	int nx=x+dx;
	int ny=y+dy;

	
	if (nx<0||ny<0||nx>=SZ(M)||ny>=SZ(M[0]) )
	{
		ok=-1;
		return M;
	}
	if (M[nx][ny]=='#')
	{
		ok=-1;
		return M;
		
	}
	vector<string> S=M;
	S[x][y]='#';
	S[nx][ny]='K';
	ok=0;
	return S;
}
int go (vector<string> &cur,int pos)
{
	
	if (DP[pos].find (cur)!=DP[pos].end())
	{
		return DP[pos][cur];
	}
	int &y=DP[pos][cur];
	y=-1;
	FOR(i,-1,1)
	FOR(j,-1,1)
	if (i!=0||j!=0)
	{
		
		
		int ok;
		vector<string>r=make_move(cur,i,j,ok);
		
		if (ok==-1)
			continue;
		y=go (r,!pos);
		
		if (y!=pos)//gano
			return !pos;
		
	}
	y=pos;//pierdo
	return pos;
}



int main ()
{
	int c,cas=1;
	scanf ("%d",&c);
	
	freopen ("output","w",stdout);
	while (c--)
	{
		DP[0].clear();
		DP[1].clear();
		printf ("Case #%d: ",cas++);
		int n,m;
		scanf ("%d%d",&n,&m);
		vector<string > M;
		char pal[100];
		REP(i,n)
		{
			scanf ("%s",pal);
			M.PB(pal);
			DEB(pal);
		}
		int ok=go (M,0);
		if (ok)
			printf ("A");
		else
			printf ("B");

		printf ("\n");
	}
	fclose(stdout);
}
