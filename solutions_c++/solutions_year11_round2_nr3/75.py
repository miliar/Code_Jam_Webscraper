#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <set>
#include <iostream>
#include <queue>
using namespace std;


vector <vector <int> > gr;
vector <int> u,v;
int n,m;

void gen(vector <int> &a)
{
	for (int i = 0; i < m; i ++)
	{

		vector <int> b;
		vector <int> c;
		bool ok1= false;
		bool ok2 = false;
		for (int k = 0; k < a.size(); k ++)
		{
			if (u[i] <= a[k] && a[k] <= v[i])
				b.push_back(a[k]);
			else
			{
				c.push_back(a[k]);
				ok2 = true;
			}
			if (u[i] < a[k] && a[k] < v[i])
			{
				ok1 = true;
			}

			if (u[i] == a[k] || a[k] == v[i])
				c.push_back(a[k]);
		}
		if (ok1 && ok2)
		{
			gen(b);
			gen(c);
			return;
		}

	}
	gr.push_back(a);
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("res.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t  <= tc; t ++)
	{
		cin >> n >> m;
		u.resize(m);
		v.resize(m);
		for (int i = 0; i < m; i ++)
		{
			cin >> u[i];
			u[i]--;
		}
		for (int i = 0; i < m; i ++)
		{
			cin >> v[i];
			v[i]--;
			if (u[i] > v[i])
				swap(u[i],v[i]);
		}
		gr.clear();
		vector <int> a(n);
		for (int i = 0; i < n; i ++)
			a[i] = i;
		gen(a);
		vector <int> res(n);
		vector <int> now(n);
		vector <int> was(n,false);
		int ans=0;
		for (int tr = 1; tr <= n; tr ++)
		{
			bool ok = false;
			int up = 1;
			for (int i = 0; i < n; i ++)
				up *= tr;
			for (int i = 0; i < up; i ++)
			{
				bool tok = true;
				int x = i;
				for (int j = 0;  j < n; j ++, x/= tr)
					now[j] = x%tr;
				for (int j  =0; tok && j < gr.size(); j ++)
				{
					was.assign(tr,false);
					int difs = 0;
					for (int k = 0; k < gr[j].size(); k ++)
					{
						if (!was[now[gr[j][k]]])
							difs ++;
						was[now[gr[j][k]]] = true;
					}
					if (difs != tr)
						tok = false;
				}
				if (tok)
				{
					ok = true;
					break;
				}
			}


			if (ok)
			{
				ans = tr;
				res = now;
			}
			else
				break;
		}
		printf("Case #%d: %d\n", t, ans);
		for (int i= 0 ; i < n; i ++)
			cout << res[i]+1 << " ";
		cout << endl;
	}

	return 0;
}
