#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

#pragma warning(disable:4996)

typedef long long int64;
typedef int64 ll;


////////////////////////////////////////start///////////////////////////////////////////

int K;
char seq[1010];
char seq2[1010];
int order[8];

void solve(int id) {
	for(int i=0; i<K; ++i) order[i] = i;
	int opt = -1;
	//memset(seq2, 0, sizeof seq2);
	int len = strlen(seq);
	do {
		int cnt = len / K;
		int already = 0;
		for (int i=0; i<cnt; ++i) {
			for (int k=0; k<K; ++k) {
				seq2[k+already] = seq[order[k]+already];
			}
			already += K;
		}
		int total = 1;
		for (int i=1; i<len; ++i) {
			if (seq2[i] != seq2[i-1])
				++total;
		}
		if (opt == -1 || opt > total) {
			opt = total;
			//printf("%s %d", seq2, total);
		}

	}while(std::next_permutation(order, order+K) );

	printf("Case #%d: %d\n", id, opt);


	
}

int main() {
	freopen("d:/input.in", "r", stdin);
	freopen("d:/output.out", "w", stdout);
	
	int C;
	scanf("%d", &C);
	for (int id=1; id<=C; ++id) {
		scanf("%d", &K);
		scanf("%s", &seq);
		solve(id);
	}
	return 0;
}