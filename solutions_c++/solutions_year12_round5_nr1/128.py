#include <cstdio>
#include <algorithm>
#define Sort sort

using namespace std;

const int Maxn=1010;
const double wc=1e-7;

int L[Maxn],p[Maxn];
int id[Maxn];
int n,m,Test;

bool Cmp(int A,int B)
{
	return p[A]*L[B]>p[B]*L[A] || (p[A]*L[B]==p[B]*L[A] && A<B);
}

int main()
{
	freopen("x.in","r",stdin);
	freopen("x.out","w",stdout);
	
	scanf("%d",&Test);
	for (int ii=1;ii<=Test;++ii)
	{
		printf("Case #%d:",ii);
		scanf("%d",&n);
		for (int i=0;i<n;++i) scanf("%d",&L[i]);
		for (int i=0;i<n;++i) scanf("%d",&p[i]);
		for (int i=0;i<n;++i) id[i]=i;
		
		Sort(id,id+n,Cmp);
		
		for (int i=0;i<n;++i) printf(" %d",id[i]);
		printf("\n");
	}
	
	return 0;
}