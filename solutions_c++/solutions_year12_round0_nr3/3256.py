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

int count_numbers(int value) {
	int k = 10, i;
	for (i=0; value / k; ++i, k *= 10);
	return i + 1;
}

int process(){
	int a, b, count = 0, length, pow = 1;
	scanf("%d %d", &a, &b);
	length = count_numbers(a);
	for (int i = 1; i < length; ++i, pow *= 10);
	for (int n = a; n < b; ++n) {
		int k = 10, l = 0;
		for (int j = 1; j < length; ++j){
			int rem = n % k;
			if (rem >= k / 10){
				int m = 10 * rem * pow / k + n / k;
				if ((m > n) && (m <= b)) {
					++count;
					//printf("\n(%d, %d)", n, m);
					++l;
				}

			}									
			k *= 10;
		}
		//if (l) printf(" %d", l);
	}
	return count;
}

int main(void){
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		printf("Case #%d: %d\n", tc, process());
	}	
}