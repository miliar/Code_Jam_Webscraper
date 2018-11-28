/*{{{*/
/*includes e defines*/
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
#include <sstream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> PII;
#define SZ(A) (int)(A).size()
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define FOREACH(A,B) for((__typeof (B).begin) A = (B).begin(); A != (B).end(); A++)
#define PB push_back
#define ALL(x) x.begin() , x.end()
#define MP make_pair
/*}}}*/
/*{{{*/
/*main*/
void solveCase();
int main() {
	int TESTES; scanf("%d", &TESTES);
	for(int TESTE = 1; TESTE <= TESTES; TESTE++) {
		printf("Case #%d: ", TESTE);
		solveCase();
	}
    return 0;
}
/*}}}*/

#define N 36
VI adj[N];
int dist[N][N];
int prof[N];
int usa[N+1];

int ansC, ansT;
int opa[N];
int n,m;

void atualiza(int c) {
	//vector<int> nada;
	int t = 0;
	FOR(i,n) opa[i] = 0;
	FOR(i,c) opa[ usa[i] ] = 1;
	FOR(i, c) {
		int v = usa[i];
	//	nada.push_back(v);
		FOR(j,SZ(adj[v])) {
			if( !opa[ adj[v][j] ] ) {
				t++;
				opa[ adj[v][j] ] = 1;
			}
		}
	}
	c--;
	if(c < ansC || (c == ansC  && t > ansT) ) {
		ansC = c;
		ansT = t;

		//printf("DA %d %d com\n", c,t);
		//FOR(i, SZ(nada)) printf("%d ", nada[i]);
		//printf("\n");

	} 
}

void solve(int v) {
	if(v == 1) {
		atualiza(prof[v]);
		return;
	}
	if(prof[v] >= prof[1]) return;

	usa[ prof[v] ] = v;
	FOR(i, SZ(adj[v])) {
		if( prof[ adj[v][i]  ] == prof[v] + 1 ) {
			solve( adj[v][i] );
		}
	}
}

void solveCase() {
	cin >> n >> m;
	FOR(i,n) adj[i].clear();
	FOR(i,n) FOR(j,n) dist[i][j] = 100;
	FOR(i,n) dist[i][i] = 0;
	FOR(i,m) {
		int a,b;
		scanf("%d,%d", &a, &b);
		adj[a].PB(b); adj[b].PB(a);
		dist[a][b] = dist[b][a] = 1;
	}
	FOR(k,n) FOR(i,n) FOR(j,n) dist[i][j] = min(dist[i][j] , dist[i][k] + dist[k][j]);
	FOR(i,n) prof[i] = dist[0][i];
//	dika();


	ansC = 100, ansT = -1;
	solve(0);
	cout << ansC << " " << ansT << endl;
}

