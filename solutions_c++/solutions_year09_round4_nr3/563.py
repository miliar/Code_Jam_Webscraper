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

int n,k;

int p[100][25];
int UU[100][25];

vector<int> s[100];


vi adj[100];
int nao[100][100];

struct P {
	ll x,  y;
};

P ponto(int a, int b) {
	P x;
	x.y = a;
	x.x = b;
	return x;
}

int left(P a, P b, P c)  {
	ll aux = (a.x-c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x);
	return aux >= 0;
}

int inter(int xa1, int xa2, int xb1, int xb2, int y) {
	if(xa1 == xb1) return 1;
	if(xa2 == xb2) return 1;
	if(xa1 > xb1) {
		if(xa2 < xb2) 
			return 1;
	}
	if(xa1 < xb1)
		if(xa2 > xb2)
			return 1;
	

	return 0;
}

int ok(int x, int pp) {
	FOR(i, sz(s[pp])) {
		FOR(j,k-1) {
			if(inter(p[x][j], p[x][j+1], p[s[pp][i]][j], p[s[pp][i]][j+1], j)) {
//				printf("%d bate com %d\n", x, s[pp][i]);
				return 0;
			}
		}
	}
	return 1;
}

int ok2(int x, int y) {
		FOR(j,k-1) {
			if(inter(p[x][j], p[x][j+1], p[y][j], p[y][j+1], j)) {
				return 0;
			}
		}
	return 1;
}



int calc() {
	int rr = 0;
	FOR(i,n) {
		FOR(j,n) {
			if(ok(i,j)) {
				s[j].push_back(i);
//				printf("insere %d em %d\n", i, j);
				rr = max(rr , j+1);
				break;
			}
		}
	}
	return rr;
}

int v[30];

int cmp(int a, int b) {

	FOR(i,k) {
		if(p[a][i] != p[b][i])
			return p[a][i] < p[b][i];
	}

	return false;
}

void arruma() {

	FOR(i,n) v[i] = i;
	sort(v, v+n, cmp);
	FOR(i,n) {
		FOR(j,k) 
			UU[i][j] = p[ v[i] ][ j];
	}
	FOR(i,n) FOR(j,k) p[i][j] = UU[i][j];

}

int ja[100];
int pd[ (1<<16) ];

int base(int xx) {
	FOR(i,n) {
		if((1<<i) & xx) {
			FOR(j,n) {
				if(i == j) continue;
				if((1 << j) & xx)
					if(nao[i][j]) return 0;
			}
		}
	}
	return 1;
}


int vamo( int xx, vi fila) {
	if(pd [ xx ] != -1) {
		int oo = 0;
		if(sz(fila))
			oo = 1;
		return pd[xx] + oo;
	}
	if( base (xx )) {
		pd[xx] = 1;
		if(sz(fila))
			return 2;
		return 1;
	}

	int aux = n;
	vi h;
	h.clear();
	FOR(i,n) {
		if((1<<i) & xx) {
			int ok = 1;
			FOR(j,sz(fila)) {
				if(nao[ fila[j] ][ i ])
					ok = 0;
			}
			if(ok)
				h.pb(i);
		}
	}

	if(sz(h) == 0) {
		FOR(i,sz(fila)) h.pb(fila[i]);
		fila.clear();
		pd[xx] = vamo(xx, fila);
		return pd[xx] + 1;
	}
	else {
		FOR(i, sz(h)) {
			fila.pb(h[i]);
			int opa = vamo(xx - (1<<h[i]), fila);
			aux = min(opa, aux);
			fila.pop_back();
		}
	}

	return pd[xx] = aux;
}

int Calc(int xx) {
	int rr = 0;
	memset(nao,0,sizeof(nao));
	FOR(i,n)
		FOR(j,n)
		if(!ok2(i,j)) {
			nao[i][j] = 1;
		}

	memset(pd, -1, sizeof(pd));

	vi uu;

	return vamo(xx, uu);

}

int main() {
	int T;
	scanf("%d", &T);
	FOR(t,T) {
		printf("Case #%d: " , t+1);
		scanf("%d %d", &n, &k);
		FOR(i,n) FOR(j,k) scanf("%d" , &p[i][j]);	
		FOR(i,n) s[i].clear();
		FOR(i,n) adj[i].clear();
		arruma();
		int rr = Calc((1<<n)-1);
		printf("%d\n", rr);
	}

    return 0;
}

