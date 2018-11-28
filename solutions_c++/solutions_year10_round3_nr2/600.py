#include "stdio.h"
#include "stdlib.h" 
#include "math.h"

int num[3];
int signa[3];
int signb[3];

// int qsort(__int* x,int low,int high)
// {
// 	__int32 t;
// 	int m;
// 
// 	if(low<high)
// 	{
// 		//swap(x,low,randint(low,high));
// 		t=x[low];
// 		m=low;
// 		for(int i=low+1;i<=high;i++)
// 		{
// 			if(x[i]<t)swap(x,++m,i);
// 		}
// 		swap(x,low,m);
// 		qsort(x,low,m-1);
// 		qsort(x,m+1,high);
// 	}
// 
// 	return 1;
// }
int main()
{
	FILE* f;
	f=fopen("B-small-attempt0.in","r");
	//f=fopen("B-large.in","r");
	//f=fopen("B-small-attempt0.in","r");
	if(f==NULL)
	{
		printf("file read error£¡");
		exit(1); 
	}

	FILE *w;
	w=fopen("test.out","w");
	//w=fopen("B-large.out","w");
	//w=fopen("B-small-attempt0.out","w");
	if (w==NULL)
	{
		printf("file write error£¡");
		exit(1); 
	}

	int count;
 
	fscanf(f,"%d",&count);
	printf("%d \n",count);
	int temp=1;
	long low;
	long high;
	int fac;
	int sum;

	for (int i=0;i<count;i++)
	{
		fscanf(f,"%d",&low);
		fscanf(f,"%d",&high);
		fscanf(f,"%d",&fac);
		sum=0;
		int base=low;
		int top=0;
		int temp=base;

		printf("%d ",low);
		printf("%d ",high);
		printf("%d\n",fac);

		if(low*fac>=high)sum=0;

		else{
			while (low<high)
			{
				low=low*fac;
				top++;
			}
// 			for (int j=0;;j++)
// 			{
// temp=temp*base;
// if (temp>high)
// {sum=j+1;break;}
// 
// 			}
			temp=1;
			for (int j=0;;j++)
			{
				temp=temp*2;
				if (temp>=top)
				{sum=j+1;break;}

			}

// 			do{
// 				low=low*fac;
// 				if(high%fac==0)
// 				{
// 					high=high/fac;
// 				}
// 				else if (high%fac==1)
// 				{
// 					high=high/fac+1;
// 				}
// 				sum++;
// 			}while(low<high);
		}
		//sum--;

		//ÕâÀïÐ´Ëã·¨
		
		fprintf(w,"Case #%d: ",i+1);
		fprintf(w,"%d",sum);
		fprintf(w,"\n");
	}
	fclose(f);
	fclose(w);

}
