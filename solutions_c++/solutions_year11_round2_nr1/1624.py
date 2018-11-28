#include<cstdlib>
#include<stdio.h>
#include<vector>
#include<string>

using namespace std;


int main()
{
	int t,n;
	char c;
	double tab[3][100];
	int tab2[100][100];
	int ileprzec[100];
	int tw,tl;
	double swp;
	scanf("%d",&t);
	for(int i=0;i<t;++i)
	{
		scanf("%d ",&n);
		for(int j=0;j<n;++j)
		{
			ileprzec[j]=0;
			for(int k=0;k<n;++k)
				tab2[j][k]=0;
		}
		for(int j=0;j<n;++j)
		{
			tw=tl=0;
			for(int k=0;k<n;++k)
			{
				scanf(" %c",&c);
				if(c=='1')
				{
					tw++;
					tab2[j][k]=1;
					ileprzec[j]++;
				}
				else if(c=='0')
				{
					tl++;
					tab2[j][k]=0;
					ileprzec[j]++;
				}
				else tab2[j][k]=-1;
			}
			tab[0][j]=((double)tw)/((double)(ileprzec[j]));
		}
		//WP policzone
		for(int j=0;j<n;++j)
		{
			swp=0;
			for(int k=0;k<n;++k)
			{
				if(tab2[j][k]!=-1)
				{
					//printf("%lf ",tab[0][k]);
					swp+=(tab[0][k]*ileprzec[k]-tab2[k][j])/((double)(ileprzec[k]-1));
				}
			}
			//printf("%d\n",ileprzec[j]);
			tab[1][j]=swp/((double)(ileprzec[j]));
		}
		for(int j=0;j<n;++j)
		{
			swp=0;
			for(int k=0;k<n;++k)
				if(tab2[j][k]!=-1) swp+=tab[1][k];
			tab[2][j]=swp/((double)(ileprzec[j]));
			//printf("wp=%lf\towp=%lf\toowp=%lf\n",tab[0][j],tab[1][j],tab[2][j]);
		}
		printf("Case #%d:\n",i+1);
		for(int j=0;j<n;++j)
			printf("%lf\n",0.25*tab[0][j]+0.5*tab[1][j]+0.25*tab[2][j]);
	}
	return 0;
}
