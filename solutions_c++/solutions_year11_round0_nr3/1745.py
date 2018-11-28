#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <bitset>
using namespace std;

typedef pair<int, int> pii;

const bool DEBAG_OUTPUT = false;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;

	for (int t = 0; t < T; ++ t)
	{
		int n;
		cin >> n;
		int Min = 10000000;
		int Sum = 0;
		int RealSum = 0;
		for (int i = 0; i < n; ++ i)
		{
			int k;
			cin >> k;
			Sum ^= k;
			RealSum += k;
			Min = min(Min, k);
		}
		
		cout << "Case #" << t + 1 << ": ";

		if (Sum != 0)
		{
			cout << "NO\n";
		}
		else
		{
			cout << RealSum - Min << '\n';
		}
	}	
	return 0;
}
