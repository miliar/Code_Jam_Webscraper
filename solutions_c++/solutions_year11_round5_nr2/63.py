#include <stdio.h>
#include <iostream>
#include <sstream>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

int T,ts,i,j,z,mi,a[20000],n,x;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		memset(a,0,sizeof(a));
		scanf("%d",&n);
		mi=1999999999;
		while(n--)
		{
			scanf("%d",&x);
			a[x]++;
		}
		for(i=1;i<=10000;)
			if(a[i]>a[i+1])
			{
				j=i;
				z=0;
				while(a[j]>0)
				{
					a[j]--;
					j--;
					z++;
				}
				if(z<mi)
					mi=z;
			}
			else
				i++;
		if(mi==1999999999)
			mi=0;
		printf("Case #%d: %d\n",++ts,mi);
	}
	return 0;
}