#include <fstream>
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
		int n;
		cin >> n;
		vector<int> a(n);
		long long s = 0, sx = 0, mn = 1e18;
		for(int i = 0; i < n; ++i)
		{
			cin >> a[i];
			sx ^= a[i];
			s += a[i];
			if (a[i] < mn) mn = a[i];
		}
		if (sx) 
		{
			cout << "Case #" << test << ": NO\n";
			continue;
		}
		else 
		{
			cout << "Case #" << test << ": " << s - mn << '\n';
			continue;
		}
	}
	return 0;
}