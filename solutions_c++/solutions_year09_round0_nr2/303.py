#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define sz(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define pb push_back
#define pii pair<int,int>
#define inf (1<<25)
#define infL 10000000000000000LL
#define F first
#define S second
#define all(x) x.begin() , x.end()

int n,m;
int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};
int tab[100][100];

vector< pair<int,int> > adj[100][100];
int ja[100][100];
map<int, char> cor;
char prox;

void dfs(int x, int y, int c) {
	if(ja[x][y] != -1) return;
	ja[x][y] = c;
	FOR(i, sz(adj[x][y])) {
		dfs( adj[x][y][i].first, adj[x][y][i].second, c);
	}
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(t,T) {
		printf("Case #%d:\n", t+1);
		scanf("%d %d", &n, &m);
		FOR(i,n) FOR(j,m) {
			scanf("%d", &tab[i][j]);
			adj[i][j].clear();
			ja[i][j] =  -1;
		}
		cor.clear();
		prox = 'a' - 1;

		FOR(i,n) {
			FOR(j,m) {
				int mm = tab[i][j];
				int mx = i; int my = j;
				FOR(k,4) {
					int ii = i + dx[k];
					int jj = j + dy[k];
					if(ii < 0 || ii >= n) continue;
					if(jj < 0 || jj >= m) continue;
					if(tab[ii][jj] < mm) {
						mm = tab[ii][jj];
						mx = ii; my = jj;
					}
				}

				if(mx != i || my != j) {
					adj[i][j].pb(pii(mx,my));
					adj[mx][my].pb(pii(i,j));
				}

			}
		}

		int aux = 0;
		FOR(i,n) FOR(j,m) {
			if(ja[i][j] == -1) {
				dfs(i,j, aux);
				aux++;
			}
		}

		FOR(i,n) {
			FOR(j,m) {
				if(j != 0) printf(" ");
				if(!cor.count(ja[i][j])) 
					cor[ja[i][j]] = ++prox;
				printf("%c", cor[ja[i][j]]);
//				printf("%d", ja[i][j]);
			}
			printf("\n");
		}

	}


    return 0;
}

