#include "stdio.h"
void main()
{
	FILE *fp1=fopen("g:\\input.txt","r");
	FILE *fp2=fopen("g:\\ouput.txt","w");
	long T,R,k,n,a[1000];
	long i,j,l,m,this_round,roundNo,profit,isOver;
	fscanf(fp1,"%ld",&T);
	for(m=1;m<=T;++m)
	{
		fscanf(fp1,"%ld",&R);
		fscanf(fp1,"%ld",&k);
		fscanf(fp1,"%ld",&n);
		for(j=0;j<n;++j)
			fscanf(fp1,"%ld",&a[j]);
		profit=0;
		this_round=0;
		roundNo=0;
		isOver=0;
		for(i=0;1;i=(i+1)%n)
		{
			this_round+=a[i];
			isOver++;
			if(this_round>k || isOver==n+1)
			{
				isOver=0;
				this_round-=a[i];
				if(i==0)
					i=n-1;
				else
					i--;
				profit+=this_round;
				this_round=0;
				roundNo++;
			}
			if(roundNo==R)
			{
				fprintf(fp2,"Case #%ld: %ld\n",m,profit);
				break;
			}
		}
	}
}
