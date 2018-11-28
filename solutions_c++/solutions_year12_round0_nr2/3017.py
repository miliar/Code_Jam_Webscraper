#include <iostream>
#include <stdlib.h>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
int main()
{
	freopen("G://GCJ/B-large.in","r",stdin);
	freopen("G://GCJ/2.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		int n,s,p;
		int res=0;
		scanf("%d%d%d",&n,&s,&p);
		int cnt1=0,cnt2=0;
		for (int j=0;j<n;j++)
		{
			int total_s;
			scanf("%d",&total_s);
			if (total_s >= 3*p-2)
			{
				cnt1++;
			}
			else if (total_s >= 3*p-4)
			{
				if(p == 1 && total_s == 0)
					continue;
				cnt2++;
			}
		}
		res=cnt1+min(s,cnt2);
		printf("Case #%d: %d\n",i+1,res);
	}	
	return 0;
}