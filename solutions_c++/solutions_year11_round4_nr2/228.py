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

char a[1000][1000];
int T,ts,i,j,k,l,m,n,ans,x,y;

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d%d",&n,&m,&i);
		for(i=0;i<n;i++)
		{
			scanf("%s",&a[i]);
			for(j=0;j<m;j++)
				a[i][j]-='0';
		}
		ans=10;
		if(ans>n)
			ans=n;
		if(ans>m)
			ans=m;
		for(;ans>2;ans--)
		{
			for(i=0;i<=n-ans;i++)
				for(j=0;j<=m-ans;j++)
				{
					x=y=0;
					for(k=0;k<ans;k++)
						for(l=0;l<ans;l++)
						{
							if(!k && !l || !k && l==ans-1 || !l && k==ans-1 || k==ans-1 && l==ans-1)
								continue;
							x+=a[i+k][j+l]*(2*k-ans+1);
							y+=a[i+k][j+l]*(2*l-ans+1);
						}
					if(!x && !y)
					{
						i=n;
						break;
					}
				}
			if(i!=n-ans+1)
			{
				printf("Case #%d: %d\n",++ts,ans);
				break;
			}
		}
		if(ans==2)
			printf("Case #%d: IMPOSSIBLE\n",++ts);
	}
	return 0;
}

/*

			
		s[0][0]=a[0][0];
		for(i=1;i<n;i++)
			s[i][0]=s[i-1][0]+a[i][0];
		for(j=1;j<m;j++)
			s[0][j]=s[0][j-1]+a[0][j];
		for(i=1;i<n;i++)
			for(j=1;j<m;j++)
				s[i][j]=s[i][j-1]+s[i-1][j]-s[i-1][j-1]+a[i][j];
		for(i=1;i<n-1;i++)
			for(j=1;j<m-1;j++)
			{
				d[i][j][1].x=d[i][j][1].y=0;
				for(k=-1;k<=1;k++)
					for(l=-1;l<=1;l++)
					{
						d[i][j].x+=k*a[i+k][j+l];
						d[i][j].y+=l*a[i+k][j+l];
					}
			}
		for(o=2;2*o+1<n && 2*o+1<m;o++)
			for(i=o;i<n-o;i++)
				for(j=o;j<m-o;j++)
				{
					d[i][j][o].x=d[i][j][o].y=0;

*/