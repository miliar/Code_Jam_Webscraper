#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
using namespace std;
void process()
{
	
	
}
int main()
{
	int t,i,j,k,n,s,p,c,pos,tmp;
	//freopen("example.txt","r",stdin);
	//freopen("aaa.txt","w",stdout);
	scanf("%d",&t);
	int zz=1;
	while(t--)
	{
		scanf("%d%d%d",&n,&s,&p);
		c=0;pos=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&tmp);
			k=(tmp+2)/3;
			if(k>=p)
			{
				c++;
				continue;
			}
			else if(k<p-1)
				continue;
			else
			{
				int h=tmp/3;
				if(tmp%3==0&&tmp!=0)
					pos++;
				else if(tmp==(h*3+2))
					pos++;
			}
		}
		pos=min(pos,s);
		printf("Case #%d: %d\n",zz,c+pos);
		zz++;
	}
	return 0;
}