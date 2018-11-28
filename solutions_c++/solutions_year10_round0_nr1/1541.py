#include<iostream>
#include<string.h>
#include<cstdio>
using namespace std;
int main()
{
	//freopen("D:\\text.in","r",stdin);
	//freopen("D:\\text2.in","w",stdout);
	int N,K,i,T;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%d %d",&N,&K);
		K=K%((1<<N));
		printf("Case #%d: ",i);
		if(K==((1<<N)-1))
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}