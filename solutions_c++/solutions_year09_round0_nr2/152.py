#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
#include <cmath>
#include <iomanip>

using namespace std;

typedef vector <int> VI;
typedef vector <string> VS;
typedef long long LL;
typedef stringstream SS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<(b); i++)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define PB push_back
#define sz size()
#define MP make_pair
#define two(x) (1<<(x))


/////////////////////////////////////////////////////////////////////////////////
int T, H, W;


int mp[100][100];
char lb[100][100];

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

char cur;

char go(int x, int y)
{
	if(lb[x][y]!='*') return lb[x][y];
	int p=mp[x][y];
	int chosen=-1;

	REP(i,4)
	{
		int x0=x+dx[i];
		int y0=y+dy[i];
		if( x0>=0 and y0>=0 and x0<H and y0<W and mp[x0][y0]<p ) { chosen=i; p=mp[x0][y0]; }
	}
	if(chosen!=-1)
	{
		lb[x][y]=go(x+dx[chosen], y+dy[chosen]);
		return lb[x][y];
	}
	else
	{
		if(lb[x][y]=='*') cur++;
		lb[x][y]=cur;
		return lb[x][y];
	}

}

int main()
{
	cin >> T;
	int index=0;
	while(index<T)
	{
		cin>>H>>W;
		REP(i,H) REP(j,W) { cin>>mp[i][j]; lb[i][j]='*'; }
		
		cur='a'-1;

		REP(i,H) REP(j,W)  go(i,j);

		cout << "Case #" << ++index <<":" << endl;
		REP(i,H) { REP(j,W) cout<<lb[i][j]<<" "; cout<<endl; }
	}
	return 0;

}
