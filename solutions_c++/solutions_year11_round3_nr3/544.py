#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <math.h>
using namespace std;

const int MAX = 205;

int N, L, H, a[105];

int go()
{
	for(int i = L; i <= H; i++)
	{
		for(int j = 0; j < N; j++)
		{
			if((i % a[j]) && (a[j] % i))  break;
			if(j == N - 1)  return i;
		}
	}
	return 0;
}

int main()
{
	freopen("d:\\Desktop\\GCJ\\C-small-attempt0.in", "r", stdin);
	freopen("d:\\Desktop\\GCJ\\C-small-attempt0.out", "w", stdout);
	int T, c = 0;
	scanf("%d", &T);
	while(T--)
	{
		printf("Case #%d: ", ++c);
		scanf("%d%d%d", &N, &L, &H);
		for(int i = 0; i < N; i++)
			scanf("%d", &a[i]);
		int ans = go();
		if(ans == 0)  printf("NO\n");
		else  printf("%d\n", ans);
	}
}