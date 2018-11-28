#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<cmath>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl

int T,n,m;
string s;
int a[150],b[150];
long long x,sqrtx;

int contain(int opt, int i)
{
	if ( (opt | (1<<i)) == opt ) return 1;
	else return 0;
}

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	cin >> T;
	for (int test=1;test<=T;test++)
	{
		cin >> s;
		n = s.size();
		for (int i=1;i<=n;i++) if (s[i-1]=='0'||s[i-1]=='1')a[i] = s[i-1] - '0'; else a[i] = 2;
		m = 0;
		for (int i=1;i<=n;i++) if (a[i]==2) b[m++] = i;
		//debug(m);
		for (int opt=0;opt<(1<<m);opt++)
		{
			//debug(opt);
			for (int i=0;i<m;i++) if (contain(opt,i))
				a[b[i]] = 0;
			else
				a[b[i]] = 1;
			
			//printf("a: "); for (int i=1;i<=n;i++) printf("%d ",a[i]); printf("\n");
			x = 0;
			for (int i=1;i<=n;i++)
				x = x * 2 + a[i];
			sqrtx = (int) round(sqrt(x));
			if (sqrtx*sqrtx==x) break;
		}
		printf("Case #%d: ",test);
		for (int i=1;i<=n;i++) printf("%d",a[i]); printf("\n");
	}
	return 0;
}
