#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t, n, k;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string s;
		cin >> n >> k;
		if (k % (1 << n) == (1 << n) - 1)
			s = "ON";
		else
			s = "OFF";
		cout << "Case #" << i << ": " << s << endl;
	}
}
