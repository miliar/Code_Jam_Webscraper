#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");

int main()
{
	int counttest;
	cin >> counttest;
	for(int test = 1; test <= counttest; ++test)
	{
		int n, k = 0;
		cin >> n;
		vector<int> a(n), b(n);
		for(int i = 0; i < n; ++i)
		{
			cin >> a[i];
			b[i] = a[i];
		}
		sort(a.begin(), a.end());
		for(int i = 0; i < n; ++i)
			if (a[i] != b[i]) ++k;
		cout << "Case #" << test << ": " << k << ".000000\n";
	}
	return 0;
}