#include<stdio.h>
#include<string.h>

struct rope{int A,B;} ropes[1000];
int N,i,j,nropes,intersections; 

void main()
{
int cases, index_cases;

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
	//read the number of ropes
	scanf("%d",&nropes);
//	printf("NRopes=%d\n",nropes);
	intersections = 0;
	for (i=0;i<nropes;i++)
	{
		scanf("%d",&ropes[i].A);
		scanf("%d",&ropes[i].B);
	}

	for(i=0;i<nropes-1;i++)
	{
		for (j=i+1;j<nropes;j++)
		{
			if(
				((ropes[i].A < ropes[j].A) && (ropes[j].B < ropes[i].B)) ||
				((ropes[i].A > ropes[j].A) && (ropes[j].B > ropes[i].B)))
			{intersections++;}
		}
	}

	printf("Case #%d: %d\n",index_cases+1,intersections );
}
fclose(stdin) ;
fclose(stdout) ;

}