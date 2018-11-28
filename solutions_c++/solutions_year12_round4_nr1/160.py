#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int n;
		cin >> n;
		vector<pair<int, int> > vines(n);
		int d;
		for (int i = 0; i < n; i++)
		{
			cin >> vines[i].first >> vines[i].second;
		}
		cin >> d;
		sort(vines.begin(), vines.end());
		vector<int> maxes(n, 0);
		maxes[0] = vines[0].first;
		for (int i = 0; i < n; i++)
		{
			for (int j = i + 1; j < n; j++)
			{
				if (vines[j].first - maxes[i] <= vines[i].first)
				{
					maxes[j] = max(maxes[j], min(vines[j].first - vines[i].first, vines[j].second));
				}
			}
		}
		bool b = false;
		for (int i = 0; i < n; i++)
		{
			if (vines[i].first + maxes[i] >= d)
				b = true;
		}
		if (b)
		{
			cout << "YES" << endl;
		}
		else
		{
			cout << "NO" << endl;
		}
	}
	return 0;
}
