#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

struct mydata
{
	int p;
	int v;
	bool operator<(const mydata &r) const
	{
		return p < r.p;
	}
}data[210];

int n;
int d;

double time;

bool solve()
{
	int i;
	double l = -1e40;
	for(i = 0;i < n;i++)
	{
		double t = data[i].p - time;
		t = max(t , l);
		t += d * (data[i].v - 1);
		if(t > data[i].p + time) return false;
		l = t + d;
	}
	return true;
}

double besearch()
{
	double left = 0 , right = 1e13;
	while(right - left > 1e-8)
	{
		time = (left + right) / 2;
		if(solve()) right = time;
		else left = time;
	}
	return left;
}

int main()
{
//	freopen("1.txt" , "r" , stdin);
//	freopen("2.txt" , "w" , stdout);
	int t;
	int ii = 0;
	scanf("%d" , &t);
	while(t--)
	{
		ii++;
		scanf("%d%d" , &n , &d);
		int i;
		for(i = 0;i < n;i++)
		{
			scanf("%d%d" , &data[i].p , &data[i].v);
		}
		sort(data , data + n);
		printf("Case #%d: %.12lf\n" , ii , besearch());
	}
	return 0;
}