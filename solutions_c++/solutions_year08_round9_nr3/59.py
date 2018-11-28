#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker,"/STACK:64000000")

#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <cctype>
#include <cassert>

using namespace std; 

#define sz(v) ((int) (v).size())
#define all(v) (v).begin(), (v).end()
#define mp make_pair
#define pb push_back

typedef double D;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;

template<typename T> T abs(T x) { return x>0 ? x : -x; }
template<typename T> T sqr(T x) { return x*x;          }

int r,c;
int a[5][5];
bool was[5][5];
int res=0;

const int dx[]={0,-1,1,0,0,1,1,-1,-1};
const int dy[]={0,0,0,-1,1,1,-1,1,-1};

bool norm(int x, int y) {
	return x>=0 && y>=0 && x<r && y<c;
}

void solve(int at) {
	if (at==r*c) {
		for (int i=0; i<r; i++)
			for (int j=0; j<c; j++)
				if (a[i][j]!=0) 
					return;
		int cur=0;
		for (int j=0; j<c; j++)
			cur+=was[r/2][j];
		res=max(res,cur);
		return;
	}
	int x=at%r, y=at/r;
	solve(at+1);
	bool bad=false;
	for (int t=0; t<9; t++) {
		int xx=x+dx[t];
		int yy=y+dy[t];
		if (!norm(xx,yy)) continue;
		a[xx][yy]--;
		if (a[xx][yy]<0) bad=true;
	}
	was[x][y]=true;
	if (!bad) 
		solve(at+1);
	was[x][y]=false;
	for (int t=0; t<9; t++) {
		int xx=x+dx[t];
		int yy=y+dy[t];
		if (!norm(xx,yy)) continue;
		a[xx][yy]++;
	}
}

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	int tn;
	cin>>tn;
	for (int tst=0; tst<tn; tst++) {
		printf("Case #%d: ",tst+1);
		cerr<<tst<<endl;
		cin>>r>>c;
		for (int i=0; i<r; i++)
			for (int j=0; j<c; j++)
				cin>>a[i][j];
		res=0;
		solve(0);
		cout<<res<<endl;
	}

	return 0;
}
