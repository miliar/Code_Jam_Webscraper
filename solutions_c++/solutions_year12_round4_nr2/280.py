#include <iostream>
#include <cmath>
using namespace std;

struct Circle
{
	double x,y;
	double r;
	int index;
};

Circle c[1000];

bool operator<(Circle a, Circle b)
{
	return a.r > b.r;
}

bool cmp(Circle a, Circle b)
{
	return a.index < b.index;
}

int main()
{
	int T;
	cin >> T;
	for(int k=1;k<=T;k++)
	{
		int N,W,L;
		cin >> N >> L >> W;
		for(int i=0;i<N;i++)
		{
			cin >> c[i].r;
			c[i].index = i;
		}
		sort(c,c+N);
		bool ltr = true;
		double tempx = 0;
		c[0].x = 0;
		c[0].y = 0;
		for(int i=1;i<N;i++)
		{
			if(ltr)
			{
				c[i].x = c[i-1].x + c[i-1].r + c[i].r;
				if(c[i].x > L)
				{
					ltr = false;
					c[i].x = L;
				}
			}
			else
			{
				c[i].x = c[i-1].x - c[i-1].r - c[i].r;
				if(c[i].x < 0)
				{
					ltr = true;
					c[i].x = 0;
				}
			}
			double tempy = 0;
			for(int j=0;j<i;j++)
			{
				if(fabs(c[i].x-c[j].x)>=c[i].r+c[j].r)
					continue;
				double ty = sqrt((c[i].r + c[j].r)*(c[i].r + c[j].r) - (c[i].x - c[j].x) *  (c[i].x - c[j].x)) + c[j].y;
				if(ty > tempy)
					tempy = ty+0.1;
			}
			c[i].y = tempy;
		}
		sort(c,c+N,cmp);
		cout << "Case #" << k << ":";
		for(int i=0;i<N;i++)
		{
			if(c[i].y > W)
				printf("ERROR\n");
			for(int j=i+1;j<N;j++)
			{
				if((c[i].x - c[j].x) * (c[i].x - c[j].x) + (c[i].y - c[j].y) * (c[i].y - c[j].y) < (c[i].r + c[j].r)*(c[i].r + c[j].r))
					printf("ERROR @ %d %d\n",i+1,j+1);
			}
		}
		for(int i=0;i<N;i++)
		{
			//cout << " " << c[i].x << " " << c[i].y;
			printf(" %.3lf %.3lf",c[i].x,c[i].y);
		}
		cout << endl;
	}
}
