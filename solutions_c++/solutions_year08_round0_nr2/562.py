#include<iostream>
#include<string.h>
#include<queue>

using namespace std;

struct pp
{
	friend bool operator <( pp a, pp b)
	{
		if(a.start != b.start)
			return a.start > b.start;
		else
			return a.arive > b.arive;
	}
	int start,arive;
	int d;//1 a->b  2 b->a
}now,car;
priority_queue<pp>pq,A,B;
int a,b;
char in[50];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int i,j,n,t,na,nb;
	scanf("%d",&n);
	for(j = 1; j <= n; j ++)
	{
		a = 0;
		b = 0;
		while( !pq.empty())
			pq.pop();
		while( ! A.empty())
			A.pop();
		while( ! B.empty())
			B.pop();
		scanf("%d",&t);
		scanf("%d %d",&na,&nb);
		for(i = 0; i < na; i ++)
		{
			scanf("%s",in);
			now.start = ((in[0]-'0')*10+in[1]-'0')*60+(in[3]-'0')*10+in[4]-'0';
			scanf("%s",in);
			now.arive = ((in[0]-'0')*10+in[1]-'0')*60+(in[3]-'0')*10+in[4]-'0';
			now.d = 1;
			pq.push(now);
		}
		for(i = 0 ; i < nb; i ++)
		{
			scanf("%s",in);
			now.start = ((in[0]-'0')*10+in[1]-'0')*60+(in[3]-'0')*10+in[4]-'0';
			scanf("%s",in);
			now.arive = ((in[0]-'0')*10+in[1]-'0')*60+(in[3]-'0')*10+in[4]-'0';
			now.d = 2;
			pq.push(now);
		}
		int leap = 0;
		while( !pq.empty())
		{
			now = pq.top();
			pq.pop();
			leap = 0;
			if(now.d == 1)
			{
				while( !A.empty())
				{
					car = A.top();
					if(car.start <= now.start)
					{
						A.pop();
						car.start = now.arive+t;
						B.push(car);
						leap = 1;
					}
					break;
				}
				if(leap == 0)
				{
					a ++;
					car.start = now.arive+t;
					B.push(car);
				}
			}
			else
			{
				while( !B.empty())
				{
					car = B.top();
					if(car.start <= now.start)
					{
						B.pop();
						car.start = now.arive+t;
						A.push(car);
						leap = 1;
					}
					break;
				}
				if(leap == 0)
				{
					b ++;
					car.start = now.arive+t;
					A.push(car);
				}
			}
		}
		printf("Case #%d: %d %d\n",j,a,b);
	}
	return 0;
}