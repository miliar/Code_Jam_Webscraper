#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>

using namespace std;

int min(int a, int b)
{
	return a < b ? a : b;
}

int max(int a, int b)
{
	return a > b ? a : b;
}

int main()
{
	int i, j, k;
	int T, cc = 0;
	
	scanf("%d", &T);
	while(T --)
	{
		int N, S, P, t[128];
		scanf("%d %d %d", &N, &S, &P);
		int Ans = 0;
		for(i = 0; i < N; i ++)
		{
			scanf("%d", &t[i]);
			if(t[i] > P*3-3)Ans ++;
			if(t[i] <= P*3-3 && t[i] >= P*3-4 && S > 0 && t[i] >= 2)
			{
				S --;
				Ans ++;
			}
		}
		printf("Case #%d: %d\n", ++cc, Ans);
	}
	return 0;
}
