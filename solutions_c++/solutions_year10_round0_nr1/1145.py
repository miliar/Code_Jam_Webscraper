#include<cstdio>
#include<iostream>
using namespace std;
int state[32];
int main()
{
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++){
		int n,k,temp,flag=0;
		scanf("%d %d",&n,&k);temp=k;
		for(int i=0;i<n;i++){
			if(temp%2==1)	 state[i]=1;
			else		{state[i]=0;flag=1;}
			temp/=2;
		}
		if(!flag)	printf("Case #%d: ON\n",test);
		else		printf("Case #%d: OFF\n",test);	
	}
	return 0;
}				
