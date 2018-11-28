#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector <int> a;
vector <int> b;

int main()
{
	int t;
	scanf("%d", &t);
	for (int uu = 0; uu < t; uu++)
	{
		int n;
		scanf("%d", &n);
		a.clear();
		b.clear();
		for (int i = 0; i < n; i++)
		{
			int x;
			scanf("%d", &x);
			a.push_back(x);
		}
		for (int i = 0; i < n; i++)
		{
			int x;
			scanf("%d", &x);
			b.push_back(x);
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		long long rez = 0;
		for (int i = 0; i < n; i++)
			rez += (a[i] * b[n - i - 1]);
		cout << "Case #" << uu + 1 << ": " << rez << endl;
	}
	return 0;
}
