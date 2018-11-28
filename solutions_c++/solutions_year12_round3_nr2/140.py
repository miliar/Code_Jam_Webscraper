#include <fstream>
#include <cstdio>
#include <vector>
#include <queue>
#include <utility>
using namespace std;

unsigned long long r;

void throwFirst(vector<pair<long long, int> > &a, long long n)
{
	a[0].first -= n;
	if (a[0].first == 0)
	{
		a.erase(a.begin());
	}
}

void go(vector<pair<long long, int> > &t, vector<pair<long long, int> > &b, unsigned long long n)
{
	if (!t.empty() && !b.empty())
	{
		vector<pair<long long, int> > v1(t.begin() + 1, t.end());
		vector<pair<long long, int> > v2(b.begin() + 1, b.end());

		go(v1, b, n);
		go(t, v2, n);

		if (t[0].second == b[0].second)
		{
			long long l = min(t[0].first, b[0].first);
			vector<pair<long long, int> > v1(t.begin(), t.end());
			throwFirst(v1, l);

			vector<pair<long long, int> > v2(b.begin(), b.end());
			throwFirst(v2, l);

			go(v1, v2, n + l);
		}
	}
	else
	{
		r = max(r, n);
	}
}
 
int main()
{
    ifstream cin("input.txt");
	ofstream cout("output.txt");

	int T;
	cin >> T;
	for (int tc = 0; tc < T; tc++)
	{
		int n, m;
		cin >> n >> m;

		vector<pair<long long, int> > t(m), b(n);
		for (int i = 0; i < n; i++)
		{
			cin >> b[i].first >> b[i].second;
		}

		for (int i = 0; i < m; i++)
		{
			cin >> t[i].first >> t[i].second;
		}

		r = 0;
		go(t, b, 0);

		cout << "Case #" << tc + 1 << ": " << r << endl;
	}
 
    return 0;
}
