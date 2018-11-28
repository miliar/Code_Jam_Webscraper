#include <iostream>
#include <vector>

#define maxN (26 + 1)

using namespace std;

char c[maxN][maxN];
vector <int> d[maxN];

void solve ()
{
	for (int i = 0; i < maxN; i++)
		d[i].resize (0);
	for (int i = 0; i < maxN; i++)
		for (int j = 0; j < maxN; j++)
			c[i][j] = 0;

	string res = "";

	int c; cin >> c;
	for (int i = 0; i < c; i++)
	{
		string x; cin >> x;
		::c[x[0] - 'A'][x[1] - 'A'] = x[2];
		::c[x[1] - 'A'][x[0] - 'A'] = x[2];
	}
	int d; cin >> d;
	for (int i = 0; i < d; i++)
	{
		string x; cin >> x;
		::d[x[0] - 'A'].push_back (x[1]);
		::d[x[1] - 'A'].push_back (x[0]);
	}
	int n; cin >> n;
	string x; cin >> x;
	for (int i = 0; i < x.size(); i++)
	{
		if (!res.size())
			res += x[i];
		else if (::c[x[i] - 'A'][res[res.size() - 1] - 'A'])
			res[res.size() - 1] = ::c[x[i] - 'A'][res[res.size() - 1] - 'A'];
		else
		{
			int find = 0;
			for (int j = 0; j < ::d[x[i] - 'A'].size(); j++)
				for (int k = 0; k < res.size(); k++)
					if (::d[x[i] - 'A'][j] == res[k])
						find = 1;
			if (find)
				res = "";
			else
				res += x[i];
		}
	}
	cout << "[";
	for (int i = 0; i < res.size(); i++)
		cout << ((i == res.size() - 1) ? string (1, res[i]) : string (1, res[i]) + ", ");
	cout << "]" << endl;
}

int main ()
{
	int t; cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		solve ();
	}
}
