#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(i,a)for(int i=0;i<(a);i++)

int C,M,N,d[10][1024],s[10];
char b[100][100];

inline bool check(int a, int b){return (s[a]&b)==0;}
bool ok(int a)
{
	int l=0,n;
	for(int i=0;i<N;i++)
	{
		n=a&1;
		if(n&l)return 0;
		a>>=1;
		l=n;
	}
	return 1;
}
bool noc(int a, int b)
{
	bool sa[10],sb[10];
	REP(i,N)
	{
		sa[i]=a&1;sb[i]=b&1;
		a>>=1;b>>=1;
	}
	for(int i=1;i<N-1;i++)if(sb[i]&&(sa[i-1]||sa[i+1]))return 0;
	if(N>1&&sb[0]&&sa[1]||N>1&&sb[N-1]&&sa[N-2])return 0;
	return 1;
}

int main()
{
	freopen("C.in","r",stdin);freopen("C.out","w",stdout);
	scanf("%d",&C);
	REP(T,C)
	{
		memset(d,0,sizeof(d));
		scanf("%d%d",&M,&N);
		REP(i,M)
		{
			scanf("%s",b[i]);
			s[i]=0;
			REP(j,N)s[i]=(s[i]<<1)+int(b[i][j]=='x');
		}
		REP(i,1<<N)if(check(0,i)&&ok(i))d[0][i]=__builtin_popcount(i);
		REP(i,M-1)REP(j,1<<N)if(check(i,j)&&ok(j))
			REP(k,1<<N)if(check(i+1,k)&&ok(k)&&noc(j,k))
				d[i+1][k]>?=d[i][j]+__builtin_popcount(k);
		int ans=0;
		REP(i,1<<N)if(check(M-1,i)&&ok(i))ans>?=d[M-1][i];
		printf("Case #%d: %d\n",T+1,ans);
	}
	return 0;
}
