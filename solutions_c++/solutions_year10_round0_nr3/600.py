#include<stdio.h>
#include<iostream>
#include<string>
#include<cstring>
#include<queue>
#include<vector>
#include<map>
#include<sstream>
#include<math.h>
#include<algorithm>
#define ll long long
#define clr(x) memset(x,0,sizeof(x))
#define _clr(x) memset(x,-1,sizeof(x))
#define fr(i,a,b) for( i=a;i!=b;i++)
#define frr(i,a,b) for(int i=a;i!=b;i--)
#define pf printf
#define sf scanf
#define mp make_pair
#define pb push_back
using namespace std;
int a[1010];
int b[10000],v[10000];
ll sum[11000];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	sf("%d",&T);
	int ca=0;
	while(T--)
	{
	    pf("Case #%d: ",++ca);
		int i;
	    int cnt=0;
	    int r,k,n;
	    sf("%d%d%d",&r,&k,&n);
	    int flag=0;
	    fr(i,0,n)
	    {
	        sf("%d",&a[i]);
	        if(a[i]>k)flag=1;
	    }
	    clr(v);
		v[0]=1;
	    int s=0;
		int begin;
	    while(1)
	    {
	        int i=s;
	        ll ret=0;
	        while(1)
	        {

	            if(ret>k-a[i])
	            {
	                break;
	            }
	            ret+=a[i];
	            i=(i+1)%n;
				if(i==s)break;
	        }
	        b[cnt]=s;
	        sum[cnt++]=ret;
	        s=i;
	        if(v[s])
			{
				begin=s;
				break;
			}
	        v[s]=1;
	    }
		fr(i,0,cnt)
		{
			if(b[i]==begin)
			{
				begin=i;
				break;
			}
		}
	    ll ret=0;
	    fr(i,begin,cnt)
	    {
	        ret+=sum[i];
	    }
	    ll ans=0;
	    if(!flag)
	    {
			fr(i,0,begin)
			{
				ans+=sum[i];
			}
			r-=begin;
            int time=r/(cnt-begin);
            r%=(cnt-begin);
            ans+=ret*time;
            fr(i,0,r)
            {
                ans+=sum[begin+i];
            }
	    }
	    else
	    {
	        fr(i,0,cnt)
	        {
	            ans+=sum[i];
	        }
	    }
	    pf("%I64d\n",ans);
	}
	return 0;
}
