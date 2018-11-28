#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <algorithm> 
#include <vector> 
#include <string> 
#include <iostream> 
#include <sstream> 
#include <map> 
#include <set> 
#include <queue> 
#include <stack> 
#include <fstream> 
#include <numeric> 
#include <iomanip> 
#include <bitset> 
#include <list> 
#include <stdexcept> 
#include <functional> 
#include <utility> 
#include <ctime> 
using namespace std; 

#define PB push_back 
#define MP make_pair 

#define rep(i,n) for(int i=0;i<(n);++i) 
#define FOR(i,l,h) for(int i=(l);i<=(h);++i) 
#define FORD(i,h,l) for(int i=(h);i>=(l);--i) 
#define print(expr) cout<<(#expr)<<" : "<<(expr)<<endl

typedef vector<int> VI; 
typedef vector<string> VS; 
typedef vector<double> VD; 
typedef long long int64; 
typedef pair<int,int> pii; 

const int maxn=1050;
pii buf[maxn]={};

int main(void)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T; cin>>T;
	FOR(Case,1,T)
	{
		int x,s,r,n;
		double t, ans=0;
		cin>>x>>s>>r>>t>>n;
		int tmp = 0;
		rep(i,n)
		{
			int b,e,w;
			cin>>b>>e>>w;
			buf[i] = MP(w,e-b);
			tmp += e-b;
		}
		buf[n] = MP(0,x-tmp);
		n++;
		sort(buf,buf+n);
		rep(i,n)
		{
			int v1=s+buf[i].first, v2=r+buf[i].first;
			double cnt = (double) buf[i].second / v2;
			if(cnt <= t)
			{
				t -= cnt;
				ans += cnt;
			}
			else
			{
				double s1 = t * v2;
				double s2 = (double)buf[i].second - s1;
				ans += t + s2/v1;
				t=0;
			}
		}
		printf("Case #%d: %.20lf\n",Case,ans);
	}
}