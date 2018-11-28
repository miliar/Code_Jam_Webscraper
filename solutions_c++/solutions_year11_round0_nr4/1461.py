#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D.txt","w",stdout);
	int T,n,cs=1,a,i,ans;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(i=1,ans=0 ; i <= n ; i++)
		{
			scanf("%d",&a);
			if(a!=i)ans++;
		}
		printf("Case #%d: %d.000000\n",cs++,ans);
	}
	return 0;
}
