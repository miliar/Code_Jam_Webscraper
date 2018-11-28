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
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

#define eps 1e-8
#define inf 1000000000
#define MAXN 1010
typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef pair<int,int> PII;

bool pri[1000010];
int prime[1000000];
LL i,j;
int main()
{
	freopen("A-large (2).in","r",stdin);
//	freopen("a.out","w",stdout);
	int cs,c,d,k,s[110],ms,cnt,ma,p,a,b,ans,tmp;
	memset(pri,true,sizeof(pri));
	pri[0]=pri[1]=false;
	for (i=2;i<=1000000;i++)
		if (pri[i])
			for (j=i*i;j<=1000000;j+=i)
				pri[j]=false;
	cnt=0;
	for (i=0;i<1000000;i++)
		if (pri[i])
			prime[cnt++]=i;
	cin>>cs;
	for (c=1;c<=cs;c++)
	{
		cin>>d>>k;
		for (i=0;i<k;i++)
			cin>>s[i];
		if (k==1) cout<<"Case #"<<c<<": I don't know."<<endl;
		else
		{
			ms=0;
			for (i=0;i<k;i++)
				ms=max(ms,s[i]);
			ma=1;
			for (i=0;i<d;i++)
				ma*=10;
			cnt=0;
			for (j=0;prime[j]<ms+1;j++);
			for (;prime[j]<ma;j++)
			{
				p=prime[j];
				for (a=0;a<p;a++)
				{
					b=((s[1]-s[0]*a)%p+p)%p;
					for (i=1;i<k-1;i++)
						if ((s[i]*a+b)%p!=s[i+1]) break;
					if (i==k-1)
					{
						tmp=(a*s[k-1]+b)%p;
						if (cnt==0)
						{
							cnt++;
							ans=tmp;
						}
						else if (ans!=tmp) 
						{
							cnt++;
							break;
						}
					}
//					if (p==9 && a==1 && b==0) cout<<i<<endl;
				}
			}
			if (cnt==1) cout<<"Case #"<<c<<": "<<ans<<endl;
			else cout<<"Case #"<<c<<": I don't know."<<endl;
		}
	}
	while (1);
	return 0;
}
