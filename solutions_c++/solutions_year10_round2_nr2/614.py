#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define sz 52

int x[sz];
int v[sz];
bool flag[sz];

int main()
{
//	freopen("B.in","r",stdin);//freopen("B_output.txt","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin);freopen("B-small-attempt2.out","w",stdout);
//	freopen("B-small-attempt3.in","r",stdin);freopen("B-small-attempt3.out","w",stdout);
//	freopen("B-small-attempt4.in","r",stdin);freopen("B-small-attempt4.out","w",stdout);
	freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);

	int _kase,kase=0,n,K,B,T,i,d,cnt,opr;
	cin>>_kase;
	while( _kase-- )
	{
		cin >> n >> K >> B >> T ;
		for(i=0;i<n;i++) flag[i]=false;
		for(i=0;i<n;i++) cin>>x[i];
		for(i=0;i<n;i++) cin>>v[i];

		cnt=opr=0;
		if(K!=0)
		{
			for( i=n-1; i>=0; i--)
			{
				d = x[i] + v[i]*T ;
				if( d>=B )
				{
					K--;
					flag[i]=true;
				}
				//printf("%d: %d --> %d\n",i,d,K);
				if(K==0) break;
			}

			if(K==0)
			{
				cnt=opr=0;
				for( ;i<n;i++)
				{
					if(flag[i])
					{
						cnt++;
					}
					else
					{
						opr+=cnt;
					}
				}
			}
		}

		printf("Case #%d: ",++kase);
		if( K==0 ) printf("%d\n",opr);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}