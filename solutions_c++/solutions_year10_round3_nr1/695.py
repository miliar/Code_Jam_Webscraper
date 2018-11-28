#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

const int MAX = 100000 + 100;

int a[MAX],b[MAX];
long long change;

void Merge(int p,int q,int r)
{
	int i,j = 0;
	int beginA = p,endA = q,beginB = q + 1,endB = r;

	while(beginA <= endA&&beginB <= endB)
	{
		if(a[beginA] <= a[beginB])
			b[j++] = a[beginA++];
		else
		{
			b[j++] = a[beginB++];
			change += q - beginA + 1;
		}
	}
	while(beginA <= endA)
		b[j++] = a[beginA++];
	while(beginB <= endB)
		b[j++] = a[beginB++];
	for(i = 0;i < j;i++)
		a[p+i] = b[i];
}

void Mergesort(int begin,int end)
{
	if(begin < end)
	{
		int mid = (begin + end)/2;
		Mergesort(begin,mid);
		Mergesort(mid + 1,end);
		Merge(begin,mid,end);
	}
}

struct data
{
    int a, b;
    bool operator < (const data& t) const
    {
        return a < t.a;
    }
};

int main(void)
{
    freopen("A.out", "w", stdout);
	int tt;
    scanf("%d", &tt);
    for (int ca = 0; ca < tt; ++ca)
    {
        int n;
        scanf("%d",&n);
        vector<data> in(n);
        for (int i = 0; i < n; ++i) scanf("%d %d", &in[i].a, &in[i].b);
        sort(in.begin(), in.end());
        change = 0;
        for(int i = 0;i < n;i++)
            a[i] = in[i].b;
        Mergesort(0,n - 1);
        printf("Case #%d: %I64d\n",ca+1,change);
    }
	return 0;
}
