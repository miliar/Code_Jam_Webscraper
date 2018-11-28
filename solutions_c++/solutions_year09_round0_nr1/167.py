#include <cstdio>
#include <cstring>
char dict[5005][25],tmp[505],now[505];
int L,D,N,Ans;
inline bool Check()
{
	for (int i=1;i<=D;++i)
	if (!strcmp(dict[i]+1,tmp+1))
		return true;
	return false;
}
inline void Gene(int st,int dep)
{
	if (dep>L)
	{
		if (Check())
			++Ans;
		return;
	}
	int h=st,t=st;
	if (now[h]=='(')
	{
		while (now[++t]!=')');
		for (int i=h+1;i<t;++i)
		{
			tmp[dep]=now[i];
			Gene(t+1,dep+1);
		}
	}
	else
	{
		tmp[dep]=now[h];
		Gene(h+1,dep+1);
	}
}
int main()
{
	int i;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d%d%d\n",&L,&D,&N) ;
	for (i=1;i<=D;++i)
		gets(dict[i]+1);
	for (i=1;i<=N;++i)
	{
		Ans=0;
		memset(now,0,sizeof(now));
		gets(now+1);
		printf("Case #%d: ",i);
		Gene(1,1);
		printf("%d\n",Ans);
	}
	return 0;
}
