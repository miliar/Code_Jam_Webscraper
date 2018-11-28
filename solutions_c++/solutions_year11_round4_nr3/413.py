#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

#define tr(i,c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define x first
#define y second

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef long long ll;

#define MAX 1000100

int q, p[MAX], pr[MAX];

void test()
{
	long long n, res = 1;
	scanf("%lld", &n);
	if(n == 1)
	{
		printf("0\n");
		return;
	}
	for(int i = 0; i < q && 1LL * p[i] * p[i] * p[i] <= n; i++)
	{
		int pw = 0;
		long long temp = 1;
		while(temp*p[i] <= n)
		{
			pw++;
			temp *= p[i];
		}
		res += pw-1;
	}
	int low = -1, high = q;
	while(low+1 < high)
	{
		int mid = (low+high) / 2;
		if(1LL * p[mid] * p[mid] <= n) low = mid;
		else high = mid;
	}
	int temp = high;
	low = -1;
	high = q;
	while(low+1 < high)
	{
		int mid = (low+high) / 2;
		if(1LL * p[mid]  *p[mid] * p[mid] <= n) low = mid;
		else high = mid;
	}
	printf("%lld\n", res+temp-high);
}

int main()
{
	for(int i = 2; i < MAX; i++) pr[i] = 1;
	for(int i = 2; i*i < MAX; i++) if(pr[i])
		for(int j = i*i; j < MAX; j += i) pr[j] = 0;
	for(int i = 2; i < MAX; i++) if(pr[i]) p[q++] = i;
	int tt;
	scanf("%d", &tt);
	for(int i = 1; i <= tt; i++)
	{
		printf("Case #%d: ", i);
		test();
	}
}
