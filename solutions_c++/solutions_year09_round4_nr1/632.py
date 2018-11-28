#include <iostream>
using namespace std;

int t,i,j,k,m,n,p,ans;
int a[50][50];
int d[50];
char c;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin >> t;
	for (p=1; p<=t; p++)
	{
		cin >> n;
		for (i=1; i<=n; i++)
			for (j=1; j<=n; j++)
			{
				cin >> c;
				if (c=='0') a[i][j]=0; else a[i][j]=1;
			}
		for (i=1; i<=n; i++)
		{
			d[i]=n;
			for (j=n; j>=1; j--)
				if (a[i][j]==1) {d[i]=n-j; break;}
//			cout << d[i] << endl;
		}
		ans=0;
		k=n;
		for (i=1; i<=n; i++)
		{
			k--;
			for (j=i; j<=n; j++)
				if (d[j]>=k) break;
			for (m=j; m>i; m--)
			{
				swap(d[m],d[m-1]);
				ans++;
			}
		}
		printf("Case #%d: %d\n",p,ans);
	}
	
//	system("pause");
	return 0;
}
