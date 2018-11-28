#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <sstream>
using namespace std;

typedef long long int64;

int main()
{
	int t;
	
	scanf("%d", &t);
	
	for(int time = 1; time <= t; ++time) {
	
		int n;
		int l[1000];
		int p[1000];
		
		scanf("%d", &n);
		for(int i = 0; i < n; ++i)
			scanf("%d", l + i);
		for(int i = 0; i < n; ++i)
			scanf("%d", p + i);
		
		pair<pair<int, int>, int > order[1000];
		
		for(int i = 0; i < n; ++i) {
		
			order[i].first.first = -p[i];
			order[i].first.second = l[i] * p[i];
			order[i].second = i;
		}
		
		sort(order, order + n);
		
		printf("Case #%d: ", time);
		for(int i = 0; i < n; ++i)
			printf("%d%s", order[i].second, i == n - 1 ? "\n" : " ");
	}
	
	return 0;
}