#define fr(i, a, x) for(int(i) = a; i <= x; ++i)
#define rfr(i, a, x) for(int(i) = a; i >= x; --i)

#include <fstream>
#include <vector>
#include <queue>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");

const int MAXC = 1048576;

int main()
{
	int t, n;
	char c;
	cin >> t;
	fr(re, 1, t)
	{
		cin >> n;
		vector< pair<int, int> > a(n);
		queue<int> qf, qs;
		fr(i, 0, n - 1)
		{
			cin >> c;
			cin >> a[i].second;
			if (c == 'O') 
			{
				a[i].first = 1;
				qf.push(a[i].second);
			}
			else 
			{
				a[i].first = 2;
				qs.push(a[i].second);
			}
		}
		int xf = 1, xs = 1, s = 0, ds;
		fr(i, 0, n - 1)
		{
			if (a[i].first == 1)
			{
				ds = abs(qf.front() - xf) + 1;
				s += ds;
				xf = a[i].second;
				if (!qs.empty())
				{
					if (xs > qs.front()) xs -= min( ds, xs - qs.front() );
					else xs += min( ds, qs.front() - xs );
				}
				qf.pop();
			}
			else 
			{
				ds = abs(qs.front() - xs) + 1;
				s += ds;
				xs = a[i].second;
				if (!qf.empty())
				{
					if (xf > qf.front()) xf -= min( ds, xf - qf.front() );
					else xf += min( ds, qf.front() - xf);
				}
				qs.pop();
			}
		}
		cout << "Case #" << re << ": " << s << '\n';
	}
	return 0;
}