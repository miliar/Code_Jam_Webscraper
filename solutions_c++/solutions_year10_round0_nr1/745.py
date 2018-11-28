#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<utility>
#include<sstream>
#define Min(a,b) a>b?b:a
using namespace std;

int main()
{
	int tc;
	scanf("%d",&tc);
	int n;
	int k;
	int i;
	int ct=1;
	int flag=0;
	int nbits=0;
	while( tc -- )
	{
		scanf("%d%d",&n,&k);
		flag = 0 ;
		for( i=0;i<=n-1;i++)
		{
			if( k & ( 1 << i ))
			{}
			else
			{
				flag =1;
				break;
			}
		}
		if( flag == 0 )
			printf("Case #%d: ON\n",ct);
		else
			printf("Case #%d: OFF\n",ct);
		ct++;
	}
	return 0;
}



