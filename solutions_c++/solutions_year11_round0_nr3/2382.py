#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("answer.txt", "w", stdout);
	int tc;
	cin>>tc;
	for(int Case = 0; Case < tc; Case++)
	{
		int n;
		cin >> n;
		vector<int> c(n);
		int sum = 0, xor = 0, min = 10000000;
		for(int i = 0; i < n; ++i)
		{
			cin >> c[i];
			xor ^= c[i];
			sum += c[i];
			if(min > c[i])
				min = c[i];
		}
		cout << "Case #" << Case + 1 <<": ";
		if(xor != 0)
			cout << "NO" << endl;
		else
		{
			cout << sum - min << endl;
		}
	}

	return 0;
}
