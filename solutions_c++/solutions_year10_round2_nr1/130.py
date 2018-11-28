#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <set>
#include <vector>
using namespace std;
#define VI vector<int>
#define PII pair<int,int>
#define MP make_pair
#define eps 1e-9
#define f0(i,n) for (i = 0; i < n; i++)
set<string> st;

vector<string> pars(string s)
{
	int i , j , k ;
	vector<string> ret;
	i = 1;
	while (i < s.size())
	{
		j = i;
		string t = "";
		while (j < s.size() && s[j] != '/')
		{
			t += s[j];
			j++;
		}
		ret.push_back(t);
		i = j+1;
	}

	return ret;

}
int n , m , k , i , j , p , t;
vector<string> v[10000] , b;
string a[10000];
string s;
int main()
{
	freopen("d:/input.txt" , "r" , stdin);
	freopen("d:/output.txt" , "w" , stdout);
	
	cin>>t;
	for (int tt = 1; tt <= t; tt++)
	{
		for (i = 0; i < 10000; i++)
		{
			v[i].clear();
			a[i].clear();
		}
		int ans = 0;
		cin>>n>>m;
		for (i = 0; i < n; i++)
		{
			cin>>a[i];
			v[i] = pars(a[i]);
		}

		for (i = 0; i < m; i++)
		{
			cin>>s;
			b = pars(s);

			int mx = 0 , nom = -1;
			for (j = 0; j < n; j++)
			{
				k = 0;
				while (k < v[j].size() && k < b.size() && v[j][k] == b[k])
					k++;

				if (k > mx)
				{
					mx = k;
					nom = j;
				}
			}


			if (nom == -1)
			{
				for (j = 0; j < b.size(); j++)
				{
					v[n].push_back(b[j]);
					ans++;
				}

				n++;
			} else
			{
				for (j = 0; j < mx; j++)
					v[n].push_back(v[nom][j]);
				for (j = mx; j < b.size(); j++)
				{
					v[n].push_back(b[j]);
					ans++;
				}
				n++;
			}

		}

		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
	
	return 0;
}