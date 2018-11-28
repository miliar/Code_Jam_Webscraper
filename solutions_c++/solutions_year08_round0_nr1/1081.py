#include <iostream>
using namespace std;
long DP[1020][1020];
char sever[120][120];
char qury[1020][120];

FILE *fp1,*fp2;

int main()
{
  	fp1=fopen("A-small.in","r");
 	fp2=fopen("A-small.out","w");
	long T;
	fscanf(fp1,"%ld",&T);
//	scanf("%ld",&T);
	long f=1;
	while (T--)
	{
		memset(DP,0,sizeof(DP));
		long S;
		fscanf(fp1,"%ld\n",&S);
	//	scanf("%ld",&S);
		long i,j,k;
	//	getchar();

		for (i=1;i<=S;++i)
		{
		fgets(sever[i],120,fp1);
	//	gets(sever[i]);
		}

		long Q;
		fscanf(fp1,"%ld\n",&Q);
	//	scanf("%ld",&Q);
	//	getchar();

		for (i=1;i<=Q;++i)
		{
			fgets(qury[i],120,fp1);
	//		gets(qury[i]);
		}

		long lmax=0;
		for (i=1;i<=Q;++i)
		{
			for (j=1;j<=S;++j)
			{
				char now[120];
				strcpy(now,sever[j]);
				if(strcmp(now,qury[i])==0)
				{
					for (k=1;k<=S;++k)
					{
						if(j!=k)
						{
							if(DP[i][j]!=0)
							{
								if(DP[i-1][k]+1<DP[i][j])
								{
									DP[i][j]=DP[i-1][k]+1;
								}
							}
							else 
							{
								DP[i][j]=DP[i-1][k]+1;
							}
						}
					}
					
				}
				else	
				{
					DP[i][j]=DP[i-1][j];
				}
			}
		}
		

		long mmax=0x7fffffff;

		for (i=1;i<=S;++i)
		{
			if (DP[Q][i]<mmax)
			{
				mmax=DP[Q][i];
			}
		}
	//	printf("Case #%ld: %ld\n",f,mmax);
		fprintf(fp2,"Case #%ld: %ld\n",f,mmax);
		++f;
	}

 	fclose(fp1);
 	fclose(fp2);
	return 0;
}
