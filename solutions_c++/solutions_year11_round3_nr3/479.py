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
		int n, l, m;
		cin>>n>>l>>m;
		vector <int> v(n);
		set <int> s;
		for (int i=0;i<n;++i)
		{
			cin>>v[i];
			s.insert(v[i]);
		}
		int _poss=0;
		cout<<"Case #"<<q<<": ";
		for (int i=l;i<=m && !_poss;++i)
		{
			int poss=1;
			for (int j=0;j<n && poss;++j)
			{
				if (i%v[j]!=0 && v[j]%i!=0)
					poss=0;
			}
			if (poss)
				cout<<i<<endl, _poss=1;
		}
		if (!_poss)
			cout<<"NO"<<endl;
	}
}

int main()
{
	prepere();
	solve();
	return 0;
}
