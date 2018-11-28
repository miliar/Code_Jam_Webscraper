#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
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

const int N = 1000010;
double pos[N];
double n_pos[N];
int n,c;
int ind;

bool ok(double czas){
	//printf("ogr : %.3lf\n",czas);
	n_pos[0] = pos[0] - czas;
	//printf("--------pierwszy na poz : %.3lf\n",n_pos[0]);
	for(int i=1;i<ind;i++){
		//printf("   cnt dla : %d\n",i);
		double gdzie = n_pos[i-1] + c; // tu najwczesniej moze sie znajdowac
		double najp = pos[i] + czas; // ru najpozniej moze sie znajdowac
		double najwczesniej = pos[i] - czas;
		//printf(" --- gdzie : %.3lf, najp : %.3lf, najwczesniej : %.3lf\n",gdzie,najp,najwczesniej);
		if(najp <= gdzie) return false;
		n_pos[i] = max(gdzie,najwczesniej);
		//printf(" ------%d na poz: %.3lf\n",i,n_pos[i]);
	}
	return true;
}

main(){
	int t;
	scanf("%d",&t);
	REP(q,t){
		scanf("%d %d",&n,&c);
		ind = 0;
		REP(i,n){
			int p,v;
			scanf("%d %d",&p,&v);
			while(v--)
				pos[ind++] = p;
		}
		double kon = ind*c*5;
		double pocz = 0.0;
		while(kon - pocz >= 1e-8){
			double sr = (pocz + kon) / 2;
			if(ok(sr)) kon = sr;
			else pocz = sr;
		}
		printf("Case #%d: %.10lf\n",q+1,pocz);
	}
}
