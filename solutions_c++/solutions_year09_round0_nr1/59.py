#include <cstdio>
#define maxl 20
#define maxd 5005

int L,D,N;
char s[maxl*30];
bool can[maxl][30];
char word[maxd][maxl];

inline void getpos(bool can[],int &p)
{
	for (int i=0;i<26;++i)
		can[i]=false;
	if (s[p]=='(')
	{
		++p;
		while (s[p]!=')')
		{
			can[s[p]-'a']=true;
			++p;
		}
	}else can[s[p]-'a']=true;
	++p;
}

int main()
{
	freopen("A_large.in","r",stdin);
	freopen("A_large.out","w",stdout);
	
	scanf("%d%d%d",&L,&D,&N);
	for (int i=0;i<D;++i)
		scanf("%s",word[i]);
	for (int test=1;test<=N;++test)
	{
		printf("Case #%d: ",test);
		
		scanf("%s",s);
		int p=0;
		for (int i=0;i<L;++i)
			getpos(can[i],p);
		int ans=0;
		for (int i=0;i<D;++i)
		{
			int delta=1;
			for (int j=0;j<L;++j)
			if (!can[j][word[i][j]-'a'])
			{
				delta=0;
				break;
			}
			ans+=delta;
		}
		printf("%d\n",ans);
	}
	return 0;
}
