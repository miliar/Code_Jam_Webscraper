#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <algorithm>
#include <numeric>
#include <iterator>
#include <cstdio>

using namespace std;

void prepere()
{
#ifdef _DEBUG
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
}

void solve()
{
	int t;
	cin>>t;
	for (int q=1;q<=t;++q)
	{
		int poss=1;
		int n,m;
		cin>>n>>m;
		vector <vector <char> > v (n, vector<char>(m));
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
				cin>>v[i][j];
		for (int i=0;i<n && poss;++i)
			for (int j=0;j<m && poss;++j)
			{
				if (v[i][j]=='#')
				{
					if (i!=n-1 && j!=m-1)
					{
						if (v[i][j+1]=='#' && v[i+1][j]=='#' && v[i+1][j+1]=='#')
						{
							v[i][j]=v[i+1][j+1]='/';
							v[i+1][j]=v[i][j+1]='\\';
						}
						else 
							poss=0;
					}
					else 
						poss=0;
				}
			}
		cout<<"Case #"<<q<<":\n";
		if (poss)
		{
			for (int i=0;i<n;++i)
			{
				for (int j=0;j<m;++j)
					cout<<v[i][j];
				cout<<endl;
			}
		}
		else
			cout<<"Impossible\n";
	}
}

int main()
{
	prepere();
	solve();
	return 0;
}
