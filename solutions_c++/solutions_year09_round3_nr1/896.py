#include<iostream>
#include<string>
using namespace std;

int main()
{
	int tc, i, j;
	int base, nowbase;
	int a[300];
	int v[300];
	long long ans, tmp;
	string str;
	cin>>tc;
	getline(cin, str);
	for (i = 1; i <= tc; i++)
	{
		memset(a, -1, sizeof(a));
		memset(v, 0, sizeof(v));
		getline(cin, str);
		base = 0;
		ans = 0;
		for (j = 0; j < str.size(); j++)
			if (v[str[j]] == 0) {
				v[str[j]] = 1;
				base++;
			}
		if (base == 1) base = 2;
		tmp = 1;
		for (j = 1; j < str.size(); j++)
			tmp *= base;
		nowbase = 1;
		for (j = 0; j < str.size(); j++) {
			if (v[str[j]] == 1) {
				v[str[j]] = 2;
				a[str[j]] = nowbase;
				if (nowbase == 1) nowbase = 0;
				else
					if (nowbase == 0) nowbase = 2;
					else nowbase++;
			}
			ans += tmp * a[str[j]];
			tmp /= base;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}