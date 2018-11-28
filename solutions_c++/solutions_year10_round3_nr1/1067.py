#include<stdio.h>
#include <iostream>
#include <queue>

using namespace std;
FILE *fin=fopen("large.in","r");
FILE *fout=freopen("output2.out","w",stdout);
int a[1000],b[1000];
int main ()
{
	int R,N,K,i,h,l,j,temp,no,sum,ans;
	fscanf(fin,"%d",&no);
	
	int count1=1;
    while(no--)
    {
				fscanf(fin,"%d",&N);
				for(i=0;i<N;i++)
				{  
						fscanf(fin,"%d %d",&a[i],&b[i]);
				}
		/*		for(i=0;i<N;i++)
				{  
						printf("%d %d\n",a[i],b[i]);
				}*/
					int count=0;
				for(i=0;i<N;i++)
				{
					for(j=i+1;j<N;j++)
					{
					if((a[i]>a[j]  &&  b[i]<b[j])||(a[i]<a[j] && b[i]>b[j]))
					count++;
					}
				
                }
                printf("Case #%d: %d\n",count1++,count);
}
/*	int jj;
	scanf("%d",&jj);*/
	return 0;
}
		
	
	
	
