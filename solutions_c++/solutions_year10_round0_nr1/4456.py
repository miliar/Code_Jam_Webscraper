#include <stdio.h>
void toggle(int *array,int n)
{	int cnt=1;
	if(array[0]==1)
	{
		while(array[cnt]==1 && cnt < n) cnt++;	
		for(int j=0;j<=cnt;j++)	if(array[j]==1) array[j]=0 ;	else array[j]=1;	
	}	
	else array[0]=1;
				
}
int main()
{
	int testcases;
	int K,N,y=1;
	int arr[30];
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	scanf("%d",&testcases);
	for(int i=1;i<=testcases;i++)
	{	y=1;
		scanf("%d %d",&N,&K);		
		for(int l=0;l<N;l++) arr[l]=0;
		while(K)
		{
			toggle(arr,N);
			K--;		
		}			
		for(int l=0;l<N;l++){	
			if(arr[l]==1) 
			continue;		
			else {
				y=0 ; 
				break;
			      }
				    }

		if(y)
		printf("Case #%d: %s\n",i,"ON");
		else
		printf("Case #%d: %s\n",i,"OFF");			
//		printf("%d ---%d\n",N,K);
	}
return 1;
}
