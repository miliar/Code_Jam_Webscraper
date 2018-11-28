#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <cstring>
#include <set>
#include <climits>
#include <ctime>
#include <cstdlib>

using namespace std;

#define LL long long
#define mp make_pair
#define F first
#define S second

int rai[10];
double res[10][2];

double sqr(double a)
{
	return a*a;
}

bool collide(int i, int j)
{
	double dist = sqrt(sqr(res[i][0]-res[j][0]) + sqr(res[i][1]-res[j][1]));
	return dist < rai[i]+rai[j];
}

int main()
{
	int t, n, w, l;
	srand(time(NULL));
	scanf("%d", &t);
	
	for (int q = 1; q<= t; ++q)
	{
		printf("Case #%d:", q);
		scanf("%d%d%d", &n, &w, &l);
		for (int i = 0 ; i< n; ++i)
			scanf("%d", &rai[i]);
		
		bool good = 0;
		while (!good)
		{
			for (int i = 0; i < n; ++i)
			{
				res[i][0] = (double)rand()/RAND_MAX*w;
				res[i][1] = (double)rand()/RAND_MAX*l;
			}
			
			good = 1;
			for (int i = 0; i < n && good; ++i)
			{
				for (int j = i+1; j < n; ++j)
				{
					if (collide(i, j))
					{
						good = 0;
						break;
					}
				}
			}
		}
		
		for (int i = 0; i < n; ++i)
			printf(" %lf %lf", res[i][0], res[i][1]);
		printf("\n");
	}
	
	return 0;
}

