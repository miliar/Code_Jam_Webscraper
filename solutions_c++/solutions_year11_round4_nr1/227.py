#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<vector>
using namespace std;

const double eps = 1e-10;

int T,X,S,R,N,len;
vector< pair<int,int> > v;
double t,ans;

int cmp(pair<int,int> a, pair<int,int> b)
{
	return a.second < b.second;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin >> T;
	for (int test=1;test<=T;test++)
	{
		cin >> X >> S >> R >> t >> N;
		len = X;
		v.clear();
		for (int i=1;i<=N;i++)
		{
			int x,y,z;
			cin >> x >> y >> z;
			v.push_back(make_pair(y-x,z));
			len -= y - x;
		}
		v.push_back(make_pair(len,0));
		sort(v.begin(),v.end(),cmp);
		ans = 0;
		for (int i=0;i<v.size();i++)
		{
			double use = v[i].first / double(v[i].second + R);
			if (use < t - eps)
			{
				t -= use;
				ans += use;
			}
			else
			{
				double run = (v[i].second + R) * t;
				ans += t + (v[i].first - run) / double(v[i].second + S);
				t = 0;
			}
		}
		printf("Case #%d: %lf\n",test,ans);
	}
	return 0;
}
