#include <stdio.h>
#include <iostream>
#include"algorithm"
#include <string>
#include <vector>
#include <map>
#include <math.h>
#include <functional>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
int main()
{
	freopen("A-large.in","r",stdin);
 	freopen("A-large.out","w",stdout);
	int i,Case,num,p,k,l;
	__int64 ans;
	scanf("%d",&Case);
	num=1;
	vector<int> frequent;
	while (Case--)
	{		
		scanf("%d %d %d",&p,&k,&l);
		ans=0;
		frequent.resize(l);
		for(i=0;i<l;i++)
			scanf("%d",&frequent[i]);
		sort(frequent.begin(),frequent.end(),greater<int>());
		for(i=0;i<l;i++)
        {
		     ans+=frequent[i]*(i/k+1);		  
		}
		printf("Case #%d: %I64d\n",num++,ans);	
	}
	return 0; 
}