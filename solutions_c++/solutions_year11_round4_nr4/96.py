#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <cmath>
#include <limits>
#define FWD(a,b,c) for(int a=(b); a<(c); a++)
#define BCK(a,b,c) for(int a=(b); a>(c); a--)
#define FE(a,b) for(typeof(b.end()) a=b.begin(); a!=b.end(); a++)
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) erase(unique(a.begin(), a.end()), a.end())
#define LL long long
#define ULL unsigned long long
#define PII pair<int, int>
#define PDD pair<double, double>
#define x first
#define y second
#define PACKS(a) int a; scanf("%d", &a); a++; while(--a)

//#define DEBUG
#ifdef DEBUG
	#define debug printf
#else
	#define debug
#endif

using namespace std;

int n, m, a, b, r;
int D[40];
vector<int> E[40];
queue<int> Q;
vector<int> S;
int M[40][40];

bool threat(int u){
	FE(s,S){
		if(*s == u)
			return 0;
	}
	FE(s,S){
		if(M[*s][u])
			return 1;
	}
	return 0;
}

void dfs(int u){
	if(u == 1){
		b = 1;
		FWD(i,2,n){
			if(threat(i)) ++b;
		}
		r = max(r, b);
	}else{
		S.push_back(u);
		FE(v,E[u])
			if(D[*v] == D[u]+1)
				dfs(*v);
		S.pop_back();
	}
}

int main(){
	int Z;
	scanf("%d", &Z);
	FWD(z,1,Z+1){
		scanf("%d %d", &n, &m);
		FWD(i,0,n){
			FWD(j,0,n)
				M[i][j] = 0;
			D[i] = -1;
			E[i].clear();
		}
		FWD(i,0,m){
			scanf("%d,%d", &a, &b);
			E[a].push_back(b);
			E[b].push_back(a);
			M[a][b] = M[b][a] = 1;
		}
		D[0] = 0;
		Q.push(0);
		while(!Q.empty()){
			a = Q.front();
			Q.pop();
			FE(v,E[a]){
				if(D[*v] == -1){
					D[*v] = D[a] + 1;
					Q.push(*v);
				}
			}
		}
		r = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", z, D[1]-1, r);
	}
	return 0;
}

