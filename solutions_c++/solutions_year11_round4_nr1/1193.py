#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
using namespace std;

struct mydata
{
	int s , e;
	int speed;
	bool operator<(const mydata &r) const
	{
		return s < r.s;
	}
}data[2000];

bool cmp(mydata a , mydata b)
{
	return a.speed < b.speed;
}

int main()
{
//	freopen("1.txt" , "r" , stdin);
//	freopen("2.txt" , "w" , stdout);

	int t;
	scanf("%d" , &t);
	int ii = 0;
	while(t--)
	{
		ii++;
		int x , s , r , t , n;
		scanf("%d%d%d%d%d" , &x , &s , &r , &t , &n);
		int i;
		int total = x;
		double res = t;
		printf("Case #%d: " , ii);
		for(i = 0;i < n;i++)
		{
			scanf("%d%d%d" , &data[i].s , &data[i].e , &data[i].speed);
			total -= data[i].e - data[i].s;
		}
		double ret = 0;
		if(total >= res * r)
		{
			ret += (double)res;
			total -= t * r;
			ret += (double) total / s;
			for(i = 0;i < n;i++)
			{
				ret += (double)(data[i].e - data[i].s) / (data[i].speed + s);
			}
			printf("%.12lf\n" , ret);
		}
		else
		{
			ret += (double) total / r;
			res -= (double) total / r;
			sort(data , data + n , cmp);
			for(i = 0;i < n;i++)
			{
				if((data[i].e - data[i].s) >= res * (data[i].speed + r))
				{
					ret += res;
					ret += ((data[i].e - data[i].s) - res * (data[i].speed + r)) / (data[i].speed + s);
					break;
				}
				else
				{
					ret += (data[i].e - data[i].s) / (double)(data[i].speed + r);
					res -= (data[i].e - data[i].s) / (double)(data[i].speed + r);
				}
			}
			for(i++;i < n;i++)
			{
				ret += (double)(data[i].e - data[i].s) / (data[i].speed + s);
			}
			printf("%.12lf\n" , ret);
		}
	}

	return 0;
}