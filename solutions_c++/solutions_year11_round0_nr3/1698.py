#include<iostream>
using namespace std;
int main() {
	int t;
	
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	cin >> t;
	for(int cas = 1; cas <= t;cas ++) {
		int n;
		cin >> n;
		int ans = 0;
		int min = 1000000000;
		int sum =0;
		for(int i =0; i < n; i ++) {
			int x;
			cin >>x;
			ans ^= x;
			sum += x;
			if (min > x) min = x;
		}
		cout << "Case #"<<cas<<": ";
		if (ans) {
			cout << "NO" << endl;
		}
		else  {
			cout << sum-min << endl;
		}
		
	}
	return 0;
}
