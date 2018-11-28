#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
#include<string>




int main(int argc,char **argv)
{
	
	FILE *fpIp,*fpOp;
	int num,K,n;
	int i,tmp,j=1;	
	int *final;
	int *ind;
	int count=0;

	fpIp = fopen("input.txt","r");
	fpOp = fopen("output.txt","w");


	fscanf(fpIp,"%d",&num);
	while(j<=num)
	{
		
		fscanf(fpIp,"%d",&K);
		fscanf(fpIp,"%d",&n);
		ind = new int[n];
		for(i=0;i<n;i++)
		{
			fscanf(fpIp,"%d",&tmp);
			ind[i] = tmp;
		}

		final = new int[K+1];
		for(i=0;i<K+1;i++)
			final[i]=0;

		final[1]=1;
		final[3]=2;
		tmp = 3;
		i= 4;
		while(tmp<=K)
		{
			if(final[i]==0)
			 {	
				count++;
				if(count==tmp)
				{
					final[i]=tmp;
					tmp++;
					count=0;
				}
			}
			i++;
			if(i>K)
				i=i%K;
		}

fprintf(fpOp,"%s%d%s","Case #",j,":");
	for(i=0;i<n;i++)
			fprintf(fpOp," %d",final[ind[i]]);
		fprintf(fpOp,"\n");
		j++;
		delete[] ind;
		delete[] final;
	}

//for(i=0;i<K+1;i++)
 //printf("%d\n",final[i]);
		


}			
