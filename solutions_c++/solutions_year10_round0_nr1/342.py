#include<iostream>
#include<stdio.h>
using namespace std;
int a[31];
void init()
{
	a[0]=1;
	for(int i=1;i<31;i++)
		a[i]=a[i-1]*2;
}
int main(void)
{
	init();
	FILE*in=fopen("D://in.txt","r");
	FILE*out=fopen("D://out.txt","w");
    int n;
	fscanf(in,"%d",&n);
	for(int i=1;i<=n;i++)
	{
		int x,y;
		fscanf(in,"%d%d",&x,&y);
		fprintf(out,"Case #%d: ",i);
		if(y%a[x]==(a[x]-1)) fprintf(out,"%s\n","ON");
		else fprintf(out,"%s\n","OFF");
	}
	return 0;
}
		