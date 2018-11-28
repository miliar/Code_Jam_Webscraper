#include <cstring>
#include <cstdio>
using namespace std;
int t,a1,a2,b1,b2,a[1000010];

int main()
{
	FILE *input=fopen("c.in","r");
	FILE *output=fopen("c.out","w");
/*	a[1]=1;
	for (long long i=1;i<=1000000;i++)
	{
		a[i]=i+i/2;
		while (a[a[i]-i]<=i) a[i]++;
		fprintf(output,"%d,",a[i]);
		if (a[i]>1000000)
		{
			for (int j=i+1;j<=1000000;j++)
			{
				a[j]=a[j-1];
				if (j%10000==0) fprintf(output,"\n");
			}
			break;
		}
		if (i%10000==0)
		{
			fprintf(output,"\n");
			printf("%d:%d\n",i,a[i]);
		}
	}
*/	fscanf(input,"%d",&t);
	for (int t0=1;t0<=t;t0++)
	{
		fscanf(input,"%d%d%d%d",&a1,&a2,&b1,&b2);
		int s=0;
		for (int i=a1;i<=a2;i++)
			for (int j=b1;j<=b2;j++)
			{
				int x,y,k=1;
				if (i>j)
				{x=j;y=i;}
				else {x=i;y=j;}
				if (x==y) continue;
				while (x<2*y)
				{
					y=y-x;
					int temp;
					temp=x;
					x=y;
					y=temp;
					k=-k;
				}
				if (k==-1) s++;
			}
		fprintf(output,"Case #%d: %d\n",t0,s);
	}
	fclose(input);
	fclose(output);
	return 0;
}