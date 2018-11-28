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
	    int n,k;
	    sf("%d%d",&n,&k);
	   // pf("%d%d\n",ft,k);
	    ll ft=(ll)1<<n;
	    k%=ft;
	   // pf("%d%d\n",ft,k);
	    if(k==(ft-1))
	    {
	        pf("ON\n");
	    }
	    else
	    {
	        pf("OFF\n");
	    }
	}
	return 0;
}
