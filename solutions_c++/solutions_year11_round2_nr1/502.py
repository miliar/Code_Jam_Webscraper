#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <vector>
using namespace std;
char nc()
{
	char c;
	while(isspace(c=getchar()));
	return c;
}
char op[100][100];
int winn[100],losen[100];
double wp[100],owp[100],oowp[100];
int main()
{
	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
	int testn;
	scanf("%d",&testn);
	for(int tn=1;tn<=testn;tn++)
	{
		memset(losen,0,sizeof(losen));
		memset(winn,0,sizeof(winn));
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				char c;
				c=nc();
				op[i][j]=c;
				if(c=='0')
					losen[i]++;
				else if(c=='1')
					winn[i]++;
			}
			//printf("%d %d\n",losen[i],winn[i]);
		}
		for(int i=0;i<n;i++)
			wp[i]=(double)(winn[i])/(losen[i]+winn[i]);
		for(int i=0;i<n;i++)
		{
			int c=0;
			double s=0;
			for(int j=0;j<n;j++)
				if(op[i][j]!='.')
				{
					if(op[i][j]=='0')
					{
						s+=(double)(winn[j]-1)/(losen[j]+winn[j]-1);
					}
					else
					{
						s+=(double)(winn[j])/(losen[j]+winn[j]-1);
					}
					c++;
				}
			owp[i]=s/c;
		}	
		for(int i=0;i<n;i++)
		{
			int c=0;
			double s=0;
			for(int j=0;j<n;j++)
				if(op[i][j]!='.')
				{
					s+=owp[j];
					c++;
				}
			oowp[i]=s/c;
		}
		printf("Case #%d:\n",tn);
		for(int i=0;i<n;i++)
			printf("%.9f\n",wp[i]*0.25+owp[i]*0.5+oowp[i]*0.25);
	}
}
