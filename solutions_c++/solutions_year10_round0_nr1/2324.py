#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;

int T,N,K;
int bit[101];

int main()
{
	int i,Case=1;
	freopen("A-large.in","r",stdin);
	freopen("aaa.txt","w",stdout);
    scanf("%d",&T);
    for(;T>0;T--)
    {
		scanf("%d%d",&N,&K);
		int mask=1;
		for(i=0;i<101;i++)
		{
			mask = 1 << i;
			if(!(mask & K)) bit[i]=0;
			else            bit[i]=1;
		}
		bool OK=true;
		for(i=0;i<N;i++)
		{
			if(!bit[i])
			{
				OK=false;
				break;
			}
		}
		if(!OK) printf("Case #%d: OFF\n",Case++);
		else    printf("Case #%d: ON\n",Case++);
	}
	//system("pause");
	return 0;
}
		
