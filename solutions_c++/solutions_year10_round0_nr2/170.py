#include <cstdio>
#include <algorithm>
using namespace std;
#define oo 1005
int Test,Case;
int a[oo];
int N;

inline void Readin()
{
	scanf("%d",&N);
	for (int i=1;i<=N;++i)
		scanf("%d",a+i);
}

inline void Solve()
{
	sort(a+1,a+1+N);
	int t=0;
	for (int i=1;i<N;++i)
		t=__gcd(t,a[i+1]-a[i]);
	
	printf("%d\n",(t-a[1]%t)%t);
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
