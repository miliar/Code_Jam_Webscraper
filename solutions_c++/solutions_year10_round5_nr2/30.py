#include <cstdio>
#include <iostream>
using namespace std;
#define oo 100005
#define nn 105
#define inf 1000000000
typedef long long LL;
int q[oo],head,tail,QQ=oo-2;

int f[oo];
long long g[oo];
bool mk[oo];
int a[nn];
int N,M;
LL L;

inline void Readin()
{
	cin >> L >> N;
	for (int i=1;i<=N;++i)
		cin >> a[i];
	sort(a+1,a+1+N);
}

inline void Solve()
{
	memset(f,63,sizeof f);
	memset(g,0,sizeof g);
	memset(mk,0,sizeof mk);
	LL mm=a[N];
	M=a[N];
	
	head=0;
	tail=1;
	q[head]=0;
	f[0]=0;
	g[0]=0;
	mk[0]=true;
	while (head!=tail)
	{
		int u=q[head++],v;
		if (head==QQ) head=0;
		for (int i=1;i<=N;++i)
		{
			v=(u+a[i])%M;
			if (f[v]*mm+g[u]+a[i]>(f[u]+1)*mm+g[v])
			{
				f[v]=f[u]+1;
				g[v]=g[u]+a[i];
				if (!mk[v])
				{
					mk[v]=true;
					q[tail++]=v;
					if (tail==QQ) tail=0;
				}
			}
		}
		
		mk[u]=false;
	}
	
	if (f[L%M]>=inf) puts("IMPOSSIBLE");
	else
	if (g[L%M]>L) puts("IMPOSSIBLE");
	else cout << f[L%M]+(L-g[L%M])/M << endl;
}

int main()
{
	int Test,Case=0;
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
