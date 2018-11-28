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

char s[105][5];
int a[105];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
    int t,n,i,j,tmax,omin,bmin,o,b,ff;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
    	scanf("%d",&n);
    	scanf("%s%d",s[1],&a[1]);
    	tmax=a[1];
    	if(s[1][0]=='O')
    	{
    		omin=0;
    		bmin=tmax;
    		o=a[1];
    		b=1;
    	}
    	else
    	{
    		bmin=0;
    		omin=tmax;
    		o=1;
    		b=a[1];
    	}
    	for(j=2;j<=n;j++)
    	{
    		scanf("%s%d",s[j],&a[j]);
    		if(s[j][0]=='O')
    		{
    			if(omin>=abs(a[j]-o))
    			{
    				tmax+=1;
    				omin=0;
    				bmin+=1;
    				o=a[j];
    			}
    			else
    			{
					ff=abs(a[j]-o)-omin+1;
    				tmax+=ff;
    				omin=0;
    				bmin+=ff;
    				o=a[j];
    			}
    		}
    		else
    		{
    			if(bmin>=abs(a[j]-b))
				{
					tmax+=1;
					bmin=0;
					omin+=1;
					b=a[j];
				}
				else
				{
					tmax+=abs(a[j]-b)-bmin+1;
					omin+=abs(a[j]-b)-bmin+1;
					bmin=0;
					
					b=a[j];
				}
    		}
    	}
    	printf("Case #%d: %d\n",i,tmax);
    }
	return 0;
}
