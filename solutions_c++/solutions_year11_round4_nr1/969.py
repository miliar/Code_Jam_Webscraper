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

void prepare()
{
#ifdef _DEBUG
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
}

long double EPS = 1e-6;

void solve()
{
	int tests;
	cin>>tests;
	for (int q=1;q<=tests;++q)
	{
		int x,s,r,n;
		long double t;
		cin>>x>>s>>r>>t>>n;
		vector <int> b(n),e(n),w(n),ww(101,0);

		long double res=0;
		for (int i=0;i<n;++i)
		{
			cin>>b[i]>>e[i]>>w[i];
			ww[w[i]]+=e[i]-b[i];
		}
		ww[0]=x-accumulate(ww.begin()+1,ww.end(),0);
		for (int i=0;i<101;++i)
		{
			if (t*(r+i)<ww[i])
			{
				res+=t+(ww[i]-t*(r+i))/(s+i);
				t=0;
			}
			else
			{
				res+=(ww[i]+.0)/(r+i);
				t-=(ww[i]+.0)/(r+i);
			}
		}
		cout<<"Case #"<<q<<": ";
		printf("%.8lf",res);
		cout<<endl;
		
	}
}

int main()
{
	prepare();
	solve();
	return 0;
}
