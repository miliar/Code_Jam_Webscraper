#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iostream>
#include <sstream>
#include <memory>
#include <complex>
using namespace std;

static const double EPS = 1e-5;
typedef long long ll;

#define FOR(i,a,b)	for(int i=(a);i<(int)(b);++i)
#define REP(i,b)	FOR(i,0,b)
#define ALL(c)		(c).begin(),(c).end()
#define LET(v,x)	typeof(x) v = x
#define FOREACH(it,c)	for(LET(it,(c).begin());it!=(c).end();++it)

#define BTN_B	0
#define BTN_O	1
#define BTN_N	2
#define BTN(x)	((x)=='O')
#define REV(b)	(1-(b))

int arr[102];
char flg[102];

int main(){
	int T;
	scanf("%d ", &T);
	REP(i, T){
		int N;
		scanf("%d ", &N);
		REP(j, N){
			scanf("%c %d ", flg + j, arr + j);
		}
		arr[N+0] = 0;
		arr[N+1] = 0;
		flg[N+0] = 'B';
		flg[N+1] = 'O';
		int t = 0;
		int ptr[2] = {0, 0};
		int pos[2] = {1, 1};
		REP(b, 2){
			while(BTN(flg[ptr[b]]) != b) ptr[b]++;
		}
		REP(p, N){
			int btn = BTN(flg[p]);
			int rev = REV(btn);
			int delta = std::abs(arr[p] - pos[btn]) + 1;
			pos[btn] = arr[p];
			while(btn != BTN(flg[++ptr[btn]])){}
			pos[rev] += std::max(std::min(arr[ptr[rev]] - pos[rev], delta), -delta);
			t += delta;
		}
		printf("Case #%d: %d\n", i + 1, t);
	}
	return 0;
}
