#include <stdio.h>
#include <iostream>
#include"algorithm"
#include <string>
#include <vector>
#include <map>
#include <math.h>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
unsigned int basetwo[32];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,Case,num,ans,N,K;
	cin>>Case;
	basetwo[0]=1;
	for(i=1;i<32;i++)
	{
		basetwo[i] = basetwo[i -1]<<1;
	}
	num=1;
	while (Case--)
	{
		cin>>N>>K;
		K+=1;
		ans=K%basetwo[N];
		if(ans == 0)
		{
			printf("Case #%d: ON\n",num++);		
		}
		else
		{
			printf("Case #%d: OFF\n",num++);		
		}	
	}
	return 0; 
}
/*
   1    2      3      4
O off  off    off    off
1 on   off    off    off
2 off  on     off    off
3 on   on     off    off
4 off  off    on     off
5 on   off    on     off
6 off  on     on     off
7 on   on     on     off
8 off  off    off    on
9 on  off    off    on
*/