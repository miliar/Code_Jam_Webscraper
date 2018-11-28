#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

const int size = 1000;
int main()
{
	int T, R, K, N, st, sum, cur, last;
	int grp[size];

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	scanf("%d", &T);
	for(int j = 1; j <= T; j++){
		scanf("%d%d%d", &R, &K, &N);
		for(int k = 0; k < N; k++)
			scanf("%d", &grp[k]);
		st = 0;
		sum = 0;
		for(int k = 0; k < R; k++){
			last = st;
			cur = 0;
			while(cur + grp[st] <= K){
				cur += grp[st];
				st = (st + 1) % N;
				if(st == last)break;
			}
			sum += cur;
		}
		printf("Case #%d: %d\n", j, sum);
	}
	return 0;
}
