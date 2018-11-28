#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>


void main()
{
int cases,index_cases,N,L,H,notes[100],i,j,possible,minnote;
freopen("C-small-attempt1.in" , "rt" , stdin ) ;
freopen("C-small-attempt1.out" , "wt" , stdout ) ;
//freopen("C-large.in" , "rt" , stdin ) ;
//freopen("C-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);


//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	scanf("%d",&N);
	scanf("%d",&L);
	scanf("%d",&H);
	for (i=0;i<N;i++)
	{
		scanf("%d",&notes[i]);
	}
	if (L==1)
	{
		minnote = 1;
	}
	else
	{
		minnote = 0;
		possible=1;
		for (j=L;(j<=H);j++)
		{
			for(i=0;(possible==1)&&(i<N);i++)
			{
				if((notes[i]%j!=0)&&(j%notes[i]!=0))
				{
					possible=0;
				}
			}
			if (possible) 
			{
				minnote = j;
				break;
			}
			else possible =1;
		}
	}

	printf("Case #%d: ",index_cases+1);
	if (minnote == 0)
	{
		printf("NO\n");
	}
	else
	{
		printf("%d\n",minnote);
	}
}
fclose(stdin) ;
fclose(stdout) ;
}