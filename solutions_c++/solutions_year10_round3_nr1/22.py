#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
#define oo 1005
int Test,Case;
int N;
struct Tnode
{
	int x,y;
}	a[oo];

inline void Readin()
{
	scanf("%d",&N);
	for (int i=1;i<=N;++i)
		scanf("%d%d",&a[i].x,&a[i].y);
}

inline bool comp(const Tnode& A,const Tnode& B)
{
	return A.x<B.x;
}

inline void Solve()
{
	sort(a+1,a+1+N,comp);
	int Ans=0;
	for (int i=1;i<=N;++i)
		for (int j=1;j<i;++j)
			if (a[i].y<a[j].y) ++ Ans;
	printf("%d\n",Ans);
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
