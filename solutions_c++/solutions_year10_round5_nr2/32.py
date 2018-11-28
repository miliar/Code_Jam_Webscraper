#include <stdio.h>
#include <algorithm>
#include <queue>
using namespace std;
#define N 110
#define K 100010
#define M 1000000000
#define I __int64
int m[N], p;
I v[K];
struct T
{
	int i;
	I h, d;
};
bool operator <(T a, T b) { return a.d*p-a.h>b.d*p-b.h; }
priority_queue <T> q;
int main()
{
	int i, n, t, ts;
	I l;
	T a, b;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%I64d%d", &l, &n), i=0; i<n; scanf("%d", &m[i]), i++);
		printf("Case #%d: ", t+1);
		sort(m, m+n);
		p=m[n-1];
		for(; !q.empty(); q.pop());
		for(v[0]=0, i=1; i<K; v[i]=M, v[i]*=M, i++);
		a.i=0;
		a.h=0;
		a.d=0;
		q.push(a);
		for(; !q.empty(); )
		{
			a=q.top(); q.pop();
			if(v[a.i]<a.d*p-a.h) continue;
			if(a.i==l%p) break;
			for(i=0; i<n-1; i++)
			{
				b.i=(a.i+m[i])%p;
				b.d=a.d+1;
				b.h=a.h+m[i];
				if(b.d*p-b.h<v[b.i])
				{
					v[b.i]=b.d*p-b.h;
					q.push(b);
				}
			}
		}
		if(a.i==l%p) printf("%I64d\n", a.d+(l-a.h)/p);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}