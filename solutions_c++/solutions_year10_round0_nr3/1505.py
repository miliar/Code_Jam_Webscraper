#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#define oo 6005

using namespace std;

int T;
long long N,R;
long long Limit,Ans;
long long mark[oo],a[oo],f[oo];

void BFS(int x)
{
	memset(mark,0,sizeof(mark));
	memset(f,0,sizeof(f));
	long long p=1,s;
	for (int i=1;i<=N+1;++i){
		if (mark[p]){
			s=i;break;
		}
		long long G=0,q=0;
		for (int j=p;j<p+N;++j)
		if (G+a[j]<=Limit)
			G+=a[j],q=j;
		else break;
		f[i]=f[i-1]+G,mark[p]=(long long)i;
		p=q % N + 1;
	}
	long long E=mark[p]-1,D=R-E;
	Ans=f[mark[p]-1]+D/(s-mark[p])*(f[s-1]-f[E])+f[E+(D % (s-mark[p]))]-f[E];
	printf("Case #%d: %I64d\n",x,Ans);
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	cin>>T;
	for (int l=1;l<=T;++l){
		cin>>R>>Limit>>N;
		for (int i=1;i<=N;++i){
			cin>>a[i];
			a[N+i]=a[i];
		}
		BFS(l);
	}
	return 0;
}
