#include <cstdio>
#include <cstring>
#define oo 55
char s[oo][oo];
char t[oo][oo];
int Test,N,K,Case;

inline void Readin()
{
	scanf("%d%d",&N,&K);
	memset(s,0,sizeof s);
	memset(t,0,sizeof s);
	for (int i=1;i<=N;++i)
		scanf("%s",s[i]+1);
}

inline void Solve()
{
	for (int i=1;i<=N;++i)
		for (int j=1;j<=N;++j)
			t[j][N+1-i]=s[i][j];
	memset(s,'.',sizeof s);
	for (int j=1;j<=N;++j)
	{
		int k=N;
		for (int i=N;i>0;--i)
			if (t[i][j]!='.') s[k--][j]=t[i][j];
	}
	
	bool flagB=false,flagR=false;
	for (int i=1;i<=N;++i)
		for (int j=1;j<=N;++j)
		{
			int B=0,R=0;
			for (int k=j;k<j+K && k<=N;++k)
			{
				B+=s[i][k]=='B';
				R+=s[i][k]=='R';
			}
			flagB|=B==K;
			flagR|=R==K;
		}
	for (int j=1;j<=N;++j)
		for (int i=1;i<=N;++i)
		{
			int B=0,R=0;
			for (int k=i;k<i+K && k<=N;++k)
			{
				B+=s[k][j]=='B';
				R+=s[k][j]=='R';
			}
			flagB|=B==K;
			flagR|=R==K;
		}
	
	for (int i=1;i<=N;++i)
		for (int j=1;j<=N;++j)
		{
			int B=0,R=0;
			for (int k1=i,k2=j;k1<i+K && k1<=N && k2<j+K && k2<=N;++k1,++k2)
			{
				B+=s[k1][k2]=='B';
				R+=s[k1][k2]=='R';
			}
			flagB|=B==K;
			flagR|=R==K;
		}
	
	for (int i=1;i<=N;++i)
		for (int j=1;j<=N;++j)
		{
			int B=0,R=0;
			for (int k1=i,k2=j;k1<i+K && k1<=N && k2>j-K && k2>0;++k1,--k2)
			{
				B+=s[k1][k2]=='B';
				R+=s[k1][k2]=='R';
			}
			flagB|=B==K;
			flagR|=R==K;
		}
	
	if (flagB && flagR) puts("Both");
	else if (flagB) puts("Blue");
	else if (flagR) puts("Red");
	else puts("Neither");
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
