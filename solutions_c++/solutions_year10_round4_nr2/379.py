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

#define sz(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define pb push_back
#define pii pair<int,int>
#define F first
#define S second
#define all(x) x.begin() , x.end()

#define inf 10000000000LL

#define N (1<<10)

int p;
int m[N];
int cst[10][N];
ll pd[11][N][11];

int temGente(int ini, int fim) {
	for(int i = ini;i <= fim; i++)
		if(m[i] > 0) return 1;
	return 0;
}

void diminui(int ini, int fim, int val) {
	for(int i = ini;i <= fim; i++) m[i] += val;
}

ll vai(int ini, int fim, int prof, int filho, int qtd) {
	
	for(int i = ini; i <= fim; i++)
		if(m[i] > p) return inf;

	if(ini == fim) {
		if(m[ini] <= 0)
			return 0;

		return inf;

		if(m[ini] == 1)
			return cst[0][ini];
		return inf;
	}
	if(!temGente(ini,fim)) return 0;

	if(pd[prof][filho][qtd] != -1)
		return pd[prof][filho][qtd];

	int meio = (ini+fim) / 2;

	ll r2 = vai(ini,meio, prof-1, 2*filho, qtd) + vai(meio+1,fim, prof-1, 2*filho+1, qtd);
	if(r2 >= inf) 
		r2 = inf;

	diminui(ini,fim,-1);

	ll r1 = vai(ini,meio, prof-1, 2*filho, qtd+1) + vai(meio+1,fim, prof-1, 2*filho+1, qtd+1);
	if(r1 >= inf) r1 = inf;
	else {
		r1 += cst[prof-1][filho];
	}
	diminui(ini,fim,1);

	return pd[prof][filho][qtd] = min(r1,r2);
}

int calc() {
	return vai(0, (1<<p)-1, p, 0, 0);
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(t,T) {
		printf("Case #%d: " , t+1);
		cin >> p;
		FOR(i, (1<<p)) {
			scanf("%d", &m[i]);
			m[i] = p - m[i];
		}
		int aux = p-1;
		int pos = 0;
		while(aux >= 0) {
			FOR(i, (1<<aux))
				scanf("%d", &cst[pos][i]);
			aux--;
			pos++;
		}
		memset(pd, -1, sizeof(pd));
		cout << calc() << endl;
	}

    return 0;
}

