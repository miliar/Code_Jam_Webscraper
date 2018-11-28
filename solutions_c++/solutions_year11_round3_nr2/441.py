#include <iostream>
using namespace std;

double f[1100][10],ti,a[1100],ans;
int i,j,c,n,t,ca,l;

int main()
{
	freopen("in.in","r",stdin);
	freopen("ou.ou","w",stdout);
	cin>>t;
	while (t--)
	{
		ca++;
		cout<<"Case #"<<ca<<": ";
		memset(f,9,sizeof(f));
		f[0][0]=0;
		cin>>l>>ti>>n>>c;
		for (i=1;i<=c;i++) cin>>a[i];
		for (i=c+1;i<=n;i++) a[i]=a[i-c];
		for (i=1;i<=n;i++)
		for (j=0;j<=l;j++)
		{
			double s=a[i]*2;
			f[i][j]=f[i-1][j]+s;
			if (j==0) continue;
			double del=ti-f[i-1][j-1];
			if (del>0)
			{
				if (f[i-1][j-1]+del+(a[i]-del/2)<f[i][j])
				f[i][j]=f[i-1][j-1]+del+(a[i]-del/2);
			} else
			if (f[i-1][j-1]+a[i]<f[i][j]) f[i][j]=f[i-1][j-1]+a[i];
		}
		ans=1e+20;
		for (j=0;j<=l;j++)
		if (f[n][j]<ans) ans=f[n][j];
		printf("%.0lf\n",ans);
	}
}
