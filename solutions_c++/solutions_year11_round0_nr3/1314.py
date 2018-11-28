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
int a;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
    int t,n,i,j,sum,min,ans;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
    	scanf("%d",&n);
    	scanf("%d",&a);
    	sum=a;
    	ans=a;
    	min=a;
    	for(j=2;j<=n;j++)
    	{
    		scanf("%d",&a);
    		if(a<min)
    			min=a;
    		sum=sum^a;
    		ans+=a;
    	}
    	printf("Case #%d: ",i);
    	if(sum!=0)
    		printf("NO\n");
    	else
    		printf("%d\n",ans-min);
    }
	return 0;
}
