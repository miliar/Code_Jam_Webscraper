#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <complex>
#include <functional>
#include <bitset>
#include <string>
#include <valarray>
#include <algorithm>
using namespace std;

#define MP(a,b)     make_pair(a,b)
#define two(i)      (1<<(i))
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,s,e)  for(int i=(s); i<(e); ++i)
#define FORD(i,s,e) for(int i=(s); i>=(e); --i)
typedef long long i64;
typedef unsigned long long u64;


string name = "C-large";
bool   is_file__ = true;

const int NN = 1024;
i64  R, K; int  N;
i64  g[NN];
i64  st_sum[NN];
int  nxt_idx[NN];
int  occ_idx[NN];
i64  made[NN];
int  cnt_2_idx[NN];


i64  go() {
	scanf("%lld%lld%d", &R, &K, &N);
	for(int i=0; i<N; ++i)
		scanf("%lld", g+i);
	
	i64  sum = 0;
	REP(i, N) sum += g[i];
	if(sum <= K)
		return sum*R;

	for(int i=0; i<N; ++i) {
		int  j = (i+1)%N;
		i64  s = g[i];
		while(true) {
			if(s + g[j] > K) break;
			s += g[j];
			++j; j%=N;
		}
		st_sum[i] = s;
		nxt_idx[i] = j;
		/*printf("i=%d  nxt_idx=%d  st_sum=%lld\n",
			i, j, s);*/
	}

	memset(occ_idx, 0, sizeof(occ_idx));

	occ_idx[0] = 1;
	int  ci = 0;
	int  cnt = 1;
	int  pre_cnt = 0;
	int  loop_beg_idx = -1;
	int  loop_end_idx = -1;
	int  loop_size = 0;
	i64  loop_sum = 0;
	made[0] = 0;
	made[1] = st_sum[0];
	cnt_2_idx[0] = -1;
	cnt_2_idx[1] = 0;

	while(true) {
		int  j = nxt_idx[ci];
		++cnt;
		cnt_2_idx[cnt] = j;
		made[cnt] = made[cnt-1] + st_sum[j];
		if(occ_idx[j]) {
			pre_cnt = occ_idx[j] - 1;
			loop_size = cnt - occ_idx[j];
			loop_beg_idx = j;
			loop_end_idx = ci;
			loop_sum = made[cnt] - made[occ_idx[j]];
			break;
		}
		occ_idx[j] = cnt;
		ci = j;
	}

	if(R <= cnt)
		return made[R];

	i64  pre_ans = made[pre_cnt];
	R -= pre_cnt;
	//if(R < 0) return made[R+pre_cnt];
	i64  loop_ans = (R/loop_size)*loop_sum;
	R %= loop_size;
	i64  other_ans = 0;
	if(R > 0)
		other_ans = made[pre_cnt+R] - made[pre_cnt];
	return pre_ans + loop_ans + other_ans;
	//return 0;
}


void  solve() {
	int  T, case_idx = 1;
	scanf("%d", &T);
	for(case_idx = 1; case_idx <= T; ++case_idx) {
		printf("Case #%d: %lld\n", case_idx, 
			go());
	}
}



void set_file() {
	string in = name+".in";
	string ou = name + ".out";
	freopen(in.c_str(), "r", stdin);
	freopen(ou.c_str(), "w", stdout);
}

int  main(int argc, char* argv[])
{
	if(is_file__)
		set_file();
	solve();
	return 0;
}

