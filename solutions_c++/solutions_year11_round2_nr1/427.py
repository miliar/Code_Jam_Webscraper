#include<sstream>
using namespace std;
double wp[101],owp[101],oowp[101],out[101];
char s[201][201];
int main()
{
	int k,j,n,ans,d,tt,t,i,o,b,to,tb,ct1,ttt;
	double ct2,tp,ttp;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%s",s[i]);
//wp
		for(i=0;i<n;i++)
		{
			ct2=ct1=0;
			for(j=0;j<n;j++)
				if(s[i][j]!='.')
				{
					ct1++;
					if(s[i][j]=='1')ct2+=1;
				}
			wp[i]=ct2/ct1;
		}
		for(i=0;i<n;i++)
		{
			tp=ttt=0;//sum wp
			for(j=0;j<n;j++)
				if(s[i][j]!='.')
				{
					ttt++;
					ct2=ct1=0;
					for(k=0;k<n;k++)
						if(i!=k&&s[j][k]!='.')
						{
							ct1++;
							if(s[j][k]=='1')ct2+=1;
						}
					tp+=ct2/ct1;
				}
			owp[i]=tp/ttt;
		}
		for(i=0;i<n;i++)
		{
			ct2=ct1=0;
			for(j=0;j<n;j++)
				if(s[i][j]!='.')
				{
					ct1++;
					ct2+=owp[j];
				}
			oowp[i]=ct2/ct1;
		}
		for(i=0;i<n;i++)
		{
			out[i]=0.25*(wp[i]+oowp[i])+0.5*owp[i];
		}
		printf("Case #%d:\n",tt);
		for(i=0;i<n;i++)
			printf("%.14f\n",out[i]);
	}
	return 0;
}