/*
author:-urrohitash@gmail.com
*/
#include<iostream>
#include<cstdio>


int main()
{
	int N,K;
	int i=1;
	int t;
	int power2[]={2,4,8,16,32,64,128,256,512,1024,};
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	scanf("%d",&t);
	while(t--)
	{
	scanf("%d%d",&N,&K);
	printf("Case #%d",i);
	if((K+1)%power2[N-1]==0)
	printf(": ON\n");
	else
	printf(": OFF\n");
	i++;
	}
	return 0;
}
