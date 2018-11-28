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
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	
	//freopen("out.txt","w",stdout);
	int T,cs,ans,n,i,j,len;
	scanf("%d",&T);

	int l[10000],r[10000];
	for(cs=1;cs<=T;cs++)
	{
		ans=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d %d",&l[i],&r[i]);
		for(i=0;i<n;i++)
		{
			for(j=0;j<i;j++)
			{
				if( (l[i]>=l[j]&&r[i]<=r[j]) || (l[i]<=l[j]&&r[i]>=r[j]))
					ans++;
			}
		}
		printf("Case #%d: %d\n",cs,ans);
	}
  	return 0;
}			