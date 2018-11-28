#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<map>
#include<set>
#include<string>
#include<vector>
#include<utility>
#include<queue>
#include<iostream>
#include<list>
#include<sstream>
#include<cmath>
#define N 3009

using namespace std;


int lod[N];



int main()
{
	int test ,i,j,k,m,n,cas=1,tt;
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&test);
	while(test--)
	{
		scanf("%d",&n);
		for( i=0;i<n;i++ ) scanf("%d",&lod[i]);

		sort(lod,lod+n);
		    tt = lod[0];
        int sum = 0;
		for(i=1;i<n;i++ )
		{
			tt = tt^lod[i];
			sum+=lod[i];
		}
		if( tt==0  ) printf("Case #%d: %d\n",cas++,sum);
		else printf("Case #%d: NO\n",cas++);
	}
	return 0;
}