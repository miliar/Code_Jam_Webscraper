#include <iostream>
using namespace std;

int main(){
	int T, no, n, ans;
	cin >> T;
	for (int C = 1; C <= T; C++){
		ans = 0;
		cin >> n;
		for (int i = 1; i <= n; i++){
			cin >> no;
			if (no != i)
				ans++;
		}
		printf("Case #%d: %d.000000\n", C, ans);
	}
	return 0;
}
