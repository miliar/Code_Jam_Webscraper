#include<iostream> 
#include<stdio.h>
#include<stdlib.h>
int a[1000];
using namespace std;
int main()
{
	int T;
	FILE *fp;
	FILE *fp1;                     
	fp=fopen("33.txt","r");             
	fp1=fopen("ans.txt","w");
	fscanf(fp,"%d",&T);
	
	for(int j=1;j<=T;j++)
	{
		int R,K,N,tsum=0,sum;
		fscanf(fp,"%d%d%d",&R,&K,&N);
		for(int i=0;i<N;i++)
		{
			fscanf(fp,"%d",&a[i]);
		     tsum+=a[i];
		}
		int *p=&a[0];
		int *q=&a[N];
		int total=0;
		while(R--)
		{
			
			if(tsum<=K)
			{
			total+=tsum;
			continue;
			}
			sum=0;
			
				while(sum+*p<=K)
				{
					 sum+=*p;
				    p++;
					if(p==q)
					p=&a[0];
				   
				
				}
				total+=sum;
				
		}
		fprintf(fp1,"Case #%d: %d\n",j,total);
	
	}	
	
	fclose(fp);
	fclose(fp1);
	return 0;
}
