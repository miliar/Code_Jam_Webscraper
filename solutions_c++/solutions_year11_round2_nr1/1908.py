#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
char s[200][200];
int win[200],tot[200];
double wp[200],owp[200],oowp[200];
int main()
{
	freopen("A-large.in","r",stdin);
		freopen("A-large.out","w",stdout);
	int t,n,i,j,cas=0;
	scanf("%d",&t);
	while (t--)
	{
		memset(win,0,sizeof(win));
		memset(tot,0,sizeof(tot));
		memset(wp,0,sizeof(wp));
		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
								
								
								cas++;
								scanf("%d",&n);
								for (i=0;i<n;i++)
								{
									getchar();
									for (j=0;j<n;j++)
										scanf("%c",&s[i][j]);
									
								}
								
								for (i=0;i<n;i++)
								{
									for (j=0;j<n;j++)
									{
										if (s[i][j]=='1')
										{
											win[i]++;
											tot[i]++;
										}
										if (s[i][j]=='0')	tot[i]++;
									}
									wp[i]=win[i]*1.00/1.00/tot[i];
									//	cout<<win[i]<<"   "<<tot[i]<<endl;
								}
								for (i=0;i<n;i++)
								{
									int num=0;
									for (j=0;j<n;j++)
									{
										num++;
										if (s[i][j]=='.')	num--;
										if (s[i][j]=='1')
											owp[i]+=win[j]*1.00/(tot[j]-1);
										if (s[i][j]=='0')	
											owp[i]+=(win[j]-1)/1.00/(tot[j]-1);
									}
									owp[i]=owp[i]/1.00/num;
									//	cout<<num<<endl;
								}
								
								for (i=0;i<n;i++)
								{
									int num=0;
									for (j=0;j<n;j++)
									{
										if (s[i][j]!='.')
										{
											oowp[i]+=owp[j];
											num++;
										}
										
									}
									oowp[i]=oowp[i]/1.00/num;
								}   	
								printf("Case #%d:\n",cas);
								for (i=0;i<n;i++)
								{
									double temp;
									temp=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
									printf("%.7lf\n",temp);
								}
	}
	return 0;
}