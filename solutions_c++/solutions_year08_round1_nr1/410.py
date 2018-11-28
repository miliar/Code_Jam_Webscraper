#include <cstdio>
#include <algorithm>

using namespace std;

struct v1
{
	long long v;
	bool operator < (const v1& a) const
	{
		return v < a.v;
	}
};
struct v2
{
	long long v;
	bool operator < (const v2& a) const
	{
		return v > a.v;
	}
};

v1 V1[1000];
v2 V2[1000];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int i, r, n;
	int cs = 0;
	scanf("%d", &r);
	while(r--)
	{
		scanf("%d", &n);
		for(i = 0; i < n; ++i)
			scanf("%I64d", &V1[i].v);
		for(i = 0; i < n; ++i)
			scanf("%I64d", &V2[i].v);
		sort(V1, V1 + n);
		sort(V2, V2 + n);
		__int64 ret = 0;
		for(i = 0; i < n; ++i)
			ret += V1[i].v * V2[i].v;
		printf("Case #%d: %I64d\n", ++cs, ret);

	}

}