#include<iostream>

using namespace std;

int n,k;

int main()
{
	int t;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin >> t;
	int tt = 0;
	while (t > 0)
	{
		tt++;
		t--;
		cin >> n >> k;
		long long s = 1;
		for (int i = 0; i < n; i++) s = s * 2;
		long long ss = s / 2;
		k = k % s;
		int ans = 0;
		if (k < s - 1) ans = 0; else ans = 1;
		cout << "Case #" << tt << ": ";
		if (ans == 0) cout << "OFF\n"; else cout <<"ON\n";
	}	
}
