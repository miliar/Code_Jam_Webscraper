#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>

using namespace std;

char ji[300][300];
int op[300][300];
char ans[1000];
char po[1000];

int main()
{
	int i,j;
	int cas=1;
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;scanf("%d",&t);
	while(t--)
	{
		int at=0;
		ans[at++]='#';
		memset(ji,0,sizeof(ji));
		memset(op,0,sizeof(op));
		int c,d;
		char temp[10];
		scanf("%d",&c);
		for(i=0;i<c;++i)
		{
			scanf("%s",temp);
			ji[temp[0]][temp[1]]=temp[2];
			ji[temp[1]][temp[0]]=temp[2];
		}
		scanf("%d",&d);
		for(i=0;i<d;++i)
		{
			scanf("%s",temp);
			op[temp[0]][temp[1]]=1;
			op[temp[1]][temp[0]]=1;
		}
		int n;scanf("%d",&n);
		scanf("%s",po);
		for(i=0;i<n;++i)
		{
			char c=ans[at-1];
			//if(c==po[i]) continue;
			if(ji[c][po[i]]!=0)
			{
				ans[at-1]=ji[c][po[i]];
			}
			else
			{
				int f=0;
				for(j=1;j<at;++j)
				{
					if(op[ans[j]][po[i]])
					{f=1;break;}
				}
				if(f)
					at=1;
				else ans[at++]=po[i];
			}
		}
		printf("Case #%d: ",cas++);
		printf("[");
		if(at>1)
		{
			for(i=1;i<at-1;++i)
				printf("%c, ",ans[i]);
			printf("%c",ans[at-1]);
		}
		printf("]\n");
	}
}