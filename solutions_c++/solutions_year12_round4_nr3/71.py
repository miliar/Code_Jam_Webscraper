#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#define pb push_back
#define mp make_pair
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
using namespace std;

int tst, _, n, a[2222], lst, h[2222];

bool construct(int l, int r, int k, int st){
	h[l] = k * l + st;
	h[r] = k * r + st;
	st = st + k * r - (k + 10) * r;
	k = k + 10;
	for (int i = l + 1; i < r;){
		if (a[i] > r)
			return 0;
		if (!construct(i, a[i], k, st))
			return 0;
		i = a[i];
	}
	return 1;
}

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tst);
	while (tst--){
		scanf("%d", &n);
		for (int i = 1; i < n; i++)
			scanf("%d", &a[i]);
		bool flag = 1;
		for (int i = 1; i < n;){
			if (!construct(i, a[i], 0, INF / 2)){
				flag = 0;
				break;
			}
			i = a[i];
		}
		if (!flag)
			printf("Case #%d: Impossible\n", ++_);
		else{
			printf("Case #%d:", ++_);
			for (int i = 1; i <= n; i++)
				printf(" %d", h[i]);
			printf("\n");
		}
	}
}
