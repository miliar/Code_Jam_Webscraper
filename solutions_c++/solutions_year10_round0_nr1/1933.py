#include<stdio.h>
#include<string.h>

void main()
{
int i,r,N, index_N, T, index_T,receiving,newreceiving;
long num,num2,K,index_K;
char light;
struct snapper 
{
	char state;
	char receiving;
} snappers[30];

freopen("A-large.in" , "rt" , stdin ) ;
freopen("A-large.out" , "wt" , stdout ) ;

N=0;
index_N=0;
T=0;
index_T=0;
K=0;
index_K=0;

//read the number of test cases T
scanf("%d",&T);
//printf("Cases = %d\n",T);
//Loop through all the cases

for (index_T;index_T<T;index_T++)
{
	//read the number of snappers
	scanf("%d",&N);
//	printf("N=%d ",N);
	 //read the number of snaps
	scanf("%d",&K);
//	printf("K=%d\n",K);
	//Initialize structure
	for (i=0;i<30;i++)
	{
		snappers[i].state = 0;
		snappers[i].receiving = 0;
	}
	//plug the first snapper
	snappers[0].receiving = 1;
	receiving = 1;

	//for each snapper check wheteher it will be on or off after K snaps
	for (r=0;r < N;r++)
	{
		num2= 1<< r;
		num = 1 <<( r+1);
		snappers[r].state = char((K%num)/num2);
//		printf("%d ", snappers[r].state/*(K%num)/num2*/);
	}
	//check which is the last snapper receiving power 
	for (r=1,newreceiving=1;r < N;r++)
	{
		if((snappers[r-1].receiving > 0)&&(snappers[r-1].state > 0 ))
		{
			snappers[r].receiving = 1; 
			newreceiving = r+1;
		}
		else
		{
			snappers[r].receiving = 0; 
		}
	}
	receiving = newreceiving;
	//check whether the light is on or off
	if((receiving == N) &&(snappers[N-1].state==1) )
	{
		light = 1;
	}
	else
	{
		light = 0;
	}
	printf("Case #%d: %s\n",index_T+1, light ?"ON":"OFF");
}
fclose(stdin) ;
fclose(stdout) ;

}