#include <cstdio>
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int parse(string s)
{
	int h, m;
	sscanf(s.c_str(), "%d:%d", &h, &m);
	return h * 60 + m;
}
typedef pair<int, int> PII;
typedef vector<PII> VPII;
int solve(VPII &v)
{
	int n = v.size();
	int ret = 0;
	for (int i=0, sum=0; i<n; i++)
	{
		sum += v[i].second;
		ret = max(ret, sum);
	}
	return ret;
}
int main()
{
	int n;
	cin >> n;
	for (int tc=0; tc<n; tc++)
	{
		int t;
		cin >> t;
		int na, nb;
		cin >> na >> nb;
		VPII a, b;
		for (int i=0; i<na; i++)
		{
			string start, end;
			cin >> start >> end;
			a.push_back(PII(parse(start), 1));
			b.push_back(PII(parse(end) + t, -1));
		}
		for (int i=0; i<nb; i++)
		{
			string start, end;
			cin >> start >> end;
			b.push_back(PII(parse(start), 1));
			a.push_back(PII(parse(end) + t, -1));
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		printf("Case #%d: %d %d\n", tc+1, solve(a), solve(b));
	}
	return 0;
}
