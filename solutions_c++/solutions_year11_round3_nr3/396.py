#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
int a[101];
int main()
{
	int repeat,i,j,n,m,ri=1,low,high;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);

	scanf("%d",&repeat);
	while(repeat--)
	{
		scanf("%d",&n);
		scanf("%d%d",&low,&high);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		for(i=low;i<=high;i++)
		{
			for(j=0;j<n;j++)
				if( i%a[j]==0 || a[j]%i==0 ) continue;
				else break;
			if( j==n ) break;
		}
		printf("Case #%d: ",ri++);
		if( i<=high ) printf("%d\n",i);
		else puts("NO");
		
	}
	return 0;
}