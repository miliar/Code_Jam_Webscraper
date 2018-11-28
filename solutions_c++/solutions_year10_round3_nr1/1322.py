#include<iostream>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;
FILE*out=fopen("H://out.txt","w");
FILE *in=fopen("H://in.txt","r");
struct line
{
	int st;
	int end;
};
line a[1005];
bool cmp(line x,line y)
{
	return x.st<y.st;
}
int main()
{
	int test,i,j,n,k;
	int ans;
	fscanf(in,"%d",&test);
	int cas;
	for(cas=1;cas<=test;cas++)
	{
		fscanf(in,"%d",&n);
		for(i=0;i<n;i++)
		{
			fscanf(in,"%d%d",&a[i].st,&a[i].end);
		}
			sort(a,a+n,cmp);
			ans=0;
			for(i=0;i<n;i++)
			{
				//printf("")
				for(j=i+1;j<n;j++)
				{
					if(a[j].end<a[i].end)ans++;
				}
			}
			printf("%d\n",ans);
		
		fprintf(out,"Case #%d: %d\n",cas,ans);
	}
	return 0;
}
