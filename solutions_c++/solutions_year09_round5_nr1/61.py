#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdlib>

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

const int dx[]={-1,1,0,0};
const int dy[]={0,0,-1,1};

int n,m;

vs b;
bool used[15][15];

void dfs(int x, int y) {
	used[x][y]=true;
	for (int t=0; t<4; t++) {
		int xx=x+dx[t];
		int yy=y+dy[t];
		if (!used[xx][yy] && b[xx][yy]=='x')
			dfs(xx,yy);
	}
}

bool connected(const vs &v) {
	b=v;
	bool was=false;
	memset(used,false,sizeof(used));
	for (int i=1; i<=n; i++)
		for (int j=1; j<=m; j++)
			if (v[i][j]=='x' && !used[i][j]) {
				if (was) return false;
				dfs(i,j);
				was=true;
			}
	return true;
}

int solve(vs v) {
	queue<pair<vs,bool> > q;
	map<pair<vs,bool>,int> d;
	vi X,Y;
	for (int i=1; i<=n; i++)
		for (int j=1; j<=m; j++) {
			if (v[i][j]=='x')
				v[i][j]='o';
			else if (v[i][j]=='o')
				v[i][j]='x';
		}
	for (int i=1; i<=n; i++)
		for (int j=1; j<=m; j++) {
			if (v[i][j]=='o') {
				v[i][j]='.';
				X.pb(i); 
				Y.pb(j);
			}
			if (v[i][j]=='w') {
				v[i][j]='x';
				X.pb(i); 
				Y.pb(j);
			}
		}
	q.push(mp(v,true));
	d[mp(v,true)]=0;
	while (!q.empty()) {
		vs cur=q.front().first;
		bool good=q.front().second;
		q.pop();
		bool final=true;
		for (int i=0; i<sz(X); i++)
			if (cur[X[i]][Y[i]]!='x') {
				final=false;
				break;
			}
		if (final) return d[mp(cur,good)];
		for (int i=1; i<=n; i++)
			for (int j=1; j<=m; j++) {
				if (cur[i][j]!='x') continue;
				for (int t=0; t<4; t++) {
					if (cur[i+dx[t]][j+dy[t]]!='.') continue;
					if (cur[i+dx[t^1]][j+dy[t^1]]!='.') continue;
					vs next=cur;
					next[i][j]='.';
					next[i+dx[t]][j+dy[t]]='x';
					bool conn=connected(next);
					if (d.count(mp(next,conn))) continue;
					if (!good && !conn) continue;
					d[mp(next,conn)]=d[mp(cur,good)]+1;
					q.push(mp(next,conn));
				}
			}
	}
	return -1;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=1; tst<=tn; tst++) {
		cerr<<tst<<endl;
		printf("Case #%d: ",tst);
		cin>>n>>m;
		vs v;
		v.resize(n+2);
		for (int i=0; i<n+2; i++)
			v[i].resize(m+2);
		for (int i=0; i<n+2; i++)
			for (int j=0; j<m+2; j++)
				v[i][j]='#';
		for (int i=1; i<=n; i++)
			for (int j=1; j<=m; j++) {
				char ch;
				do {
					cin>>ch;
				} while (ch<=' ');
				v[i][j]=ch;
			}
		cout<<solve(v)<<endl;
	}

	return 0;
}
