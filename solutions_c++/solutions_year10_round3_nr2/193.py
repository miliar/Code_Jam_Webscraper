#include <iostream>
#include <cstdio>
using namespace std;
int main(){
	int cases;
	scanf("%d", &cases);
	for (int tt = 0; tt < cases; ++tt){
		long long l, r, c;
		cin >> l >> r >> c;
		int ans = 0;
		while (l * c < r){
			c *= c;
			++ans;
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}
	return 0;
}