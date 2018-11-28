#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,n,i,j,ti,tj,p,res;
	char s[11];
	scanf("%d",&t);
	for(int tt = 0; tt < t; tt++)
	{
		scanf("%d",&n);
		res = 0;
		i = 1; ti = 0;
		j = 1; tj = 0;
		for(int r = 0; r < n; r++)
		{
			scanf("%s%d",&s,&p);
			if (s[0] == 'O')
			{	
				ti += max(abs(i - p) - tj,0) + 1;
				res += max(abs(i - p) - tj,0) + 1;
                    i = p;
                    tj = 0;
			} else
			{
				tj += max(abs(j - p) - ti,0) + 1;
				res += max(abs(j - p) - ti,0) + 1;
                    j = p;
                    ti = 0;
			}			
		}
		printf("Case #%d: %d\n",tt + 1,res);
	}
	return 0;
}
