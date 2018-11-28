#include<ctime>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;

lli l, t, n, c;
lli dist[1010]; // MODIFY
lli cumu[1010];

lli getTime(lli timegone,int ind,int l)
{
	if(n==ind) return timegone;
	if(l==0)
	{
	    lli sum=cumu[n-1];
	    if(ind) sum-=cumu[ind-1];
	    return timegone+sum*2;
	}
    	lli rv=getTime(timegone+dist[ind]*2,ind+1,l);

	if(l)
	{
	if(timegone>=t)
	{
	    lli temp=getTime(timegone+dist[ind],ind+1,l-1);
	    rv=min(rv,temp);
	}
	else
	{
	    lli sum=cumu[ind];
	    int visited=t/2;
	    int distrem=sum-visited;
	    lli temp=getTime(t+distrem,ind+1,l-1);
	    rv=min(rv,temp);
	}
	}
	return rv;
}

int main()
{
    int T; cin>>T; int cn=0;
    while(T--)
    {
	 cin>>l>>t>>n>>c;
	for(int i=0;i<c;i++)
	{
	    int ai; cin>>ai;
	    for(lli k=0;k*c+i<=n;k++)
	    {
		dist[k*c+i]=ai;
	    }
	}
//	for(int i=0;i<n;i++) cerr<<dist[i]<<' '; cerr<<endl;
	printf("Case #%d: ",++cn);
	cumu[0]=dist[0];
        for(int i=1;i<n;i++) cumu[i]=dist[i]+cumu[i-1];;
	cout<<getTime(0,0,l)<<endl;




    }

}
