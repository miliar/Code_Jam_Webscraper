#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
using namespace std;

struct asdf
{
	int odl[110];
	int mp;
};

void solve(int num)
{
	asdf b, o;
	o.mp = 1;
	b.mp = 1;
	int n, xd[110];
	scanf("%d", &n);
	for(int i = 1; i <= n; i++)
	{
		o.odl[i] = 0;
		b.odl[i] = 0;	
		int temp;
		char zn;
		scanf(" %c %d", &zn, &temp);
		if(zn == 'O')
		{
			xd[i] = 0;
			o.odl[i] = abs(temp - o.mp);
			b.odl[i] = 0;
			o.mp = temp;
//			printf("O - odl %d %d\n", i ,o.odl[i]);
			continue;
		}
		if(zn == 'B')
		{
			xd[i] = 1;
			b.odl[i] = abs(temp - b.mp);
			o.odl[i] = 0;
//			printf("B - odl %d %d\n", i ,b.odl[i]);
			b.mp = temp;
			continue;
		}
	}
	int ot = 0, bt = 0, rq = 0;
	for(int i = 1; i <= n; i++)
	{
//		printf("%d %d\n", ot, bt);
		if(xd[i])
		{
			if(rq == 10)
			{
				bt += b.odl[i]+1;
				continue;
			}
			if(rq == 20)
			{
				if(ot >= bt+b.odl[i])
				{
					bt = ot+1;
					rq = 10;
					continue;
				}
				if(ot < bt+b.odl[i])
				{
					bt += b.odl[i]+1;
					rq = 10;
					continue;
				}
			}
			if(!rq)
			{
				bt = b.odl[i]+1;
				rq = 10;
				continue;
			}
		}
		if(!xd[i])
		{
			if(rq == 10)
			{
				if(bt >= ot + o.odl[i])
				{
					ot = bt+1;
					rq = 20;
					continue;
				}
				if(bt < ot + o.odl[i])
				{
					ot += o.odl[i]+1;
					rq = 20;
					continue;
				}
			}
			if(rq == 20)
			{
				ot += o.odl[i]+1;
				continue;
			}
			if(!rq)
			{	
				ot = o.odl[i]+1;
				rq = 20;
				continue;
			}
		}
	}
	printf("Case #%d: %d\n", num, max(ot, bt));
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; i++) solve(i);
}
