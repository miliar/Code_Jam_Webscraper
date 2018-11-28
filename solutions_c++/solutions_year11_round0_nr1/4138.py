#include <vector>
#include <memory.h>
#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

vector<int> a;
vector<char> z;
//vector<int> p;
map<char, int> p;
map<char, vector<int> > b;
map<char, int> l;

void solve(int TCase)
{
	int n = a.size();
	b.clear();
	p.clear();
	l.clear();
	
	for (int i = 0; i < n; ++i)
	{
		if (b[z[i]].size() == 0)
			p[z[i]] = 0, l[z[i]] = 0;
		b[z[i]].push_back(a[i]); 
	}
	
	
	int i = 0, T = 0;
	while (i != n)
	{
		bool u[1005];
		memset(u, 0, sizeof(u));
		if (p[z[i]] == a[i])
		{
			l[z[i]]++;
			u[(int)z[i]] = 1;
			++i;
			if (i == n)
				break;
		}
		for (map<char, int>::iterator it = p.begin(); it != p.end(); ++it)
		{
			char c = it->first;
			if (u[(int)c] == 1 || l[c] >= (int)b[c].size())
			{
//				cerr << p[c] << " ";
				continue;
			}
			if (p[c] != b[c][l[c]])
			{
				if (p[c] > b[c][l[c]])
					--p[c];
				else
					++p[c];
			}
//			cerr << p[c] << " ";
		}
//		cerr << endl;

		++T;
	}
	
	cout << "Case #" << TCase + 1 << ": " << T << endl;
}

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	
	int T;
	cin >> T;
	
	for (int i = 0; i < T; ++i)
	{
		int n;
		cin >> n;
		a.resize(n);
		z.resize(n);
		for (int j = 0; j < n; ++j)
			cin >> z[j] >> a[j];
		solve(i);
	}
	
}
