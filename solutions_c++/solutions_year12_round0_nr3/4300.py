#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <cmath>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cctype>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define rall(a) (a).rbegin(), (a).rend()
#define mp make_pair
#define pb push_back

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
}

bool check (int a, int b)
{
	string n,m;
	while(a)
	{
		n+=a%10+'0';
		a/=10;
	}
	reverse(all(n));

	while(b)
	{
		m+=b%10+'0';
		b/=10;
	}
	reverse(all(m));

	if (n.size()!=m.size())
		return false;

	for (int i=1; i<m.size(); ++i)
	{
		string m_;
		for (int j=i; j<m.size(); ++j)
			m_+=m[j];
		for (int j=0; j<i; ++j)
			m_+=m[j];
		if (n==m_)
			return true;
	}
	return false;
}

vector<vector<int> > cache(1001, vector<int>(1001,-1));

int checker(int a, int b)
{
	int ans=0;
	for (int i=a; i<b; ++i)
			for (int j=i+1; j<=b; ++j)
			{
				if (cache[i][j]==-1)
					if (check(i,j))
					{
						++ans;
						cache[i][j]=1;
					}
					else
						cache[i][j]=0;
				else if (cache[i][j]==1)
					++ans;
			}
	return ans;
}

void solve()
{
	int n;
	cin>>n;
	for (int test=1;test<=n;++test)
	{
		cout<<"Case #"<<test<<": ";
		int a,b;
		cin>>a>>b;
		if(b==1000)
			b=999;
		int ans=0;
		if (a<10 && b>=10)
		{
			ans+=checker(a,9);
			a=10;
		}
		if (a<100 && b>=100)
		{
			ans+=checker(a,99);
			a=100;
		}
		ans+=checker(a,b);
		cout<<ans;
		cout<<endl;
	}
}

int main()
{
	prepare();
	solve();
	return 0;
}