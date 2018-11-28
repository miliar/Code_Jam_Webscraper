#include "stdio.h"

int main_t()
{
	int sum;
	freopen("2000000table.txt", "w", stdout);
	for(int i=1;i<2000000;i++)
	{
		sum=0;
		int temp=i;
		while(temp>0)
		{
			sum = sum + (temp%10);
			temp=temp/10;
		}
		printf("%d ",sum);
		//if(i%100==0)printf("\n");
	}
	//scanf("%d",&sum);
	return 0;
}