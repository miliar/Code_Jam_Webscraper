#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> PII;
typedef unsigned long long ULL;


void solution(int tstNum){
	int n, k, b, t;
	scanf("%d%d%d%d", &n, &k, &b, &t);
	PII p[50];
	for (int i = 0; i < n; i++){
		scanf("%d", &p[i].first);
	}
	for (int i = 0; i < n; i++){
		scanf("%d", &p[i].second);
	}
	sort(p, p + n);
	bool can[50] = {0};
	for (int i = 0; i < n; i++){
		if (p[i].second * t >= b - p[i].first){
			can[i] = true;
		}
	}
	int res = 0;
	int cnt = 0;
	for (int i = n - 1; i >= 0; i--){
		if (!can[i]){
			continue;
		}
		++cnt;
		for (int j = i + 1; j < n; j++){
			res += !can[j];
		}
		if (cnt == k){
			break;
		}
	}
	if (cnt != k){
		printf("Case #%d: IMPOSSIBLE\n", tstNum + 1);
	}else{
		printf("Case #%d: %d\n", tstNum + 1, res);
	}
}

int main(){

	//freopen("A-small.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	//freopen("A-large.in", "rt", stdin);
	//freopen("A-large.out", "wt", stdout);

	//freopen("B-small.in", "rt", stdin);
	//freopen("B-small.out", "wt", stdout);

	freopen("B-large.in", "rt", stdin);
	freopen("B-large.out", "wt", stdout);


	//freopen("C-small.in", "rt", stdin);
	//freopen("C-small.out", "wt", stdout);

	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);

	int t = 0;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		solution(tt);
	}

	return 0;
}