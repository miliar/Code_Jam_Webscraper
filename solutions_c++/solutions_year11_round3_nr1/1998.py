#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>



void main()
{
int cases,index_cases,i,k,count,totalcount,R,C,possible;
char row[50][51];
freopen("A-small-attempt0.in" , "rt" , stdin ) ;
freopen("A-small-attempt0.out" , "wt" , stdout ) ;
//freopen("A-large.in" , "rt" , stdin ) ;
//freopen("A-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);


//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	scanf("%d",&R);
	scanf("%d",&C);
	possible = 1;
	totalcount = 0;
	for (i=0;i<R;i++)
	{
		scanf("%s",&row[i]);
		if (possible)
		{
			for(count =0,k=0;k<C;k++)
			{
				if(row[i][k] =='#') count++;
			}
			if (count%2 !=0) possible = 0;
			totalcount = totalcount+count;
		}
	}
	for (i=0;(possible)&&(i<R-1);i++)
	{
		for (k=0;(possible)&&(k<C-1);k++)
		{
			if(row[i][k]=='#')
			{
				if((row[i][k+1]=='#')&&(row[i+1][k]=='#')&&(row[i+1][k+1]=='#'))
				{
					row[i][k]='/';
					row[i][k+1]='\\';
					row[i+1][k]='\\';
					row[i+1][k+1]='/';
					totalcount = totalcount -4;
				}
				else
				{
					possible = 0;
				}
			}
		}
	}
	printf("Case #%d:\n",index_cases+1);
	if (possible)
	{
		for (i=0;i<R;i++)
		{
			for(k=0;k<C;k++)
			{
				printf("%c",row[i][k]);
			}
			printf("\n");
		}
	}
	else
		printf("Impossible\n");
}
fclose(stdin) ;
fclose(stdout) ;
}