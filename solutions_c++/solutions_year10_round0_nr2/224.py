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
#define fr(i,a,b) for(int i=a;i!=b;i++)
#define frr(i,a,b) for(int i=a;i!=b;i--)
#define pf printf
#define sf scanf
#define mp make_pair
#define pb push_back
using namespace std;
ll gcd(ll a,ll b)
{
    return b?gcd(b,a%b):a;
}
ll a[1000];
ll b[1000];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	sf("%d",&T);
	int ca=0;
	while(T--)
	{
	    int n;
	    sf("%d",&n);
	    fr(i,0,n)
	    {
	        sf("%I64d",&a[i]);
	    }
	    sort(a,a+n);
	    ll k=0;
	    fr(i,0,n)
	    {
	        fr(j,i+1,n)
	        {
	            if(!k)
	            {
	                k=a[j]-a[i];
	            }
	            else
	            {
	                k=gcd(k,a[j]-a[i]);
	            }
	        }
	    }
	    //pf("%I64d\n",k);
	    pf("Case #%d: %I64d\n",++ca,(k-a[0]%k)%k);
	}
	return 0;
}
