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

struct s{
	double d, v;
};

inline bool cmp(const s &a, const s &b){
	return a.v > b.v;
}

int a, b, c;
int X, N, K;
double S, T, W, R;
vector<s> V;
s w;

int main(){
	int Z;
	scanf("%d", &Z);
	FWD(z,1,Z+1){
		scanf("%d %lf %lf %lf %d", &X, &S, &R, &T, &N);
		W = 0;
		V.clear();
		R -= S;
		w.d = 0;
		w.v = S;
		K = 0;
		FWD(i,0,N){
			V.push_back(w);
			scanf("%d %d %d", &a, &b, &c);
			w.d += a-K;
			K = b;	
			V.back().d = b-a;
			V.back().v = c + S;
		}
		w.d += X-K;
		W = 0;
		if(w.d > 0) V.push_back(w);
		sort(ALL(V), cmp);
		while(!V.empty()){
			//printf("%lf %lf %lf\n", T, V.back().v, V.back().d);
			if(T * (V.back().v + R) >= V.back().d){
				W += V.back().d / (V.back().v + R);
				T -= V.back().d / (V.back().v + R);
				V.pop_back();
			}else{
				W += T;
				V.back().d -= T * (V.back().v + R);
				break;
			}
		}
		//printf("%lf\n", W);
		FE(v,V){
			W += v->d / v->v;
			//printf("%lf\n", W);
		}
		printf("Case #%d: %lf\n", z, W);
	}
	return 0;
}

