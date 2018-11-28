#include <stdio.h>
#include <memory.h>
#include <string.h>
#define oo 1005
struct Thash
{
	char s[oo+105][105];
	int tot;
	inline int Get(char ch[])
	{
		for (int i=1;i<=tot;++i)
			if (!strcmp(s[i],ch)) return i;
		strcpy(s[++tot],ch);
		return tot;
	}
	inline void format()
	{
		memset(s,0,sizeof s);
		tot=0;
	}
}	Hash;
char s[105];
int N,S,Q;
int a[105],b[oo];
char mk[105];
int ans,cnt,Case;

int main()
{
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
	for (scanf("%d",&N);N;N--)
	{
		//readin
		Hash.format();
		scanf("%d",&S);gets(s);
		for (int i=1;i<=S;++i)
		{
			gets(s);
			a[i]=Hash.Get(s);
		}
		
		scanf("%d",&Q);gets(s);
		for (int i=1;i<=Q;++i)
		{
			gets(s);
			b[i]=Hash.Get(s);
		}
		
		//Done
		memset(mk,0,sizeof mk);
		ans=cnt=0;
		for (int i=1;i<=Q;++i)
			if (b[i]<=S && !mk[b[i]])
			{
				++cnt;
				mk[b[i]]=true;
				if (cnt==S)
				{
					++ans;
					cnt=0;
					memset(mk,0,sizeof mk);
					--i;
				}
			}
		printf("Case #%d: %d\n",++Case,ans);
	}
	
	return 0;
}
