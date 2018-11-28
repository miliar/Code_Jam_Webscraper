#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
const int MAXN = 1000;
const int MAXM = 10000 + 10;
struct WIRE
{
	int x, y;
};
const int M = 10000 + 10;
int n;
WIRE a[MAXN];
int s[MAXM];
bool operator<(const WIRE &w1, const WIRE &w2)
{
	return (w1.x < w2.x);
}
int Lowbit(int t) 
{
	return t & ( t ^ ( t - 1 ) ); 
} 
int Sum(int end) 
{ 
	int sum = 0; 
	while(end > 0) 
	{ 
		sum += s[end]; 
		end -= Lowbit(end); 
	} 
	return sum; 
} 
void plus(int pos, int num) 
{ 
	while(pos <= M) 
	{ 
		s[pos] += num; 
		pos += Lowbit(pos); 
	} 
} 
int main()
{
	int cases;
	scanf("%d", &cases);
	for (int k = 1; k <= cases; ++k)
	{
		printf("Case #%d: ", k);
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%d%d", &a[i].x, &a[i].y);
		sort(a, a + n);
		int ans = 0;
		memset(s, 0, sizeof(s));
		for (int i = n - 1; i >= 0; --i)
		{
			ans += Sum(a[i].y);
			plus(a[i].y, 1);
		}
		printf("%d\n", ans);
	}
	return 0;
}
