#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int N,T;
int A[1005];
int Case;
int main()
{
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		int ans = 0;
		scanf("%d",&N);
		printf("Case #%d: ",++Case);
		int res = 0;
		for(int i = 1;i <= N;++i)
		{
			scanf("%d",&A[i]);
			res ^= A[i];
		}
		if(res != 0)	printf("NO\n");
		else
		{
			sort(A+1,A+N+1);
			for(int i = N;i > 1;--i)
				ans += A[i];
			printf("%d\n",ans);
		}
	}
}