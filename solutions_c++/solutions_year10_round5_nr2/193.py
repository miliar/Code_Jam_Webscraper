#include <iostream>
using namespace std;

const int cb=100000;
int p[101];
bool f[cb+1];
long long b[cb+1];
int i,j,m,n;
long long l,ans,q;

int t,c;


int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	for (c=1; c<=t; c++)
	{
		cin >> l >> n;
		for (i=1; i<=n; i++)
			cin >> p[i];
		
		sort(p+1,p+n+1);

		ans=0;
		q=(l-cb)/p[n]+1;
		if (q>0)
		{
			ans+=q;
			l-=(p[n]*q);
		}
		
		memset(f,false,sizeof(f));
		f[0]=true;
		b[0]=0;
		for (j=1; j<=l; j++)
			b[j]=1 << 30;
		
		for (i=1; i<=n; i++)
		{
			for (j=0; j<=l; j++)
			{
				if (f[j] && j+p[i]<=l)
				{
					f[j+p[i]]=true;
					b[j+p[i]]=min(b[j+p[i]],b[j]+1);
				}
			}
		}
		printf("Case #%d: ",c);
		if (f[l]) {ans+=b[l]; cout << ans << endl;} else printf("IMPOSSIBLE\n");
	}
//	system("pause");
	return 0;
}
