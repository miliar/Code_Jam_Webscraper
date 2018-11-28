#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <complex>
#include <iostream>
#include <cmath>
#include <utility>
#include <ctype.h>
#include <cstring>
#include <string>
#include <cassert>
#include <queue>
#include <map>
#include <set>
#include <complex>
using namespace std;

#define REP(_i, _N) for(_i=0;_i<_N;_i++)
#define REC(_i, _N) for(_i=1;_i<=_N;_i++)
#define PF printf
#define SF scanf
#define LIMPIA(_a) memset((_a), 0, sizeof(_a))
#define ANULA(_a) memset((_a), -1, sizeof(_a))

typedef long long ll;
const double EPS=1e-9;
const int INF=1000000000;

int T, N;

int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int i, k, h;
	SF("%d", &T);
	int caso;
	REC(caso, T){
		SF("%d", &N);
		int m=INF;
		int z1=0;
		int z2=0;
		REP(i, N){
			SF("%d", &k);
			z1+=k;
			z2^=k;
			m=min(m, k);
		}
		PF("Case #%d: ", caso);
		if(z2!=0){
			PF("NO\n");
		}else{
			PF("%d\n", z1-m);
		}
	}
	return 0;
}
