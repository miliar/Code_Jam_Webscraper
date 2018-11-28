#include <iostream>
#include <cstdio>
#include <map>
#include <cassert>
#include <algorithm>
#include <vector>

using namespace std;

inline int min(int a, int b, int c){
	return min(a, min(b, c));
}
inline int max(int a, int b, int c){
	return max(a, max(b, c));
}
bool norm(int k, int p, int Limit){
	for (int i = 0; i <= 10; ++ i)
		for (int j = 0; j <= 10; ++ j)
			for (int l = 0; l <= 10; ++ l)
				if (i + j + l == k && max(i, j, l) - min(i, j, l) <= Limit && max(i, j, l) >= p)
					return 1;
	return 0;
}
int main(){
	int T;
	scanf("%d\n", &T);
	for (int testcase = 0; testcase < T; ++ testcase){
		int n, s, p;
		int ans = 0;
		scanf("%d%d%d", &n, &s, &p);
		vector<int> a(n);
		vector<bool> done(n, 0);
		for (int i = 0; i < n; ++ i)
			scanf("%d", &a[i]);
		for (int i = 0; i < n && s > 0; ++ i)
			if (!done[i] && norm(a[i], p, 1) == false && norm(a[i], p, 2) == true){
				done[i] = 1;
				--s;
				++ans;
			}
		for (int i = 0; i < n && s > 0; ++ i)
			if (!done[i] && norm(a[i], p, 2) == true){
				done[i] = 1;
				--s;
				++ans;
			}
		for (int i = 0; i < n; ++ i)
			if (!done[i] && norm(a[i], p, 1) == true){
				done[i] = 1;
				++ans;
			}
		printf("Case #%d: %d\n", testcase + 1, ans);
	}
	return 0;
}