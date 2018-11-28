#include <stdio.h>
#include <string.h>
int ans[1000];
void sort(int n)
{
	int i,j,temp;
	for (i=0;i<n-1;i++)
		for (j=i+1;j<n;j++)
			if (ans[i]<ans[j])
			{
				temp=ans[i];ans[i]=ans[j];ans[j]=temp;
			}
}

int work(int m,int n)
{
	int i=0,j=0,sum=0,count=1;
	while (i<n)
	{
		sum+=ans[i]*count;
		i++;j++;
		if (j==m) {j=0;count++;}
	}
	return sum;
}

void main()
{
	int i,j,n,p,k,l;
	FILE *fin,*fout;
	fin=fopen("A-small-attempt0.in","r");
	fscanf(fin,"%d\n",&n);
	fout=fopen("A-small.out","w");
	for (i=0;i<n;i++)
	{
		fscanf(fin,"%d %d %d",&p,&k,&l);
		for (j=0;j<l;j++)
		{
			fscanf(fin,"%d",&ans[j]);
		}
		sort(l);
		fprintf(fout,"Case #%d: %d\n",i+1,work(k,l));
	}
}