#include <iostream>
#include <algorithm>
using namespace std;
struct Wire
{
	int a, b;
	bool operator<(Wire s)
	{
		return a < s.a;
	}
};
Wire w[1010];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t, n;
	cin >> t;
	for (int k = 1; k <= t; k++)
	{
		int count = 0;
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> w[i].a >> w[i].b;
		sort(w, w + n);
		for (int i = 0; i < n - 1; i++)
			for (int j = i + 1; j < n; j++)
				if (w[i].b > w[j].b)
					count++;
		cout << "Case #" << k << ": " << count << endl;
	}
	return 0;
}