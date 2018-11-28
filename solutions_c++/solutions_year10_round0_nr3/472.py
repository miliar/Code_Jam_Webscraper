#include <cstdio>
#define oo 1005
int N,K,R;
int a[oo];
int s[oo],next[oo];
int Test,Case;

inline void Readin()
{
	scanf("%d%d%d",&R,&K,&N);
	for (int i=0;i<N;++i)
		scanf("%d",a+i);
}

inline void Solve()
{
	for (int i=0;i<N;++i)
	{
		int x=0;
		for (int j=0;j<N;++j)
		{
			x+=a[(i+j)%N];
			if (x<=K)
			{
				s[i]=x;
				next[i]=(i+j)%N;
			}
			else break;
		}
		next[i]=(next[i]+1)%N;
	}
	
	long long Sum=0;
	for (int i=1,u=0;i<=R;++i)
	{
		Sum+=s[u];
		u=next[u];
	}
	
	printf("%I64d\n",Sum);
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
