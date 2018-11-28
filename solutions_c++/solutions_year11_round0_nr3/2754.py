#include <cstdio>
#include <algorithm>
using namespace std;
int T,N,A[1005];
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	for (int Te=1;Te<=T;++Te)
	{
		int xsum=0,sum=0;
		scanf("%d",&N);
		for (int i=0;i<N;++i)
			scanf("%d",&A[i]),xsum^=A[i],sum+=A[i];
		int ret=-1;
		for (int i=0,tot=1<<N;i<tot;++i)
		{
			int x=0,s=0,cnt=0;
			for (int j=0;j<N;++j)
			if (i & (1<<j))	x^=A[j],s+=A[j],++cnt;
			if (cnt>0 && cnt<N && (xsum^x)==x)
				ret=max(ret,max(s,sum-s));
		}
		printf("Case #%d: ",Te);
		if (ret<0)	puts("NO");
		else	printf("%d\n",ret);
	}
	return 0;
}
