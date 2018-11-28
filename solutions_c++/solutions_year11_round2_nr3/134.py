#pragma comment(linker, "/STACK:16777216")

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <functional>
#include <numeric>

using namespace std;

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i+1 << " "; cout << endl; }

typedef long long ll;

#define eps 1e-10
#define inf 0x3f3f3f3f
#define INF 0x3f3f3f3f3f3f3f3fLL

#define fr(x,y,z) for(int(x)=(y);(x)<(z);(x)++)
#define cast(x,t) *({stringstream ss;static t __ret;ss<<x,ss>>__ret;&__ret;})
#define rep(x,n) for(int x = 0; x < (n); x++)

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

// var
const int maxn = 2000 + 10;
int n, m;
vector<int> adj[maxn];
int tab[maxn][maxn];
int u[maxn], v[maxn];

int read() {
	scanf("%d %d",&n,&m);
	rep(i,m) scanf("%d",u+i), u[i]--;
	rep(i,m) scanf("%d",v+i), v[i]--;
	return 1;
}

void liga(int x, int y) {
	tab[x][y] = tab[y][x] = 1;
	adj[x].push_back(y);
	adj[y].push_back(x);
}

vector< vector<int> > ciclos;

int cor[maxn];
int opa[maxn], best;

int conta(vector<int>& v) {
	map<int,int> mapa;
	rep(i,v.size()) if(cor[v[i]] == -1) return 100; else mapa[ cor[ v[i] ] ]++;
	return mapa.size();
}

int ok(vector<int>& v, int opa) {
	map<int,int> mapa;
	rep(i,v.size()) if(cor[v[i]] == -1) return 0; else if(cor[v[i]] >= opa) return 0;
	return 1;
}

void go(int x) {
	// cut
	int nbest = 100; rep(i,ciclos.size()) nbest = min(nbest, conta(ciclos[i]));
	if(nbest <= best) return;

	if(x >= n) {
		int vai = 1;
		rep(i,ciclos.size()) vai &= ok(ciclos[i],nbest);
		if(vai) {best = nbest; rep(i,n) opa[i] = cor[i];}
		return;
	}
	
	int vmax = 0; rep(i,n) vmax = max(vmax,cor[i]+2);
	
	rep(xx,vmax) {
		cor[x] = xx;
		go(x+1);
		cor[x] = -1;
	}

}

void process() {
	memset(tab,0,sizeof tab);
	rep(i,n) adj[i].clear();
	rep(i,n) liga(i,(i+1)%n);
	rep(i,m) liga(u[i],v[i]);
	
	// achar ciclos
	ciclos.clear();
	rep(i,1<<n) if(__builtin_popcount(i) > 2) {
		vector<int> vet;
		rep(j,n) if(i >> j & 1) {
			int last = -1;
			vet.push_back(last = j);
			rep(k,n) if(i >> k & 1) if(last < k) {
				if(!tab[last][k]) goto end;
				else vet.push_back(last = k);
			}
			break;
		}
		if(tab[vet[0]][vet[vet.size()-1]]) {
			rep(ii,vet.size()) rep(jj,vet.size()) {
				int d1 = 0, _ = ii; while(_ != jj) _++, _%= vet.size(), d1++;
				int d2 = 0, __ = ii; while(__ != jj) __+= vet.size()-1, __%= vet.size(), d2++;
				if(min(d1,d2) > 1 && tab[vet[ii]][vet[jj]]) {
					goto end;
				}
			}
			//pv(vet.begin(),vet.end());
			ciclos.push_back(vet);
		}
		end:;
	}
	
	//return;
	
	// colorir ^^
	memset(cor,-1,sizeof cor);
	best = -1; go(0);

	static int caso = 1;
	printf("Case #%d: %d\n",caso++,best);
	rep(i,n) {
		if(i) printf(" ");
		printf("%d",opa[i]+1);
	}
	printf("\n");
	
}

int main() {
	// solve
	int t; cin >> t;
	while(t-- && read()) {
		process();
	}
	return 0;
}
