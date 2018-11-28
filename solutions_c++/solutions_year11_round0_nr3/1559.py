#include <iostream>
#include <cstdio>

using namespace std;

int pow[20];

int T, N;
int C[2000];
int i, j, k;
int ans;

int t, xt;

int calc(int m)
{
	int x, y, w;
	int ans = 0;
	int tmp1, tmp2;
	int ans1, ans2;
	for( x = 1; x < m; x++)
	{
		//printf("!");
		tmp2 = 0;
		ans2 = 0;
		w = x;
		for( y = 0; y < N; y ++, w/=2)
		{
			if(w%2==1)
			{
				tmp2 = tmp2^C[y];
				ans2 += C[y];
			}
			
		}
		if(tmp2 ^ xt == tmp2)
		{
			ans1 = t - ans2;
			ans = ans < ans1 ? ans1 : ans;
		}
	}
	return ans;
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	pow[0] = 1;
	for(j = 1; j < 20; j++)
		pow[j] = pow[j-1] * 2;
	scanf("%d",&T);
	for( k = 1; k <= T; k ++ )
	{
		scanf("%d",&N);
		t=xt = 0;
		ans = 99999999;
		for( i = 0; i < N; i ++ )
		{
			scanf("%d",&C[i]);
			t += C[i];
			xt = xt ^ C[i];
			ans = ans <= C[i] ? ans : C[i];
		}
		//ans = calc(pow[N]);
		

		printf("Case #%d: ",k);
		if(xt != 0) printf("NO\n");
		else printf("%d\n",t - ans);
	}
	return 0;
}