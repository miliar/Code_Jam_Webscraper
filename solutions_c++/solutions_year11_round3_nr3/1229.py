#include<iostream>
using namespace std;
int main()
{
	FILE *fin,*fout;
	fin=fopen("in.in","r");
	fout=fopen("out.in","w");
	int t;
	int a[101];
	fscanf(fin,"%d",&t);
	for(int tt=1;tt<=t;tt++)
	{
		int n,l,h;
		fscanf(fin,"%d%d%d",&n,&l,&h);
		int i,j;
		for(i=0;i<n;i++)
		{
			fscanf(fin,"%d",&a[i]);
		}
		int min=h+1;
		for(j=l;j<=h;j++)
		{
			int num=0;
			for(i=0;i<n;i++)
			{
				if(!(a[i]%j==0||j%a[i]==0))
					break;
				else
					num++;
			}
			if(num==n)
			{
				min=j;
				break;
			}
		}
		if(min<=h)
		{
			fprintf(fout,"Case #%d: %d\n",tt,min);
		}
		else
		{
			fprintf(fout,"Case #%d: NO\n",tt);
		}
	}
	return 0;
}


