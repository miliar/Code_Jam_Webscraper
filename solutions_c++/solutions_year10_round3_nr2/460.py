#include <algorithm>
#include <valarray>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main(){
	int Tests;
	scanf("%d ", &Tests);
	for(int Test = 1; Test <= Tests; ++Test){
		long long int l, p, c;
		scanf("%lld %lld %lld ", &l, &p, &c);
		long long int n = 0;
		for(int i = l; i * c < p; i *= c) ++n;
		int result = 0;
		for(; n; n /= 2) ++result;
		printf("Case #%d: %d\n", Test, result);
	}
}
