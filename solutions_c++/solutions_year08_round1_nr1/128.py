#include <iostream>
#include <algorithm>
using namespace std;
const int MAXN = 1000;
int a[MAXN], b[MAXN];
int main(){
	int cases;
	cin >> cases;
	for (int t = 0; t != cases; ++t){
		int n;
		cin >> n;
		for (int i = 0; i != n; ++i)  cin >> a[i];
		for (int i = 0; i != n; ++i)  cin >> b[i];
		sort(a, a + n);
		sort(b, b + n, greater<int>());
		long long ans = 0;
		for (int i = 0; i != n; ++i)  ans += a[i] * b[i];
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
	system("pause");
}