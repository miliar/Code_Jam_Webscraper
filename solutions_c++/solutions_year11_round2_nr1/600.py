#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int cs,n,cn=1;
char mp[110][110];
double wp[110];
double owp[110];
double oowp[110];
int win[110],tot[110];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int i,j;
	scanf("%d",&cs);
	while(cs--)
	{
		scanf("%d",&n);
		memset(mp,0,sizeof(mp));
		memset(win,0,sizeof(win));
		memset(tot,0,sizeof(tot));
		for(i=0;i<n;i++)
		{
			scanf("%s",mp[i]);
		}
		printf("Case #%d:\n",cn++);
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++) if(i != j)
			{
				if(mp[i][j] == '1')
				{
					win[i]++;
					tot[i]++;
				}
				else if(mp[i][j] == '0')
				{
					tot[i]++;
				}
			}
			wp[i] = 1.0*win[i]/tot[i];
		}
		for(i=0;i<n;i++)
		{
			double t=0;
			for(j=0;j<n;j++) if(i != j)
			{
				if(mp[i][j] == '1')
				{
					t += 1.0*win[j]/(tot[j]-1);
				}
				else if(mp[i][j] == '0')
				{
					t += 1.0*(win[j]-1)/(tot[j]-1);
				}
			}
			owp[i] = t/tot[i];
		}
		for(i=0;i<n;i++)
		{
			double t=0;
			for(j=0;j<n;j++) if(i != j)
			{
				if(mp[i][j] == '1' || mp[i][j] == '0')
				{
					t += owp[j];
				}
			}
			oowp[i] = t/tot[i];
		}
		for(i=0;i<n;i++)
		{
			printf("%.10lf\n",0.25 * wp[i] + 0.5 * owp[i] + 0.25*oowp[i]);
		}
	}
	return 0;
}
