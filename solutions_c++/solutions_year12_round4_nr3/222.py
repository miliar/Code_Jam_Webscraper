#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


#define maxn 2222


int n;
bool wrong;
int h[maxn], r[maxn];

int dv(long long a, int b)
{
	if(a%b==0) return a/b;
	if(a > 0) return a/b;
	return -((-a+b-1)/b);
}

int get(int ax, int bx, int cx)
{
	int ay = h[ax], by = h[bx];
	long long res = 1LL * (by-ay) * cx + 1LL * ay*bx - 1LL*ax*by;
	//printf("get = %lld / %d\n", res, bx-ax);
	return dv(res,bx-ax);
}

void upd(int &x, int &y, int z)
{
	if(x < z) x = z;
	else
	{
		y = x;
		x = z;
	}
}

void rec(int low, int high)
{
	//printf("low = %d, high = %d\n", low, high);
	if(low > high) return;
	vector<int> mid;
	int cur = low+1;
	while(cur < high)
	{
		//printf("cur = %d\n", cur);
		mid.push_back(cur);
		cur = r[cur];
	}
	if(cur > high)
	{
		wrong = 1;
		return;
	}
	int x = low, y = high;
	int s = mid.size();
	s--;
	for( int i = s; i >= 0; i--)
	{
		h[mid[i]] = get(x,y,mid[i]);
		if(i == s) h[mid[i]]--;
		upd(x,y,mid[i]);
		rec(x, y);
	}
}

void test()
{
	scanf("%d", &n);
	for(int i = 1; i < n; i++)
	{
		scanf("%d", &r[i]);
	}
	wrong = 0;
	h[0] = 0;
	h[n] = 0;
	rec(0, n);
	if(wrong) printf("Impossible\n");
	else
	{
		int mm = 0;
		for(int i = 1; i <= n; i++) if(h[i] < mm) mm = h[i];
		for(int i = 1; i <= n; i++) printf("%d ", h[i]-mm);
		printf("\n");
	}
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for(int i = 1; i <= tt; i++)
	{
		printf("Case #%d: ", i);
		test();
	}
	return 0;
}
