#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>



void main()
{
int cases,index_cases,i,j,k,won[100], opponents[100],opponent[100][100],N;
double rpi[100], wp[100],owp[100],oowp[100],owpval[100][100],sum;
char row[100][101];

//freopen("A-small-attempt0.in" , "rt" , stdin ) ;
//freopen("A-small-attempt0.out" , "wt" , stdout ) ;
freopen("A-large.in" , "rt" , stdin ) ;
freopen("A-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);


//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	memset(row,0,sizeof(row));
	scanf("%d",&N);
	memset(opponents,0,sizeof(opponents));
	memset(won,0,sizeof(won));
	for (i=0;i<N;i++)
	{
		scanf("%s",row[i]);
//		printf("Row[%d] = %s\n",i,row[i]);
		for (k=0,j=0;j<N;j++)
		{
//			printf("%c\n",row[i][j]);
			if(row[i][j]!='.')
			{
				opponents[i]=opponents[i]+1;
				opponent[i][k]=j;
				k++;
				if(row[i][j]=='1')
				{
//					printf("won\n");
					won[i]=won[i]+1;
				}
			}
		}
//		printf("won = %d\n",won[i]);
//		printf("opponents = %d\n",opponents[i]);
		wp[i] = (double) won[i] /(double)opponents[i];
//		printf("wp = %f\n",wp[i]);
		for (k=0;k<opponents[i];k++)
		{
//			printf("opponent %d = %d - result%c\n",k,opponent[i][k], row[i][opponent[i][k]]); 
			if(row[i][opponent[i][k]]=='1')
			{
				owpval[i][opponent[i][k]] = (double)(won[i]-1)/(double)(opponents[i]-1);
			}
			else
			{
				owpval[i][opponent[i][k]] = (double)(won[i])/(double)(opponents[i]-1);
			}
//			printf("owpval = %f, %d\n",owpval[i][opponent[i][k]],k);
		}
	}
//	printf("error after this\n");
	for (i=0;i<N;i++)
	{
		for (sum=0,j=0;j<opponents[i];j++)
		{
			sum = sum+owpval[opponent[i][j]][i];
		}
		owp[i] = sum/opponents[i];
	}
	for (i=0;i<N;i++)
	{
		for (sum=0,j=0;j<opponents[i];j++)
		{
			sum = sum + owp[opponent[i][j]];
		}
		oowp[i] = sum/opponents[i];
		rpi[i] = (0.25 * wp[i]) + (0.5 * owp[i])+(0.25 *oowp[i]);

	}
	printf("Case #%d:\n",index_cases+1);
	for (i=0;i<N;i++)
	{
		printf("%.9f\n",rpi[i]);
	}
}
fclose(stdin) ;
fclose(stdout) ;
}