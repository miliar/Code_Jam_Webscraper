#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>



void main()
{
int cases,index_cases,d,N,Pd,Pg,w,l,possible;
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

	scanf("%d",&N);
	scanf("%d",&Pd);
	scanf("%d",&Pg);
	for (possible = 0,d=1;d<=N;d++ )
	{
		w = (d * Pd)/100;
		l = (d * (100-Pd))/100;
//		printf("%d = %d + %d\n",d,w,l);
		if (w + l == d)
		{
//			printf("%d = %d + %d\n",d,w,l);
			if ((w>0)&&(l>0)&&(Pg>0)&&(Pg<100))
			{
				possible = 1;
			}
			else
			{
				if ((w==0)&&(Pg<100))
				{
					possible = 1;
				}
				else
				{
					if ((l==0)&&(Pg>0))
					{
						possible = 1;
					}
				}
			}
		}
		if (possible) break;
	}
	if (possible)
		printf("Case #%d: Possible\n",index_cases+1);
	else
		printf("Case #%d: Broken\n",index_cases+1);
}
fclose(stdin) ;
fclose(stdout) ;

}