#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#define maxn (1005)
using namespace std;

int C,R,N,test,next[maxn][31],a[maxn];
long long F[maxn][31];

int main()
{
	//freopen("i.txt","r",stdin);
	int cnt=1;
	for (scanf("%d",&test);test--;++cnt)
	{
		scanf("%d%d%d",&R,&C,&N);
		for (int i=0;i<N;++i) scanf("%d",&a[i]);
		for (int i=0;i<N;++i)
		{
			long long now=0;
			int tmp=i;
			for (int j=0;j<N && now+a[tmp]<=C;++j,now+=a[tmp],tmp=(tmp+1)%N);
			next[i][0]=tmp;
			F[i][0]=now;
		}
		long long now=2;
		for (int i=1;now<=R;++i,now<<=1)
		{
			for (int j=0;j<N;++j) 
			{
				next[j][i]=next[next[j][i-1]][i-1];
				F[j][i]=F[j][i-1]+F[next[j][i-1]][i-1];
			}
		}
		printf("Case #%d: ",cnt);
		long long ans=0;
		for (int i=0,tmp=0;R;R>>=1,tmp++)
		{
			if (R&1)
			{
				ans+=F[i][tmp];
				i=next[i][tmp];
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}
