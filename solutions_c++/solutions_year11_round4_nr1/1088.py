#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

struct qu {
	int b;
	int e;
	int w;
}node[3000], next[3000];

bool cmp(qu a, qu b)
{
	return a.b < b.b;
}

bool cmp2(qu a, qu b)
{
	return a.w < b.w;
}

int main()
{
	int cas, T;
	scanf("%d", &T);
	for(cas = 1; cas <= T; cas ++)
	{
		int i, j, k;
		int x, s, r, t, n;
		
		scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
		
		double speed = s;
		
		for(i = 0; i < n; i ++)
		{
			scanf("%d %d %d", &node[i].b, &node[i].e, &node[i].w);
		}
		
		sort(node, node+n, cmp);
		int cnt = 0, ss = 0;
		
		for(i = 0; i < n; i ++)
		{
			if(ss < node[i].b)
			{
				next[cnt].b = ss;
				next[cnt].e = node[i].b;
				next[cnt].w = 0;
				cnt ++;
			}
			next[cnt ++] = node[i];
			ss = node[i].e;
		}
		if(ss < x)
		{
			next[cnt].b = ss;
			next[cnt].e = x;
			next[cnt].w = 0;
			cnt ++;
		}
		sort(next, next+cnt, cmp2);
		
		double used = 0, sss;
		double ans = 0;
		
		for(i = 0; i < cnt; i ++)
		{
			sss = (double)(next[i].e-next[i].b)/(double)(next[i].w+r);
			//printf("%d %d %lf %lf %lf\n", next[i].b, next[i].e, sss, used, ans);
			if(sss < t-used)
			{
				used += sss;
				ans += sss;
			}
			else {
				ans += t-used;
				double dis = (double)(next[i].e-next[i].b) - (double)(next[i].w+r)*(t-used);
				used = t;
				ans += dis/(next[i].w+s);
			}
		}
		printf("Case #%d: %.9lf\n", cas, ans);
	}
	return 0;
}
