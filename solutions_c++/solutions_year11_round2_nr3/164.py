#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

const int N = 2010;
int n;
int m;
set<int> neigh[N];
VI zb[N];
bool jest[N];
int u[N];
int v[N];

int kolory[N];
int udane[N];
bool ok;
int kt;

void obadaj(int ilosc){
	if(ok ) return ;
	bool oki = true;
	FOR(i,1,kt){
		FOR(j,1,ilosc)
			jest[j] = 0;
		FOREACH(p,zb[i])
			jest[kolory[*p]] = true;
		FOR(j,1,ilosc)
			if(!jest[j]){
				oki = false;
				return ;
			}
	}
	if(oki){
		ok = true;
		FOR(i,1,n)
			udane[i] = kolory[i];
	}
}

void tryColor(int ilosc, int ktory){
	if(ok) return;
	if(ktory == n+1){
		obadaj(ilosc);
		return ;
	}
	FOR(i,1,ilosc){
		kolory[ktory] = i;
		tryColor(ilosc,ktory+1);
	}
}

main(){
	int t,a,b;
	scanf("%d",&t);
	REP(q,t){
		scanf("%d %d",&n,&m);
		REP(i,m){
			scanf("%d",&u[i]);
		}
		REP(i,m){
			scanf("%d",&v[i]);
		}
		REP(i,m)
			neigh[v[i]].insert(u[i]);
		stack<int>S;
		kt = 0;
		for(int i=1;i<=n;i++){
			S.push(i);
			while(!neigh[i].empty()){
				int edge = *neigh[i].rbegin();
				neigh[i].erase(neigh[i].find(edge));
				kt++;
				while(S.top() != edge){
					int pom = S.top(); S.pop();
					zb[kt].PB(pom);
				}
				zb[kt].PB(edge);
				S.push(i);
			}
		}
		kt++;
		while(!S.empty()){
			zb[kt].PB(S.top()); S.pop();
		}
		int wyn;
		for(int i=n-1;i>=1;i--){
			ok = false;
			tryColor(i,1);
			if(ok){
				wyn = i;
				break;
			}
		}
		printf("Case #%d: %d\n",q+1,wyn);
		FOR(i,1,n)
			printf("%d ",udane[i]);
		printf("\n");
		FOR(i,1,kt)
			zb[i].clear();
		FOR(i,1,n)
			neigh[i].clear();
	}
	return 0;
}
