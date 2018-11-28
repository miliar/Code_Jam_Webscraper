#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker,"/STACK:64000000")

#include <iostream>
#include <cstdio>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define sz(v) ((int)(v).size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;

template<class T>T abs(T x) { return (x>0) ? x : -x; }
template<class T>T sqr(T x) { return x*x;            }

const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};

int n,m;
int b[100][100];
vi to[100][100];
char ans[100][100];

bool norm(int x, int y) {
	return x>=0 && y>=0 && x<n && y<m;
}

void dfs(int x, int y, char what) {
	if (ans[x][y]) return;
	ans[x][y]=what;
	for (int i=0; i<sz(to[x][y]); i++) {
		int t=to[x][y][i];
		dfs(x+dx[t],y+dy[t],what);
	}
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=1; tst<=tn; tst++) {
		printf("Case #%d:\n",tst);
		cin>>n>>m;
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++) {
				cin>>b[i][j];
				to[i][j].clear();
			}
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++) {
				int bestT=-1, best=1<<30;
				for (int t=0; t<4; t++) {
					int x=i+dx[t];
					int y=j+dy[t];
					if (!norm(x,y)) continue;
					if (b[x][y]<b[i][j] && b[x][y]<best) {
						best=b[x][y];
						bestT=t;
					}
				}
				if (bestT==-1) continue;
				int x=i+dx[bestT];
				int y=j+dy[bestT];
				to[i][j].pb(bestT);
				to[x][y].pb(3-bestT);
			}
		memset(ans,0,sizeof(ans));
		char cur='a';
		for (int i=0; i<n; i++)
			for (int j=0; j<m; j++)
				if (ans[i][j]==0)
					dfs(i,j,cur++);
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) cout<<ans[i][j]<<" ";
			cout<<endl;
		}
	}

	return 0;
}
