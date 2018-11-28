#include<stdio.h>
#include<memory.h>
//
bool dsmap[128][128];
char upmap[128][128];
char qu[123456],qi;
int hm[128];

//
int main()
{
	freopen("test/bl.in","r",stdin);
	freopen("test/bl.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int ii=0;ii<T;ii++)
	{
		memset(dsmap,0,sizeof(dsmap));
		memset(upmap,0,sizeof(upmap));
		qi=0;
		memset(hm,0,sizeof(hm));
		int t;
		char st[123456];
		scanf("%d",&t);
		for(int i=0;i<t;i++)
		{
			scanf("%s",st);
			upmap[st[0]][st[1]]=st[2];
			upmap[st[1]][st[0]]=st[2];
		}
		scanf("%d",&t);
		for(int i=0;i<t;i++)
		{
			scanf("%s",st);
			dsmap[st[0]][st[1]]=1;
			dsmap[st[1]][st[0]]=1;
		}
		scanf("%d",&t);
		scanf("%s",st);
		qi=0;
		for(int i=0;i<t;i++)
		{
			qu[qi]=st[i];
			hm[st[i]]++;
			qi++;
			while(qi>=2)
			{
				if(upmap[qu[qi-1]][qu[qi-2]]==0)
				{
					break;
				}else
				{
					hm[qu[qi-1]]--;
					hm[qu[qi-2]]--;
					hm[upmap[qu[qi-1]][qu[qi-2]]]++;
					qu[qi-2]=upmap[qu[qi-1]][qu[qi-2]];
					qi-=1;
				}
			}
			if(qi>=2)
			{
				for(int j=0;j<128;j++)
				{
					if(dsmap[qu[qi-1]][j]&&(hm[j]>0))
					{
						//puts("yoo");
						qi=0;
						memset(hm,0,sizeof(hm));
						break;
					}
				}
			}
		}
		if(qi==0)
		{
			printf("Case #%d: []\n",ii+1);
		}else
		{
			printf("Case #%d: [%c",ii+1,qu[0]);
			for(int i=1;i<qi;i++)
			{
				printf(", %c",qu[i]);
			}
			printf("]\n");
		}
	}
}
