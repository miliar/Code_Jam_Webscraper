#include <cstdio>
#include <cstring>
#define maxn 12000005
char s[2005];
bool f[maxn];
int Res[maxn],tmp[32],base;
inline void Prepare(int u)
{
	if (f[u])
		return;
	f[u]=1;
	if (u==1)
	{
		Res[u]|=(1<<base);
		return;
	}
	int s=0;
	memset(tmp,0,sizeof(tmp));
	for (int k=u;k;k/=base)
		tmp[++tmp[0]]=k%base;
	for (int i=1;i<=tmp[0];++i) 
		s+=tmp[i]*tmp[i];
	Prepare(s);
	if (Res[s]&(1<<base)) 
		Res[u]|=(1<<base);
}		

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int i,j;
	for (base=2;base<=10;++base)
	{
		memset(f,0,sizeof(f));
		for (i=1;i<=maxn;++i)
		if (!f[i]) 
			Prepare(i);
	}
	int T;scanf("%d\n",&T);
	for (int TT=1;TT<=T;++TT)
	{	
		gets(s+1);
		int t=0;
		for (i=1;s[i];++i)
		{
			while (s[i]==' ')
				++i;
			if (!s[i]) 
				break;
			int now=0;
			for (;'0'<=s[i]&&s[i]<='9';++i)
				now=now*10+s[i]-48;
			t|=(1<<now);
			if (!s[i])
				break;
		}
		for (i=2;i<=maxn;++i)
		if ((Res[i]&t)==t)
		{
			printf("Case #%d: %d\n",TT,i);
			break;
		}
	}
	return 0;
}
