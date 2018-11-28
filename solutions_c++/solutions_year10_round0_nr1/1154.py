#include<iostream>
#include<stdio.h>
using namespace std;
__int64 mask[35];
int n,k;
FILE*out=fopen("D://out.txt","w");
	
void init()
{
	int i;
	mask[1]=1;
	for(i=2;i<=33;i++)
	{
		mask[i]=mask[i-1]*2;
	}
}
void work()
{
	__int64 t=mask[n+1];
	if(k%t==t-1)  fprintf(out,"ON\n");
	else fprintf(out,"OFF\n");
}
int main()
{
	//freopen("A-small-attempt2.in", "r", stdin);
  
	int test;
	init();
	scanf("%d",&test);
	for(int cas=1;cas<=test;cas++)
	{
		
		scanf("%d%d",&n,&k);
		fprintf(out,"Case #%d: ",cas);
		work();
	}
	return 0;
}
	 
