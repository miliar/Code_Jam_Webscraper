#include<iostream>
using namespace std;
int times,n,m,all,use[32][32],op[32][32],now,st[1000],have[32];
char ch1,ch2,ch3;
void mem()
{
	memset(have,0,sizeof(have));
	memset(op,0,sizeof(op));
	memset(use,0,sizeof(use));
	now=0;
	memset(st,0,sizeof(st));
	
}
char gc()
{
	char ch;
	scanf("%c",&ch);
	while (!isalpha(ch)) scanf("%c",&ch);
	return ch;
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&times);
	for (int z=1;z<=times;++z)
	{
		scanf("%d",&n);
		mem();
		for (int a=1;a<=n;++a)
		{
			ch1=gc();
			ch2=gc();
			ch3=gc();
			use[ch1-'A'][ch2-'A']=ch3-'A'+1;
			use[ch2-'A'][ch1-'A']=ch3-'A'+1;
		}
		scanf("%d",&m);
		for (int a=1;a<=m;++a)
		{
			ch1=gc();
			ch2=gc();
			op[ch1-'A'][ch2-'A']=1;
			op[ch2-'A'][ch1-'A']=1;
		}
		scanf("%d",&all);
		for (int a=1;a<=all;++a)
		{
			st[++now]=gc()-'A';
			have[st[now]]++;
		//	printf("push:%c\n",'A'+st[now]);
			if (now>1)
			{
				if (use[st[now]][st[now-1]])
				{
				//	printf("pop:%c %c,%c\n",'A'+st[now-1],'A'+st[now],'A'+use[st[now]][st[now-1]]-1);
					have[use[st[now]][st[now-1]]-1]++;
					have[st[now-1]]--;
					have[st[now]]--;
					st[now-1]=use[st[now]][st[now-1]]-1;
					now--;
				}
				for (int b=0;b<26;++b)
				{
					if ((have[b])&&(op[st[now]][b]))
					{
				//		printf("clear\n");
						now=0;
						memset(have,0,sizeof(have));
					}
				}
			}
		}printf("Case #%d: [",z);
		for (int a=1;a<=now;++a)
		{
			if (a>1) printf(", ");
			printf("%c",'A'+st[a]);
		}
		printf("]\n");
	}
}
