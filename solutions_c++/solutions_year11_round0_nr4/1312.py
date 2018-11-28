#include <cstdlib>
#include <stdio.h>
#include <math.h>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <queue>
#include <stack>
#include <map>

using namespace std;

int main(){
	freopen("D-large.in","r",stdin);
	freopen("out.txt","w",stdout);
    int t,n,max,i,j,a;
	double ans;
    scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		max=0;
        scanf("%d",&n);
		for(j=1;j<=n;j++)
		{
			scanf("%d",&a);
			if(a!=j)
				max++;
		}
		ans=(double)max;
		printf("Case #%d: %.6lf\n",i,ans);
	}
	return 0;
}
