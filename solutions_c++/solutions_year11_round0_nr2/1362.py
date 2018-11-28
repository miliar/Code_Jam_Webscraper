#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;
#define M 210

int c,d,n,top;
char cc[40][5],dd[30][5];
char st[200],s[200];

int ab(int x)
{
	if(x<0)
		return -x;
	return x;
}

int main()
{
	int i,j,k,t,tc=1;
	freopen("out.txt","w",stdout);
	freopen("gcj/B-large.in","r",stdin);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&c);
		for(i=0;i<c;i++)
			scanf("%s",cc[i]);
		scanf("%d",&d);
		for(i=0;i<d;i++)
			scanf("%s",dd[i]);
		scanf("%d",&n);
		scanf("%s",s);
		top=0;
		for(i=0;i<n;i++)
		{
			st[top]=s[i];
			top++;
			if(top>1)
			{
				for(j=0;j<c;j++)
				{
					if(cc[j][0]==s[i])
					{
						if(cc[j][1]==st[top-2])
						{
							top-=2;
							st[top]=cc[j][2];
							top++;
							break;
						}
					}
					if(cc[j][1]==s[i])
					{
						if(cc[j][0]==st[top-2])
						{
							top-=2;
							st[top]=cc[j][2];
							top++;
							break;
						}
					}
				}
				if(j<c)
					continue;

				for(j=0;j<d;j++)
				{
					if(dd[j][0]==s[i])
					{
						for(k=0;k<top-1;k++)
						{
							if(dd[j][1]==st[k])
							{
								break;
							}
						}
						if(k<top-1)
							top=0;
					}
					if(dd[j][1]==s[i])
					{
						for(k=0;k<top-1;k++)
						{
							if(dd[j][0]==st[k])
							{
								break;
							}
						}
						if(k<top-1)
							top=0;
					}
				}
			}
		}
		printf("Case #%d: ",tc++);
		printf("[");
		if(top>0)
		{
			printf("%c",st[0]);
			for(i=1;i<top;i++)
				printf(", %c",st[i]);
		}
		printf("]");
		putchar(10);
	}
	return 0;
}


