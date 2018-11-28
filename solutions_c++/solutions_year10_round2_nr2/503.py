#include <iostream>
#include <string>
#include <set>
#include <math.h>
#include <vector>
#include <algorithm>
using namespace std;

const int MAX = 100;

int N, K, B, T;
int x[MAX], v[MAX];
double t[MAX];

int go()
{
	for(int i = 1; i <= N; i++)  t[i] = (B - x[N + 1 - i]) * 1.0 / v[N + 1 - i];
	int j = 1;
	int res = 0;
	for(int i = 1; i <= K; i++)
	{
		while(j <= N && t[j] > T)  j++;
		if(j > N)  return -1;
		res += j - i;
		j++;
	}
	return res;
}

int main()
{
	freopen("d:\\B-large.in", "r", stdin);
	freopen("d:\\B-large.out", "w", stdout);

	int C, c = 0;
	scanf("%d", &C);
	while(C--)
	{
		scanf("%d%d%d%d", &N, &K, &B, &T);
		for(int i = 1; i <= N; i++)  scanf("%d", &x[i]);
		for(int i = 1; i <= N; i++)  scanf("%d", &v[i]);
		int flag = go();
		printf("Case #%d: ", ++c);
		if(flag == -1)  printf("IMPOSSIBLE\n");
		else  printf("%d\n", flag);	
	}
}