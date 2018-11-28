#include <cstdio>
#include <algorithm>
using namespace std;
#define oo 1005
int X,S,R,N;
double t;
struct Tnode
{
	int b,e,w;
	int t;
}	a[oo];

inline void Readin ()
{
	scanf("%d%d%d%lf%d",&X,&S,&R,&t,&N);
	for (int i=1;i<=N;++i)
		scanf("%d%d%d",&a[i].b,&a[i].e,&a[i].w);
}

bool comp(const Tnode& A, const Tnode& B)
{
	return A.w < B.w;
}

inline void Solve()
{
	int rst=X;
	for (int i=1;i<=N;++i)
	{
		rst -= a[i].e- a[i].b;
		a[i].t= a[i].e -a[i].b;
	}
	sort(a+1,a+1+N,comp);
	a[0].t=rst;
	a[0].w=0;
	
	double ans=0;
	for (int i=0;i<=N;++i)
	{
		if (a[i].t <= t*(R+a[i].w))
		{
			ans += (double)a[i].t / (R+a[i].w);
			t -= (double)a[i].t / (R+a[i].w);
		}
		else {
			ans += (double) (a[i].t-t*(R+a[i].w))/(S+a[i].w) + t;
			t = 0;
		}
	}
	
	printf("%.10lf\n",ans);
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	int Test,Case = 0;
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	return 0;
}
