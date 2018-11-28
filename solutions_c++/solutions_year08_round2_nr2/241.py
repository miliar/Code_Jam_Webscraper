/*#include<iostream>
#include<algorithm>

using namespace std;

struct pp
{
	long long x,y;
}p[100005];
long long T,n,m,a,b,c,d,x0,y0;
bool comp(pp A, pp B)
{
	if(A.x != B.x)
		return A.x  < B.x;
	else
		return A.y < B.y;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,i,j,k;
	scanf("%lld",&T);
	for(t = 1; t <= T; t ++)
	{
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n,&a,&b,&c,&d,&x0,&y0,&m);
		p[0].x = x0;	p[0].y = y0;
		a %= m;
		b %= m;
		for(i = 1; i < n; i ++)
		{
			p[i].x = (a*p[i-1].x+b)%m;
			p[i].y = (c*p[i-1].y+d)%m;
		}
		long long ans = 0;
		long long x,y;
		for(i = 0; i < n; i ++)
		{
			for(j = i+1; j < n; j ++)
			{
				for(k = j+1; k < n; k ++)
				{
					if(((p[i].x+p[j].x+p[k].x)%3 == 0)  && ((p[i].y+p[j].y+p[k].y)%3 == 0) )
						ans ++;
				}
			}
		}

		printf("Case #%d: %lld\n",t,ans);
	}
	return 0;
}*/

#include<iostream>
#include<cmath>

using namespace std;

int pre[1005],rank[1005],num;

void makeset(int x)
{
	pre[x] = -1;
	rank[x] = 0;
}
int find(int x)
{
	int r = x;
	while(pre[r] != -1)
		r = pre[r];
	while(x != r)
	{
		int q = pre[x];
		pre[x] = r;
		x = q;
	}
	return r;
}
void unionone(int a, int b)
{
	int t1 = find(a);
	int t2 = find(b);
	if(rank[t1] > rank[t2])
	{
		pre[t2] = t1;
	}
	else
	{
		pre[t1] = t2;
	}
	if(rank[t1] == rank[t2])
		rank[t2] ++;
}
int c,a,b,p,pr;
int prim[1005],use[1005] = {0};
void init()
{
	int i,j;
	for(i = 2; i < sqrt(1005*1.0); i ++)
	{
		if(use[i] == 0)
		{
			for(j = i*i; j < 1005; j += i)
				use[j] = 1;
		}
	}
	pr = 0;
	for(i = 2; i < 1005; i ++)
		if(use[i] == 0)
			prim[pr ++] = i;
}
int main()
{	
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int i,j,t;
	init();
	scanf("%d",&c);
	for(t = 1; t <= c; t ++)
	{
		scanf("%d %d %d",&a,&b,&p);
		num = b-a+1;
		for(i = a; i <= b; i ++)
			makeset(i);
		for(i = 0; i < 1005 ; i ++)
		{
			if(prim[i] >= p)
				break;
			if(prim[i] > b)
				break;
		}
		if(prim[i] > b)
		{
			printf("%d\n",num);
			continue;
		}
		int start = i;
		for(i = a; i <= b; i++)
		{
			for(j = i+1; j <= b; j ++)
			{
				if(find(i) != find(j))
				{
					for(int l = start; prim[l] <= i && l < pr; l ++)
					{
						if((i%prim[l] == 0) && (j%prim[l]) == 0)
						{
							num -= 1;
							unionone(i,j);
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: %d\n",t,num);
	}
	return 0;
}