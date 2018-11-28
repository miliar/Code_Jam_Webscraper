#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<algorithm>
#include<numeric>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<cassert>

#define rep(i,n) for(int i=0;i<n;i++)
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define rp(i,c) rep(i,(c).size())
#define fr(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dbg(x) cerr<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pi;
const int inf=1<<28;
const double INF=1e12,EPS=1e-9;

int main()
{
	int CS; cin>>CS;
	rep(cs,CS)
	{
		ll r,k;
		int n; cin>>r>>k>>n;
		int g[1000]; rep(i,n)cin>>g[i];
		
		int fst[1000]; fill_n(fst,1000,-1);
		fst[0]=0;
		
		int i=0,cfst=0;
		ll ans=0,cpsn,psn[1000];
		
		//find frequency
		int bg=-1,ed=-1;
		for(;i<min(r,1000LL);i++)
		{
			cpsn=0;
			rep(j,n)
			{
				if(cpsn+g[cfst]>k)break;
				cpsn+=g[cfst];
				if(++cfst>=n)cfst-=n;
			}
			psn[i]=cpsn;
			
			if(fst[cfst]>=0)
			{
				bg=fst[cfst]; ed=i+1;
				break;
			}
			
			ans+=cpsn;
			fst[cfst]=i+1;
		}
		
		dbg(ans);dbg(bg);dbg(ed);
		
		if(i<r)
		{
			ll one=accumulate(psn+bg,psn+ed,0LL); dbg(one);
			ans+=(r-i)/(ed-bg)*one;
			i+=(r-i)/(ed-bg)*(ed-bg);
			
			for(;i<r;i++)ans+=psn[(i-bg)%(ed-bg)+bg];
		}
		
		cout<<"Case #"<<cs+1<<": "<<ans<<endl;
	}
	
	return 0;
}
