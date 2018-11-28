#include <cstdio>
#include <deque>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <map>

using namespace std;

int T;

struct path {
	int s, e,w;
} inp[10024];

bool cmp(const path &a, const path &b){
	return a.s < b.s;
}
bool cmp_w(const path &a, const path &b){
	return a.w < b.w;
}

void solve(){
	int X, S, R, t, N;
	scanf(" %d %d %d %d %d", &X, &S, &R, &t, &N);
	double tim = t;
	
	for (int i=0;i<N;++i){
		scanf(" %d %d %d", &inp[i].s, &inp[i].e, &inp[i].w);
	}
	sort(inp, inp+N, cmp);
	int pre = 0;
	int M = N;
	for (int i=0;i<M;++i){
		if (inp[i].s != pre){
			inp[N++] = (path){pre, inp[i].s, 0};
		}
		pre = inp[i].e;
	}
	if (pre != X){
		inp[N++] = (path){pre, X, 0};
	}
	
	sort(inp, inp+N, cmp_w);
	double tr = 0.0f;
	for (int i=0;i<N;++i){
		int len = inp[i].e - inp[i].s;
//		printf("%d %d %llf\n", inp[i].s, inp[i].e,tim);
		if (tim>0){
			if (tim * (R + inp[i].w) > len){
				double timeused = (double)len / (double)(R + inp[i].w);
				tim -= timeused;
				tr += timeused;
			}else{
				tr += tim;
				tr += (double)(len - tim * (R + inp[i].w)) / (double)(S + inp[i].w);
				tim = 0.0f;
			}
		}else{
			tr += (double)(len) / (double)(S + inp[i].w);
		}
	}
	printf("%.8llf\n",tr);
}

int main(){
	scanf("%d", &T);
	for (int tc=1;tc<=T;++tc){
		printf("Case #%d: ", tc);
		solve();
	}

	return 0;
}

