#include<cstdio>
using namespace std;

int main()
{
	int t,n;
	char wl[105][105];
	int a[105][105];
	double wp[105],owp[105],oowp[105],rpi[105];
	freopen("text.in","r",stdin);
	freopen("text.out","w",stdout);
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++) 
		{
			scanf("%s",wl[i]);
			for(int j=0;j<n;j++) 
			{
				if (wl[i][j]=='.') a[i][j]=-1;
				if (wl[i][j]=='0') a[i][j]=0;
				if (wl[i][j]=='1') a[i][j]=1;
			}
		}
		int tot,win;
		for(int i=0;i<n;i++)
		{
			tot=0;win=0;
			for(int j=0;j<n;j++)
			{
				if (a[i][j]>=0)
				{
					tot++;
					if (a[i][j]==1) win++;
				}
			}
			wp[i]=double(win)/double(tot);
		}
		double k1;
		int tot2;
		for(int i=0;i<n;i++)
		{
			tot=0;k1=0;
			for(int j=0;j<n;j++)
			{
				if (a[i][j]>=0)
				{
					tot2=0;win=0;
					for(int l=0;l<n;l++)
					{
						if (a[j][l]>=0 && l!=i)
						{
							tot2++;
							if (a[j][l]==1) win++;
						}
					}
					tot++;
					k1+=double(win)/double(tot2);
				}
			}
			owp[i]=k1/double(tot);
		}
		for(int i=0;i<n;i++)
		{
			tot=0;k1=0;
			for(int j=0;j<n;j++)
			{
				if (a[i][j]>=0)
				{
					tot++;
					k1+=owp[j];
				}
			}
			oowp[i]=k1/double(tot);
		}
		for(int i=0;i<n;i++) rpi[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
		printf("Case #%d:\n",cas);
		for(int i=0;i<n;i++) printf("%.10lf\n",rpi[i]);
	}
	return 0;
}

