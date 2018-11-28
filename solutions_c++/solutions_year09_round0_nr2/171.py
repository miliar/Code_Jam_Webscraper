#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;

const int MAXN = 120;
const int INF = 1000000000;
const int dir[4][2] = { { -1, 0 } , { 0, -1 } , { 0, 1 }, { 1, 0 } };
int N, M;
int a[MAXN][MAXN];
int fa[MAXN*MAXN], c[MAXN*MAXN];

inline int trans(int x, int y) { return x * M + y; }
inline int legal(int x, int y) { return x>=0 && x<N && y>=0 && y<M; }
void init() {
	cin>>N>>M;
	for (int i=0;i<N;i++)
		for (int j=0;j<M;j++)
			cin>>a[i][j];
	for (int i=0;i<N;i++)
		for (int j=0;j<M;j++) {
			int min = INF, ci = -1, cj = -1;
			for (int di=0;di<4;di++) { //order: North , West , East, South
				int tx = i + dir[di][0], ty = j + dir[di][1];
				if (legal(tx,ty))
					if (a[tx][ty] < a[i][j])
						if (a[tx][ty]<min) {
							min = a[tx][ty];
							ci = tx; cj = ty;
						}
			}
			if (min==INF) fa[trans(i,j)] = trans(i,j); else fa[trans(i,j)] = trans(ci, cj);
		}
/*	for (int i=0;i<N;i++) {
		for (int j=0;j<M;j++)
			cout<<fa[trans(i,j)]<<" ";
		cout<<endl;
	}
	cout<<endl;*/
}

int getfa(int x) { return fa[x] == x ? fa[x] : fa[x] = getfa(fa[x]); }

void work() {
	for (int i=0;i<N*M;i++)
		fa[i] = getfa(i);
	memset(c, -1, sizeof(c));
	int ct = 0;
	for (int i=0;i<N*M;i++)
		if (c[fa[i]] == -1) {
			c[fa[i]] = ct;
			ct ++;
			c[i] = c[fa[i]];
		} else c[i] = c[fa[i]];
	for (int i=0;i<N;i++) {
		for (int j=0;j<M-1;j++)
			cout<<char('a'+c[trans(i,j)])<<" ";
		cout<<char('a'+c[trans(i,M-1)])<<endl;
	}
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	cin>>T;
	for (int ti=1;ti<=T;ti++) {
		cout<<"Case #"<<ti<<":"<<endl;
		init();
		work();
	}
	return 0;
}

