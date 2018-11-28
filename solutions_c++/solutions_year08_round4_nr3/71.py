#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
using namespace std;
struct point
{
	double a,b,c,r;
};
vector<point> v;
int m;
double res(const point& p)
{
	double res = -1;
	for(int i = 0; i < m; i++)
		res = max(res, (fabs(p.a - v[i].a) + fabs(p.c - v[i].c) + fabs(p.b - v[i].b)) / v[i].r);
	return res;
}
int main()
{
	freopen("../../google.in", "r", stdin);
	freopen("../../google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		//int m;
		cin >> m;
		v.clear();
		v.resize(m);

		
		point p;
		p.a = 0.0;
		p.b = 0.0;
		p.c = 0.0;
		for(int i = 0; i < m ;i++)
		{
			cin >> v[i].a >> v[i].b >> v[i].c >> v[i].r;
			p.a += v[i].a;
			p.b += v[i].b;
			p.c += v[i].c;
		}
		p.a /= (double)m;
		p.b /= (double)m;
		p.c /= (double)m;
		double step = 100000000.0;
		double maxm = res(p);
		while(step > epsilon)
		{
			p.a -= step;
			double temp = res(p);
			if(temp - maxm > -epsilon)
			{
				p.a += 2 * step;
				temp = res(p);
				if(temp - maxm > -epsilon)
				{
					p.a -= step;
					p.b -= step;
					temp = res(p);
					if(temp - maxm > -epsilon)
					{
						p.b += 2 * step;
						temp = res(p);
						if(temp - maxm > -epsilon)
						{
							p.b -= step;
							p.c -= step;
							temp = res(p);
							if(temp - maxm > -epsilon)
							{
								p.c += 2 * step;
								temp = res(p);
								if(temp - maxm > -epsilon)
								{
									p.c -= step;
									step /= 2.0;
								}
								else
									maxm = temp;
							}
							else
								maxm = temp;
						}
						else
							maxm = temp;
					}
					else
						maxm = temp;
				}
				else
					maxm = temp;
			}
			else
				maxm = temp;
		}
		printf("%.6lf\n", maxm);
	}
	return 0;
}
