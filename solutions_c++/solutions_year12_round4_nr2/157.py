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
		printf("Case #%d:", testCounter + 1);
		int n, w, l;
		cin >> n >> w >> l;
		vector<double> dists(n);
		vector<pair<int, int> > v(n);
		for (int i = 0; i < n; i++)
		{
			cin >> v[i].first;
			v[i].second = i;
			dists[i] = v[i].first;
		}
		sort(v.rbegin(), v.rend());
		vector<pair<double, double> > solution(n);
		solution[v[0].second] = make_pair(0, 0);
		double curX = v[0].first;
		double curY = 0;
		double nextY = v[0].first;
		for (int i = 1; i < n; i++)
		{
			if(curX + v[i].first - epsilon > w)
			{
				curY = nextY + v[i].first;
				nextY = nextY + 2 * v[i].first;
				curX = -v[i].first;
			}
			solution[v[i].second] = make_pair(curX + v[i].first, curY);
			/*if (solution[v[i].second].second - epsilon > l)
			{
				cout << "Using " << solution[v[i].second].second  << " when only " << l << " is allowed" << endl;
			}*/
			curX += 2 * v[i].first;
		}
		/*for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (i == j)
					continue;
				if ((solution[i].first - solution[j].first) * (solution[i].first - solution[j].first) + 
					(solution[i].second - solution[j].second) * (solution[i].second - solution[j].second) <
					dists[i] * dists[i] + dists[j] * dists[j])
				{
					cout << "Circles " << i << " " << j << " intersect" << endl;
				}
			}
		}*/
		for (int i = 0; i < n; i++)
		{
			printf(" %.6lf %.6lf", solution[i].first, solution[i].second);
		}
		cout << endl;

	}
	return 0;
}
