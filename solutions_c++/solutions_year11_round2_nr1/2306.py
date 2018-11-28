#include<iostream>
using namespace std;
#include<stdio.h>
#define S 100
main()
{
	int n,i,j,k,num;
	double rpi,wp[S],owp[S],oowp[S],wp_ag,games,win;
	char a[S][S],c;
int t,ic=1;
scanf("%d\n",&t);
while(t--)
{
printf("Case #%d:\n",ic++);
	scanf("%d\n",&n);
	for(i=0;i<n;i++)
	{
		wp[i]=0;
		games=0;
		for(j=0;j<n;j++)
		{
			scanf("%c",&a[i][j]);
			if(a[i][j]=='1')
			{
				wp[i]+=1;
				games+=1;
			}
			else if(a[i][j]=='0')
				games+=1;
		}
	scanf("%c",&c);
		wp[i]/=games;
	}

	for(i=0;i<n;i++)
	{
		num=wp_ag=0;
		for(j=0;j<n;j++)
		{
			if(j!=i && a[i][j]!='.')
			{
				num++;
				games=win=0;
				for(k=0;k<n;k++)
				{
					if(a[j][k]!='.' && k!=i)
					{
						games++;
						if(a[j][k]=='1')
							win++;
							
					}
				}
				wp_ag+=win/games;
//printf("%d %d w=%f g=%f wp=%f\n",i,j,win,games,wp_ag);	
			}
		}
//printf("%d %f\n",i,wp_ag);
		owp[i]=wp_ag/num;
		
	}	

	for(i=0;i<n;i++)
	{
	
		num=oowp[i]=0;
		for(j=0;j<n;j++)
		{
			if(a[i][j]!='.')
			{
				num++;
				oowp[i]+=owp[j];
			}
		}
		oowp[i]/=num;
	}

	for(i=0;i<n;i++)
	{
		//printf("%f\t%f\t%f\n",wp[i],owp[i],oowp[i]);
		rpi=(0.25*wp[i])+(0.5*owp[i])+(0.25*oowp[i]);
		printf("%.12lf\n",rpi);
	}
	

}
}
