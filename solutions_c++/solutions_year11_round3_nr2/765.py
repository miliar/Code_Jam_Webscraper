#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
#define n 1000005
int L,t,N,C,T;
int a[n],A[n],s[n];
vector<int>	sb;
int main()
{
	freopen("B.in","r",stdin);
	freopen("B_.out","w",stdout);
	scanf("%d",&T);
	for (int Te=1;Te<=T;++Te)
	{
		scanf("%d%d%d%d",&L,&t,&N,&C);
		t>>=1;
		for (int i=0;i<C;++i)
			scanf("%d",&A[i]);
		printf("Case #%d: ",Te);
		memset(a,0,sizeof(a));
		memset(s,0,sizeof(s));
		int now=0,sum=0,ret;
		for (int j=1;j<=N;++j)
		{
			a[j]=A[now];
			s[j]=s[j-1]+a[j];
			now=(now+1)%C;
		}
		ret=s[N]*2;
		if (L==1)
		{
			for (int i=0;i<N;++i)
			if (s[i]<t && t<s[i+1])	ret=min(ret,s[N]*2-(s[i+1]-t));
			else
			if (s[i]>=t)	ret=min(ret,s[N]*2-a[i+1]);
		}
		else
		if (L==2)
		{
			for (int i=0;i<N-1;++i)
			{
				int sum=0;
				if (s[i]<t && t<s[i+1])	sum=s[i+1]-t;
				else
				if (s[i]>=t)	sum=a[i+1];
				for (int j=i+1;j<N;++j)
				{
					int svm=sum;
					if (s[j]<t && t<s[j+1])	svm=sum+s[j+1]-t;
					else
					if (s[j]>=t)	svm=sum+a[j+1];
					ret=min(ret,s[N]*2-svm);
				}
			}
		}
		printf("%d\n",ret);
	}
	return 0;
}
