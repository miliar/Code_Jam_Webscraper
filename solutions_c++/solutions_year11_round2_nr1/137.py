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
		printf("Case #%d:\n", testCounter + 1);
		int n;
		cin >> n;
		vector<string> v(n);
		for(int i = 0; i < n; i++) 
			cin >> v[i];
		vector<int> wins(n, 0);
		vector<double> wp(n, 0);
		vector<double> oowp(n, 0);
		vector<double> owp(n, 0);
		vector<double> coef(n, 0);

		vector<int> played(n, 0);
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				if(v[i][j] == '.')
					continue;
				if(v[i][j] == '1')
				{
					played[i]++;
					wins[i]++;
				}
				else
				{
					played[i]++;
				}
			}
			wp[i] = (double)wins[i] / (double)played[i];
		}

		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				if(v[i][j] == '.')
					continue;
				if(v[i][j] == '1')
				{
					owp[i] += (double)wins[j] / (double)(played[j] - 1);
				}
				else
				{
					owp[i] += (double)(wins[j] - 1) / (double)(played[j] - 1);
				}
			}
			owp[i] /= (double)played[i];
		}

		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				if(v[i][j] == '.')
					continue;
				oowp[i] += owp[j];
			}
			oowp[i] /= (double)played[i];
		}

		for(int i = 0; i < n; i++)
		{
			coef[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
			printf("%.9lf\n", coef[i]);
		}

	}
	return 0;
}
