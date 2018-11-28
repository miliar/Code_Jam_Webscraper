#include<cstdio>
#include<cstring>
int main()
{
	int t,n,i,j,win[200],mat[200],ca=0;
	double r[200],owp[200],oowp[200],wp[200],d,e;
	char ch,str[200][200];
	scanf("%d%c",&t,&ch);
	while(t--)
	{
		ca++;
		scanf("%d%c",&n,&ch);
		for (i=0;i<n;i++)
		{
			win[i] = 0;
			mat[i] = 0;
			scanf("%s",str[i]);
			for (j=0;j<n;j++)
			{
				if (i!=j && str[i][j]=='1')
					win[i]++;
				if (i!=j && str[i][j]!='.')
					mat[i]++;
			}
//			printf("i = %d win[i] = %d mat[i] = %d\n",i,win[i],mat[i]);
		}
		for (i=0;i<n;i++)
		{
			d = win[i];
			e = mat[i];
			wp[i] = d/e;
			owp[i] = 0;
			for (j=0;j<n;j++)
			{
				if (i!=j && str[i][j]!='.')
				{
					if (str[i][j]=='0')
						d = win[j]-1;
					else
						d = win[j];
					e = mat[j]-1;
					owp[i] = owp[i] + d/e;
				}
			}
			d = mat[i];
			owp[i] = owp[i]/d;
		}
		printf("Case #%d:\n",ca);
		for (i=0;i<n;i++)
		{
			oowp[i] = 0;
			for (j=0;j<n;j++)
			{
				if (str[i][j]!='.')
					oowp[i] = oowp[i] + owp[j];
			}
			d = mat[i];
			oowp[i] = oowp[i]/d;
//			printf("i = %d wp[i] = %.2lf owp[i] = %.2lf oowp[i] = %.2lf\n",i,wp[i],owp[i],oowp[i]);
			r[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
			printf("%lf\n",r[i]);
		}
	}
	return 0;
}
