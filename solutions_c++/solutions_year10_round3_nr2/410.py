#pragma warning(disable: 4786)
#include<stdio.h>
#include<string>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<map>
#include<iostream>
#include<set>
#include<math.h>
#include<queue>
using namespace std;
		


int main()	
{			
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	//freopen("in.txt","r",stdin);
	int T,cs;
	__int64 i,L,P,C,cnt,now,till;
	scanf("%d",&T);

	for(cs=1;cs<=T;cs++)
	{
		
		scanf("%I64d %I64d %I64d",&L,&P,&C);
		now=L;
		cnt=0;
		till=P/C;
		if(P%C!=0)
			till++;
		while(L<till)
		{
			L*=C;
			cnt++;
		}
	
		i=1<<30;
		while(!(i&cnt))
		{
			if(i==0)break;
			i>>=1;
		}
		cnt=0;
		while(i)
		{
			cnt++;
			i>>=1;
		}
		printf("Case #%d: %I64d\n",cs,cnt);
	}
  	return 0;
}			