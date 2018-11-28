#include<cstdio>
#include<iostream>
#include<cstring>
#define maxn 10009
int d[maxn],l[maxn];
int f[maxn];
using namespace std;
int main()
{
	int runs,N,D;
	cin>>runs;
	for (int run=1;run<=runs;run++)
	{
		cin>>N;
		for (int i=0;i<N;i++) cin>>d[i]>>l[i];
		cin>>D;d[N]=D;l[N]=0;
		memset(f,-1,sizeof(f));
		printf("Case #%d: ",run);
		f[0]=d[0];
		for (int i=0;i<=N;i++)
		{
			for (int j=i+1;j<=N;j++)
				if (d[i]+f[i]>=d[j])
				{
					if (f[j]<min(d[j]-d[i],l[j]))
						f[j]=min(d[j]-d[i],l[j]);
				}
		}
		if (f[N]==-1) puts("NO");
		else puts("YES");
	}
	return 0;
}

