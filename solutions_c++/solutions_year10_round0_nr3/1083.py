#include <iostream>
#include <cstdio>
#include <list>
using namespace std;
int main(){
	int cases;
	scanf("%d", &cases);
	for (int t = 0; t < cases; ++t){
		int r, k, n;
		scanf("%d%d%d", &r, &k, &n);
		list<int> data;
		for (int i = 0; i < n; ++i){
			int x;
			scanf("%d", &x);
			data.push_back(x);
		}
		int ans = 0;
		for (int i = 0; i < r; ++i){
			int rest = k;
			int tot = 0;
			while (rest >= data.front() &&  tot < n){
				int x = data.front();
				data.pop_front();
				data.push_back(x);
				rest -= x;
				ans += x;
				++tot;
			}
		}
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}