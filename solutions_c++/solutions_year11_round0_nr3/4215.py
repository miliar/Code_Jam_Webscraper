#include "stdafx.h"

#include <iostream> 

using namespace std; 

#define inf 1000000001

int pocess(int n)
{
	int i,mi = inf,mask = 0,total = 0,val;
	for(i = 0;i < n; i++)
	{
		scanf("%d",&val); total += val; mi = min(mi,val); mask ^= val;
	}
	if(mask > 0)return 0;
	return total - mi;
}

void main()
{
	freopen("D://CIN.txt","r",stdin);
	freopen("D://COUT.txt","w",stdout);
	int i,t,n;
	scanf("%d",&t);
	for(i = 0;i < t;i++)
	{
		printf("Case #%d: ",i+1);
		scanf("%d",&n); n = pocess(n);		
		if(n == 0)cout << "NO\n"; 
		else cout << n << endl;
	}	
} 

