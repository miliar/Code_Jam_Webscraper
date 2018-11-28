#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#define PB push_back
using namespace std;

void solve(int nr)
{
	int n, s, p, a, wyn = 0;
	vector<int> v;
	scanf("%d%d%d", &n, &s, &p);
	for(int i = 0; i < n; i++)
	{
		scanf("%d", &a);
		v.PB(a);
	}
	for(int i = 0; i < n; i++)
	{
		int x = v[i]/3;
		if(x >= p || (x*3 < v[i] && x == p-1))wyn++;
		else if(s && (p+p-1+p-2 == v[i] || p+p+p-4 == v[i]) && p-2 >= 0)
		{
			wyn++;
			s--;
		}
	}
	printf("Case #%d: %d\n", nr, wyn);
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)solve(i);
}
