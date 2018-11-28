#include<iostream>
using namespace std;
int main()
{
	FILE *fin;
	FILE *fout;
	fin=fopen("in.in","r");
	fout=fopen("out.in","w");
	int t;
	fscanf(fin,"%d",&t);
	for(int tt=1;tt<=t;tt++)
	{
		int n;
		int a[1000];
		fscanf(fin,"%d",&n);
		int min=1000001;
		int max=0;
		for(int i=0;i<n;i++)
		{
			fscanf(fin,"%d",&a[i]);
			if(a[i]<min)
				min=a[i];
			max+=a[i];
		}
		int tag=20;
		bool tage=true;
		int sum;
		while(tag--)
		{
			sum=0;
			for(int k=0;k<n;k++)
			{
				sum+=a[k]%2;
				a[k]/=2;
			}
			if(sum%2==1)
			{
				tage=false;
				break;
			}
			else
				continue;
		}
		if(tage)
			fprintf(fout,"Case #%d: %d\n",tt,max-min);
		else
			fprintf(fout,"Case #%d: NO\n",tt);
	}
	return 0;
}