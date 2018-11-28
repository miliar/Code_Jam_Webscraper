#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<string.h>
#include<string>
using namespace std;
int n,T,Ti,da;

int r[1100],s;

int main()
{
    freopen("z.in","r",stdin);
    freopen("z.out","w",stdout);
    int i,a,b,c,d,j,k,z;
    
    int ai,bi;
	
    scanf("%d",&T);    for(Ti=1;Ti<=T;Ti++)
//    while(scanf("%s%s",a,b)!=EOF)
    {	
		printf("Case #%d: ",Ti);
		scanf("%d",&n);
		da=0;s=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&r[i]);
			da=da^r[i];
			s+=r[i];
		}
		if(da)
		{
			printf("NO\n");
			continue;
		}
		
		sort(r,r+n);
		s-=r[0];
		printf("%d\n",s);
	}	
    return 0;
}
