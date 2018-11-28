#include <iostream>
#include <string>

using namespace std;
#define ll long long

string s[2000005];
ll a[2000005];
ll ans;
int t;
int l, r;
int n;

string get_string(int x){
	string ans = "";
	while(x){
		char c = x % 10;
		ans += c + '0';
		x = x / 10;
	}
	int n = ans.length();
	for (int i = 0; 2 * i < n; ++i)
		swap(ans[i], ans[n - i - 1]);
//cout << ans << endl;
	return ans;
}

void add(string x){
	string m = x;
	int k = x.length();
	for (int i = 0; i < k; ++i){
		string t = x.substr(1);
		t += x[0];
//cout << "t = " << t << endl;
		x = t;
		m = min(m, x);
//cout << "m = " << m << endl;
	}
//cout << "!m = " << m << endl;
	for (int i = 0; i < n; ++i)
		if (m == s[i]){
			++a[i];
			return;
		}
	s[n] = m;
	a[n] = 1;
	++n;
}

int main(){
	cin >> t;
	for (int _i = 0; _i < t; ++_i){
		cin >> l >> r;
		for (int i = 0; i < 2000000; ++i) s[i] = "";
		memset(a, 0, sizeof(a));
		ans = 0;
		for (int i = max(l, 10); i <= r; ++i)
			add(get_string(i));
		for (int i = 0; i < n; ++i)
			ans += a[i] * (a[i] - 1) / 2;
		cout << "Case #" << _i + 1 << ": "  << ans << endl;
	}
	return 0;
}