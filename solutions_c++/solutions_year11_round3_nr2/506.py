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

double eps=10e-6;

long double maxx (long double a, long double b)
{
	if (a>b)
		return a;
	return b;
}


void solve()
{
	int test;
	cin>>test;
	for (int q=1;q<=test;++q)
	{
		long long l,t,n,c;
		cin>>l>>t>>n>>c;
		vector<int> dist(c);
		for (int i=0;i<c;++i)
			cin>>dist[i];
		int res=2*((n/c)*accumulate(dist.begin(),dist.end(),0)+accumulate(dist.begin(),dist.begin()+n%c,0));
		vector <int> eco (n,0);
		int i=0;
		while (t>0)
		{
			t-=2*dist[i%c];
			i++;
		}
		
		if (t<0 && i<n)
		{
			i--;
			eco[i]=-t/2;
			i++;
		}
		for (;i<n;++i)
		{
			eco[i]=dist[i%c];
		}
		sort(eco.rbegin(), eco.rend());
		for (int i=0;i<l;++i)
			res-=eco[i];
		cout<<"Case #"<<q<<": "<<res<<endl;
	}
}

int main()
{
	prepere();
	solve();
	return 0;
}
