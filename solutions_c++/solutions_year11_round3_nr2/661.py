#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

int L, C, T, t, N, lic[1000005], item[1000005];
int n[1000005], nN;
__int64 ans;
int main()
{
	freopen("input.txt", "r" ,stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d",&T);
	for(int tt=1; tt<=T; tt++){
		scanf("%d %d %d %d",&L,&t,&N,&C);
		int i, j;
		for(i = 1; i <= C; i++) scanf("%d", &lic[i]);
		for(i = 1, j = 1; i <= N; i++, j++){
			if(j > C) j -= C;
			item[i] = lic[j];
		}

		ans = 0;
		for(i = 1; i <= N; i++)
		{
			// if cannot usable, continue;
			if(ans + item[i]*2 <= t){
				ans += item[i]*2;
				continue;
			}
			break;
		}
		// can use booster from i ! 
		if(i != N+1){
			n[1] = item[i] - (t - ans)/2;
			nN = 1;
			ans += item[i] * 2;
			for(i = i + 1; i <= N; i++){
				ans += item[i]*2;
				nN++;
				n[nN] = item[i];
			}

			std::sort(n+1, n+nN+1);
			for(i = nN; i >= 1 && L; i--, L--)
				ans -= n[i];

		}
		printf("Case #%d: %I64d\n", tt, ans);
	}
	return 0;
}