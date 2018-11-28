#include<iostream>
#include<cstdio>
#include<cmath>
#include<complex>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<sstream>
#include<utility>

using namespace std;
using namespace __gnu_cxx;

typedef long long _ll;
typedef double _db;
typedef unsigned int _ui;
typedef vector<int> _vi;
typedef vector<vector<int> > _vvi;
typedef vector<string> _vs;
typedef istringstream _is;
typedef ostringstream _os;

#define INF (1<<30)
#define INFLL (1LL<<61LL)
#define EPS = (1e-9)
#define PB push_back
#define FI first
#define SE second
#define ALL(v) (v).begin(),(v).end()
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
#define FORS(i,a) for(int (i)=0;(i)<(int)(a).size();(i)++)
#define FORE(i,a) for(__typeof((a).begin()) i=(a).begin();i!=(a).end();i++)
#define PRINT(v) for(int (i)=0;(i)<(int)(a).size();(i)++) cerr<<v[i]<<" "; cerr<<endl;

int alts[100][100];
bool sink[100][100];
int ids[100][100];
bool lnks[100][100][4];

void dfs(int x, int y, int id){
	if(ids[x][y] != -1) return;
	ids[x][y] = id;
	if(lnks[x][y][0]) dfs(x-1,y,id);
	if(lnks[x][y][1]) dfs(x,y-1,id);
	if(lnks[x][y][2]) dfs(x,y+1,id);
	if(lnks[x][y][3]) dfs(x+1,y,id);
}

void run(int cs){
	int H,W;
	cin >> H >> W;
	REP(i,H) REP(j,W){
		cin >> alts[i][j];
		ids[i][j] = -1;
		sink[i][j] = false;
		REP(k,4) lnks[i][j][k] = false;
	}

	REP(i,H) REP(j,W){
		int minn = INF;
		int x,y,ll;
		if(i > 0 && alts[i-1][j] < minn){ minn = alts[i-1][j]; x = i-1; y = j; ll=3; }
		if(j > 0 && alts[i][j-1] < minn){ minn = alts[i][j-1]; x = i; y = j-1; ll=2;}
		if(j < W-1 && alts[i][j+1] < minn){ minn = alts[i][j+1]; x = i; y = j+1; ll=1;}
		if(i < H-1 && alts[i+1][j] < minn){ minn = alts[i+1][j]; x = i+1; y = j; ll=0;}

		if(minn < alts[i][j]){
			lnks[x][y][ll] = true;
			lnks[i][j][3-ll] = true;
		}
		else
			sink[i][j] = true;
	}

	int N = 0;
	REP(i,H) REP(j,W)
		if(ids[i][j] == -1)
			dfs(i,j,N++);

	cout << "Case #" << cs << ": \n";
	REP(i,H){
		REP(j,W)
			cout << (char)(ids[i][j]+'a') << " ";
		cout << "\n";
	}
}

int main(){
	ios::sync_with_stdio(0);
	int C;
	cin >> C;
	REP(i,C) run(i+1);
	return 0;
}

