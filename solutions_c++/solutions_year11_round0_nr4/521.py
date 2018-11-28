#include <iostream>
using namespace std;
int main(){
	int cases;
	cin >> cases;
	for (int tt = 0; tt < cases; ++tt){
		int n;
		cin >> n;
		int ans = 0;
		for (int i = 0; i < n; ++i){
			int x;
			cin >> x;
			if (x != i + 1) ++ans;
		}
		printf("Case #%d: %d.000000\n", tt + 1, ans);
	}
	return 0;
}