#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>
#include<map>
#include<set>
#pragma comment(linker, "/STACK:167767260")
typedef long long ll;
const int INF = 1000000000;
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define FORN(i,a,b) for(i=a;i>=b;i--)
#define pb push_back 
#define mp make_pair
using namespace std;
int p,i,j,t,k[1001],l[1001],a[1001],tes,o,ii,n,uns1,uns2,uns,vv;
bool z[1001],w[1001];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	memset(z,true,sizeof(z));
	p=0;
	FOR(i,2,1000)
	if(z[i])
	{
		p++;a[p]=i;
		j=i+i;
		while(j<=1000){z[j]=false;j+=i;}
	}

	cin>>tes;
	FOR(o,1,tes)
	{
		cin>>n;
		memset(k,0,sizeof(k));
		uns2=0;

		FOR(i,1,n)
		{
			memset(l,0,sizeof(l));
			ii=i;
			FOR(t,1,p)
			{
				while(ii%a[t]==0){l[t]++;ii/=a[t];}
			}

			bool is=false;
			FOR(t,1,p)if(l[t]>k[t])is=true;

			FOR(t,1,p)k[t]=max(k[t],l[t]);

			if(is)uns2++;
		}

		uns1=0;
		memset(w,false,sizeof(w));
		FOR(i,1,p)
		{
			vv=a[i];
			while(vv*a[i]<=n)vv*=a[i];

			vv=(n/vv)*vv;
			w[vv]=true;
		}
		if(n==1)uns1++;
		FOR(i,1,n)if(w[i])uns1++;

		printf("Case #%d: %d\n",o,uns2-uns1+1);
	}
}