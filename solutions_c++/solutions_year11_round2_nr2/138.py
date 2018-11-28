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
#define epsilon 1e-10
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;
double dp[1 << 20];
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
		long double d;
		cin >> n >> d;
		vector<long double> v;
		int x, y;
		for(int i = 0; i < n; i++)
		{
			cin >> x >> y;
			for(int j = 0; j < y; j++)
				v.push_back((long double)x);
		}
		sort(v.begin(), v.end());
		long double step = 1e13;
		long double cur = 0.0;
		bool does;
		while(step > 1e-9)
		{
			cur += step;
			dp[0] = v[0] - cur;
			does = true;
			for(int i = 1; i < v.size(); i++)
			{
				if(dp[i - 1] + d - epsilon > v[i] + cur)
				{
					does = false;
					break;
				}
				dp[i] = max(dp[i - 1] + d, v[i] - cur);
			}
			if(does)
				cur -= step;
			step /= 2.0;
		}
		printf("%.9Lf\n", cur);
	}
	return 0;
}
