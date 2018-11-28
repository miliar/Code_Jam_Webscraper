#include <iostream> 
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int nt;
	cin>>nt;
	for(int it =0 ;it<nt;it++)
	{
		ll m,n,a,b,c,d,x0,y0;
		cin>>n>>a>>b>>c>>d>>x0>>y0>>m;
		vector<pair<ll,ll> > pts(n);
		pts[0].first = x0;
		pts[0].second  = y0;
		for(int i=0;i<n-1;i++)
		{
			pts[i+1].first = (a*pts[i].first + b)%m;
			pts[i+1].second = (c*pts[i].second + d)%m;	
		}	
		int cnt[3][3];
		for(int i=0;i<3;i++)
			for(int j=0;j<3;j++)
				cnt[i][j] = 0;
		for(int i=0;i<pts.size();i++)
			cnt[(3+pts[i].first%3)%3][(3+pts[i].second%3)%3]++;
		ll res = 0;
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
			{
				ll xx,yy;
				xx = (3 - (pts[i].first + pts[j].first)%3)%3;
				yy = (3 - (pts[i].second + pts[j].second)%3)%3;
				ll count = cnt[xx][yy];
				if((3+pts[i].first%3)%3 == xx&& (3+pts[i].second%3)%3 == yy)
					count --;
				if((3+pts[j].first%3)%3 == xx&& (3+pts[j].second%3)%3 == yy)
					count --;
				res+=count;
			}
			cout<<"Case #"<<it+1<<": "<<res/3<<endl;
	}
	return 0;
}
