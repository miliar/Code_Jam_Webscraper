#include <stdio.h>
#include <iostream>
#define M 35

using namespace std;
int f[M];

void proc()
{
	f[1]=2;
	int i;
	for(i=2;i<M;i++)
	{
		f[i]=f[i-1]*2;
	}
}

int main(int argc, char **argv)
{
	int t,index=1;
	proc();
	scanf("%d",&t);
	while(t--)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		if((k+1)%f[n])
		{
			printf("Case #%d: OFF\n",index++);
		}
		else
		{
			printf("Case #%d: ON\n",index++);
		}
	}
	return 0;
}
