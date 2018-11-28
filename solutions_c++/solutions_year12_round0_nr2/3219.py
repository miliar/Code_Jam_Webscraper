#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)



int process(){
	int n, s, p, max_g = 0;
	scanf("%d %d %d", &n, &s, &p);
	for(int i = 0; i < n; ++i) {
		int points, max_result;
		scanf("%d", &points);
		max_result = points / 3 + (points % 3?1:0);
		if (max_result >= p) ++max_g;
		else if (s && points > 1 && points % 3 != 1 && max_result + 1 >= p) {
			--s;
			++max_g;
		}		
	}
	return max_g;
}

int main(void){
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		printf("Case #%d: %d\n", tc, process());
	}	
}