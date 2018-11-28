#include<stdio.h>
int ket(int a)
{
	int ret=1;
	for(;;)
	{
		if(a==0)
		{
			break;
		}
		a/=10;
		ret*=10;
	}
	return ret;
}
int main()
{
	FILE *fp;
	fp=fopen("C-large.in","r");
	int data;
	fscanf(fp,"%d",&data);
	FILE *fp2;
	fp2=fopen("out2.txt","w");
	for(int i=0;i<data;i++)
	{
		int a,b;
		fscanf(fp,"%d%d",&a,&b);
		int sum=0;
		for(int j=a;j<=b;j++)
		{
			int zi=j;
			for(;;)
			{
				zi=(zi+(zi%10)*ket(j))/10;
				if(zi==j)
				{
					break;
				}
				if(zi>j&&zi<=b)
				{
					sum++;
				}
			}
		}
		fprintf(fp2,"Case #%d: ",i+1);
		fprintf(fp2,"%d\n",sum);
	}
}