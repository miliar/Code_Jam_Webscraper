#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	freopen("alg.in","r",stdin);
	freopen("outg.txt","w",stdout);
	int T,i,j,N,K;
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cin>>N>>K;
		int flag=0;
		if(!K){printf("Case #%d: OFF\n",i);continue;}
		for(j=0;j<N;j++)
		{
			
			if(!(K&1))
			{
				printf("Case #%d: OFF\n",i);
				flag=1;
				break;
			}
			K=(K>>1);
		}
		if(!flag)printf("Case #%d: ON\n",i);
	}
	return 0;
}