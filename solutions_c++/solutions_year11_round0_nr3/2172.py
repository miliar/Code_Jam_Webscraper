#include <iostream>
#include <vector>

using namespace std;


void solve(){	
	int n;
	cin >> n;
	int sum = 0, minx = 10000000, xor = 0, x;
	for (int i = 0; i < n; ++i){
		cin >> x;
		sum += x;
		if (x < minx) minx = x;
		xor ^= x;
	}	
	if (xor != 0){
		printf("NO\n");
	}else {
		printf("%d\n", sum - minx);
	}
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <=T; ++t){
		printf("Case #%d: ", t);
		solve();
	}
	return 0; 
}