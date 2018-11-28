
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <stack>
#include <algorithm>
using namespace std;
typedef __int64 INT;
int c,r,d,mx;
char a[501][501];
bool ok(int i,int j,int c)
{
	int ii,jj,t;
	INT resultx=0,resulty=0;

	for(ii=0;ii<c;ii++)
	{
		for(jj=0;jj<c;jj++)
		{
			if( ii==0 && jj==0 || ii==0 && jj==c-1 || ii==c-1 && jj==0 || ii==c-1 && jj==c-1) continue;
			t=a[i+ii][j+jj]-'0';
			if( c%2)
			{
				resultx+=t*(ii-c/2);
				resulty+=t*(jj-c/2);
			}
			else
			{
				if( ii>=c/2 )
					resultx+=t*(ii-c/2+1);
				else
					resultx+=t*(ii-c/2);	
				if( jj>=c/2) resulty+=t*(jj-c/2+1);
				else resulty+=t*(jj-c/2);
			}
		}
	}
	if( resultx==0 && resulty==0) return true;
	else return false;
}
int main()
{
	int repeat,ri=1,i,j,flag,ii,jj;
	freopen("B-small-attempt3.in","r",stdin);
	freopen("1.out","w",stdout);

	scanf("%d",&repeat);
	while(repeat--)
	{
		flag=0;
		scanf("%d%d%d",&r,&c,&d);
		for(i=0;i<r;i++)
			scanf("%s",a[i]);
		for(i=3;i<=r && i<=c;i++)
		{
			for(ii=0;ii<c-i+1;ii++)
			{
				for(jj=0;jj<r-i+1;jj++)
				{
					if(ok(ii,jj,i))
					{
						flag=i;
						break;
					}
				}
				if( flag==i) break;
			}
		}
		printf("Case #%d: ",ri++);
		if( flag==0 ) puts("IMPOSSIBLE");
		else printf("%d\n",flag);
	}
	return 0;
}
