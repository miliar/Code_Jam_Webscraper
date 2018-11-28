#include<stdio.h>
int main()
{
	FILE* in;
	FILE* out;
	int test,cas;
	cas=0;
	in=fopen("C-small-attempt1.in","r");
	out=fopen("C-small-attempt1.out","w");
	fscanf(in,"%d",&test);
	while(test--)
	{
		int n,min,max,i,count,m1,m2,bai,shi,ge;
		i=0;
		count=0;
		fscanf(in,"%d %d",&min,&max);
		cas++;
		if(max==1000)
			max--;
		for(i=min;i<=max;i++)
		{
			n=i;
			bai=n/100;
			shi=(n-bai*100)/10;
			ge=n%10;
			if(bai>0)
			{
				m1=ge*100+bai*10+shi;
				m2=shi*100+ge*10+bai;
				if(n<m1&&m1<=max)
					count++;
				if(n<m2&&m2<=max)
					count++;
			}
			else if(bai==0)
			{
				m1=ge*10+shi;
				if(n<m1&&m1<=max)
					count++;
			}
		}
		if(min==1&&max==1000)
			count+=3;
		fprintf(out,"Case #%d: %d\n",cas,count);
	}
	return 0;
}