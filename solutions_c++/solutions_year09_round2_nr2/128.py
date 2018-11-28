#include<iostream>
#include<vector>
using namespace std;

vector<int> a;

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cout << "Case #" << t << ": ";
		string z;
		cin >> z;
		a.clear();
		for (int i = 0; i < z.size(); i++) a.push_back(z[i] - '0');
		if (next_permutation(a.begin(), a.end()))
		{
			for (int i = 0; i < a.size(); i++) cout << a[i];
			cout << endl;
		}
		else
		{
			for (int i = 0; i < a.size(); i++)
				if (a[i] != 0)
					swap(a[i], a[0]);
			for (int i = 0; i < a.size(); i++)
				if (a[i] != 0 && a[i] < a[0])
					swap(a[i], a[0]);
			cout << a[0];
			a[0] = 0;
			sort(a.begin(), a.end());
			for (int i = 0; i < a.size(); i++) cout << a[i];
			cout << endl;
		}
	}
}