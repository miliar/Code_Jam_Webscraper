#include <iostream>
using namespace std;
typedef long long LL;
int g[1010];
int hash[1010];
LL num[1010];
bool flag[1010];
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T;
	scanf("%d",&T);
	int b = 1;
	while (T--)
	{
		int R,k,n;
		scanf("%d%d%d",&R,&k,&n);
		int i;

		for (i=0;i<n;++i)
		{
			scanf("%d", g+i);
		}

		memset(hash,-1,sizeof(hash));
		i = 0;
		int len = 0;
		while (hash[i] == -1)
		{
			hash[i] = len;
			int now = k;
			LL ct = 0;
			memset(flag,0,sizeof(flag));
			while (now - g[i] >=0 && !flag[i])
			{
				flag[i] = true;
				ct += g[i];
				now -= g[i];
				i = (i+1) % n;
			}
			num[len] = ct;	
			++len;
		}

		int rd = hash[i];
		int nlen = len - rd;
		LL sum = 0;
		for (i = 0; i < rd && i < n; ++i)
		{
			sum += num[i];
		}

		LL ct2 = 0;
		for (i = rd ; i < len; ++i)
		{
			ct2 += num[i];
		}
		R = R - rd;
		if (R < 0)
		{
			R = 0;
		}
		int mul = R / nlen;
		int dd = R % nlen;
		sum += mul * ct2;
		for (i = 0; i < dd; ++i)
		{
			sum += num[rd + i];
		}
		printf("Case #%d: %lld\n",b,sum);
		++b;
	}
	return 0;
}