#include <iostream>
#include <algorithm>
#include <vector> 
using namespace std;

#define sz(a) int((a).size())
#define rep(i, s, f) for((i) = (s); (i) < (f); ++(i)) 
#define beg(a) (a).begin()
#define end(a) (a).end()

int main()
{
	int tests, t_num;
	cin >> tests;
	rep(t_num, 1, tests + 1)
	{
		int n, i;
		cin >> n;
		vector <int> a(n);
		rep(i, 0, n)
			cin >> a[i];
		int xor_all = a[0];
		rep(i, 1, n)
			xor_all ^= a[i];
		cout << "Case #" << t_num << ": ";
		if (xor_all)
			cout  << "NO" << endl;
		else 
		{
			sort(beg(a), end(a));
			int sum = 0;
			rep(i, 1, n)
				sum += a[i];
			cout << sum << endl;
		}
	}
	return 0;
}
