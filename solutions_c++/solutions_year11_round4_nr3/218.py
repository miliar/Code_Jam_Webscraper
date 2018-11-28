#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl;

typedef long long ll;

int T,l,ans;
ll n;
ll p[33];
int q[33];

int cnt;
int bl[1000001];
ll pr[100000];

int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cnt = 0;
	memset(bl,0,sizeof bl);
	for (int i=2;i<=1000000;i++) if (bl[i]==0)
	{
		pr[++cnt] = i;
		for (int j=i+i;j<=1000000;j+=i) bl[j] = 1;
	}
	
	//printf("cnt=%d\n",cnt);
	
	cin >> T;
	for (int test=1;test<=T;test++)
	{
		cin >> n;
		if (n==1)
		{
			printf("Case #%d: %d\n",test,0);
			continue;
		}
		ans = 1;
		for (int i=1;i<=cnt;i++)
		{
			if (pr[i]*pr[i]>n) break;
			ll pwr = pr[i];
			int add = 0;
			while (pwr<=n)
			{
				pwr *= pr[i];
				add ++;
			}
			//debug(add);
			ans += add - 1;
		}
		printf("Case #%d: %d\n",test,ans);
	}
	
	return 0;
}
