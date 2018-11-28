#include<stdio.h>
#include<string.h>

void main()
{

int cases, i, ngroups, index_T,groupsinround,nextgroup;
long runs, capacity, roundincome;
long long totalincome;
struct group 
{
	int next;
	long members;
	long income;
} groups[1000];

freopen("C-large.in" , "rt" , stdin ) ;
freopen("C-large.out" , "wt" , stdout ) ;

cases = 0;
//read the number of test cases 
scanf("%d",&cases);
//printf("Cases = %d\n",cases);
//Loop through all the cases

for (index_T=0 ; index_T<cases; index_T++)
{
	//read the number of runs
	scanf("%d",&runs);
//	printf("Runs=%d\n",runs);
	 //read the capacity
	scanf("%d",&capacity);
//	printf("Capacity=%d\n",capacity);
	 //read the number of groups
	scanf("%d",&ngroups);
//	printf("Number of Groups=%d\n",ngroups);
	totalincome =  0;
	nextgroup = 0;
	//Initialize structure
	for (i=0;i<1000;i++)
	{
		groups[i].members = 0;
		groups[i].income = 0;
		groups[i].next = 0;
	}
	//read the group information
	for (i=0;i<ngroups;i++)
	{
		scanf("%d",&groups[i].members);
//		printf("%d ",groups[i].members);
	}
//	printf("\n");
	//update the table for each group
	for (i =0; i < ngroups; i++)
	{
		for (roundincome = 0,nextgroup=i,groupsinround = 0;;)
		{
			if((roundincome + groups[nextgroup].members <= capacity) && (groupsinround < ngroups))
			{
				roundincome += groups[nextgroup].members;
				groupsinround++;
				nextgroup = (nextgroup+1)% ngroups;
//				printf("nextgroup %d -",nextgroup);
			}
			else
			{
				groups[i].income = roundincome;
				groups[i].next = nextgroup;
				break;
			}
		}
//		printf("Group %d, income %d,next %d\n",i+1, groups[i].income,groups[i].next);
	}
	//Run all the runs
	for (i=0,nextgroup=0 ;i< runs; i++)
	{
		totalincome += groups[nextgroup].income;
		nextgroup = groups[nextgroup].next;
	}
	printf("Case #%d: %I64d\n",index_T+1, totalincome);
}
fclose(stdin) ;
fclose(stdout) ;

}