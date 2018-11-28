#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

int T,n,l,r,m,p,cnt,now;
int a[1010],b[10010],s[10010];

int ok(int lmt)
{
	p = 1;
	while (1)
	{
		while (s[p]==0 && p<=10000) p++;
		if (p>10000) return 1;
		cnt = 0; now = p;
		while (1)
		{
			if (s[now]<=0) return 0;
			cnt++;
			s[now]--;
			if (cnt>=lmt && s[now+1]<=s[now]) break;
			now++;
		}
	}
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	
	cin >> T;
	for (int test=1;test<=T;test++)
	{
		cin >> n;
		for (int i=1;i<=n;i++) cin >> a[i];
		memset(b,0,sizeof b);
		for (int i=1;i<=n;i++) b[a[i]]++;
		l = 1; r = n + 1;
		while (l<r)
		{
			m = (l + r) / 2;
			for (int i=1;i<=10000;i++) s[i] = b[i];
			if (ok(m))
				l = m + 1;
			else
				r = m;
		}
		printf("Case #%d: %d\n",test,l-1);
	}
	
	return 0;
}
