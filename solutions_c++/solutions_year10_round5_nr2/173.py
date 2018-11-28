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
#define inf (1<<25)
#define infL 10000000000000000LL
#define F first
#define S second
#define all(x) x.begin() , x.end()

#define N 30000
int v[100];
ll l;
int n;

int pd2[N];

/*
int pd[N][100];

int PD(int falta, int pos) {
	if(falta == 0) return 0;
	if(falta < 0) return -2;
	if(pos < 0) return -2;
	if(pd[falta][pos] != -1) 
		return pd[falta][pos];

	int x = v[pos];
	if(falta % x != 0) {
		if(pos == 0) return -2;
	}
	else
		return falta / x;

	int res = -2, vai;
	for(int i = falta / x; i > 0 ;i--) {
		vai = x * i;
		int aux = PD(falta - vai, pos-1);
		if(aux == -2) continue;
		if(res == -2) res = aux + i;
		else res = min(res, aux+i);
	}	

	return pd[falta][pos] = res;
}*/

ll PD2(int falta, int nada) {
	memset(pd2, -1, sizeof(pd2));
	pd2[0] = 0;

	FOR(k, falta) {
		if(pd2[k] == -1) continue;
		FOR(i, n) {
			for(int j = 1; ;j++) {
				int pos = k + (j*v[i]);
				if(pos > falta) break;
				int qtd = pd2[k] + j;
				if(pd2[pos] == -1 || qtd < pd2[pos])
					pd2[pos] = qtd;
			}
		}
	}

	return pd2[falta];
}

ll calc() {
	sort(v, v+n);
	ll maior = v[n-1];
	ll qtd = (l - N) / maior;
	l -= (qtd*maior);
	while(l >= N) {
		l -= maior;
		qtd++;
	}

//	memset(pd, -1, sizeof(pd));
	int aux = PD2(l, n-1);
	if(aux <= -1) return -1;
	qtd += aux;
	return qtd;
}

int main() {
	int T;
	scanf("%d", &T);
	FOR(t,T) {
		printf("Case #%d: " , t+1);
		scanf("%lld %d\n", &l, &n);
		FOR(i,n) scanf("%d", &v[i]);
		ll r = calc();
		if(r == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%lld\n", r);
	}

    return 0;
}

