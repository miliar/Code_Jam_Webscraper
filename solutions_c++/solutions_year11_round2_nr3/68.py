//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <complex>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define F first
#define S second

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_N = 10 + 2;

int n;
bool adj[MAX_N][MAX_N];
int u[MAX_N];
vector< vector<int> > cycles;

bool mark[MAX_N];
vector<int> stk;

void bt(int v, int len){
	len--;
	stk.PB(v);
	mark[v] = true;
	if(len == 0){
		bool loop = false;
		FOR(i, SZ(stk))
			for(int j = i + 2; !loop && j < SZ(stk) - !i; j++)
				if(adj[stk[i]][stk[j]])
					loop = true;
		if(adj[stk.back()][stk[0]] && !loop)
			cycles.PB(stk);
		stk.pop_back();
		mark[v] = false;
		return;
	}
	for(int i = stk[0]; i < n; i++)
		if(!mark[i] && adj[i][v])
			bt(i, len);
	stk.pop_back();
	mark[v] = false;
}

int col;
int rang[MAX_N];

bool bt2(int v){
	if(v == n){
		FOR(i, SZ(cycles)){
			int cnt = 0;
			memset(mark, 0, sizeof mark);
			FOR(j, SZ(cycles[i]))
				if(!mark[rang[cycles[i][j]]]++)
					cnt++;
			if(cnt < col)
				return false;
		}
		return true;
	}
	FOR(i, col){
		rang[v] = i;
		if(bt2(v + 1))
			return true;
	}
	return false;
}

void print(int test, int col){
	printf("Case #%d: %d\n", test, col);
	FOR(i, n)
		printf("%d%c", rang[i] + 1, (i + 1 == n) ? '\n' : ' ');
}

int main(){
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++){
		scanf("%d", &n);
		memset(adj, 0, sizeof adj);
		FOR(i, n)
			adj[i][(i + 1) %n] = adj[(i + 1) % n][i] = true;
		int m;
		scanf("%d", &m);
		FOR(i, m)
			scanf("%d", &u[i]);
		FOR(i, m){
			int v;
			scanf("%d", &v);
			--v;
			--u[i];
			adj[v][u[i]] = adj[u[i]][v] = true;
		}
		cycles.clear();
		
		
		for(int len = 3; len <= n; len++){
			memset(mark, 0, sizeof mark);
			FOR(i, n)
				bt(i, len);
		}
		
		if(SZ(cycles[0]) >= 5){
			cerr<<"Bad\n";
			printf("Case #%d: %d\n", test, SZ(cycles[0]));
			continue;
		}
		
		col= 4;
		if(bt2(0)){
			print(test, 4);
			continue;
		}
		
		col= 3;
		if(bt2(0)){
			print(test, 3);
			continue;
		}
		col= 2;
		if(bt2(0)){
			print(test, 2);
			continue;
		}
		memset(rang, 0, sizeof rang);
		print(test, 1);
		/*FOR(i, SZ(cycles)){
			FOR(j, SZ(cycles[i]))
				cerr<< cycles[i][j] + 1 << " ";
			cerr<<endl;
		}*/
	}
	return 0;
}
