#include<stdio.h>
#include<algorithm>
#include<string>
using namespace std;

const int maxn = 300;

int N;
char S1[maxn],S[maxn];
bool cmpf(const int i,const int j)
{
	return S[i] > S[j];
}

int main()
{
	freopen("next.in","r",stdin);
	freopen("next.out","w",stdout);
	scanf("%d\n",&N);
	for(int i = 1;i <= N; ++i)
	{
		int x = i;
		memset(S,0,sizeof(S));
		scanf("%s",S + 1);
		int N = strlen(S + 1);
		for(int i = 1;i <= N; ++i) S1[i] = S[i];
		if (next_permutation(S + 1,S + N + 1))
		{
			printf("Case #%d: %s\n",x,S + 1);
		}
		else
		{
			for(int i = 1;i <= N; ++i) S[i] = S1[i];
			int cur = 0;
			S[0] = 100;
			for(int i = N; i; --i)
			{
//					printf("%d %d %d\n",S[i] < S[cur],S[i],S[cur]);
					if (S[i] < S[cur] && S[i] != '0') cur = i;
			}
//			printf("%d\n",cur);
			swap(S[1],S[cur]);
			sort(S + 2,S + N + 1);
/*			printf("%s\n",S + 2);
			next_permutation(S + 2,S + N + 1);
*/			N++;
			for(int i = N;i >= 2; --i) S[i] = S[i - 1];
			S[2] = '0';
			printf("Case #%d: %s\n",x,S + 1);
		}
	}

	return 0;
}



