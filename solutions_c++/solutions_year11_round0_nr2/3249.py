#include<stdio.h>
#include<string.h>


void main()
{
int cases,index_cases,ncombinations,nopposed,nelements,i,j,n;
char combinations[26][26],opposed[26][26], elementlist[101],inputlist[101],comb1,comb2,comb3,combaux[4];

//freopen("B-small-attempt1.in" , "rt" , stdin ) ;
//freopen("B-small-attempt1.out" , "wt" , stdout ) ;
freopen("B-large.in" , "rt" , stdin ) ;
freopen("B-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);
//Loop through all the cases
for (index_cases=0 ; index_cases<cases; index_cases++)
{
	n=0;
	nopposed =0;
	ncombinations=0;
	memset (combinations,0,sizeof(combinations));
	memset (opposed,0,sizeof(opposed));
	memset (elementlist,0,sizeof(elementlist));
	memset (inputlist,0,sizeof(inputlist));
	nelements = 0;

	scanf("%d",&ncombinations);
//	printf("Ncomb = %d\n",ncombinations);
	for(i=0;i<ncombinations;i++)
	{
		scanf("%s",combaux);
		comb1 = combaux[0]- 'A';
		comb2 = combaux[1]- 'A';
		comb3 = combaux[2]- 'A';
//		printf("%c%c%c - %d,%d,%d\n",comb1+'A',comb2+'A',comb3+'A',comb1,comb2,comb3);
		combinations[comb1][comb2] = comb3;
		combinations[comb2][comb1] = comb3;
	}
	scanf("%d",&nopposed);
//	printf("Nopp = %d\n",nopposed);
	for(i=0;i<nopposed;i++)
	{
		scanf("%s",combaux);
		comb1 = combaux[0]- 'A';
		comb2 = combaux[1]- 'A';
//		printf("%c%c - %d,%d\n",comb1+'A',comb2+'A',comb1,comb2);
		opposed[comb1][comb2] = 1;
		opposed[comb2][comb1] = 1;
	}
	scanf("%d",&n);
	scanf("%s",inputlist);
	for (i=0;i<n;i++)
	{
		//put element at the end of list
		elementlist[nelements] = inputlist[i] - 'A';
		//check to see if combines with previous
		if((nelements) &&(combinations[elementlist[nelements]][elementlist[nelements-1]]))
		{
			elementlist[nelements-1] = combinations[elementlist[nelements]][elementlist[nelements-1]];
		}
		else //check to see if opposed to any other on the list
		{
			nelements++;
			for (j=0;j<nelements-1;j++)
			{
				if (opposed[elementlist[nelements-1]][elementlist[j]])
				{
					nelements = 0;
					break;
				}
			}
			
		}
		
	}
	printf("Case #%d: [",index_cases+1);
	if (nelements)
	{
		printf("%c",elementlist[0]+'A');
		for (i=1;i<nelements;i++)
		{
			printf(", %c",elementlist[i]+'A');
		}
	}
	printf("]\n");
}
fclose(stdin) ;
fclose(stdout) ;

}