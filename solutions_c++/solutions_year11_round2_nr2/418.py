#include <iostream>
using namespace std;
#define maxnum 300

double D;
int C;
int P[maxnum];
int V[maxnum];

int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		int C,D;
		cin >> C >> D;
		for(int j=0;j<C;j++)
		{
			cin >> P[j] >> V[j];
		}
		double minimum = 0, maximum = 1e15, mid;
		while(1)
		{
			double leftbound = -1e20;
			bool flag = true;
			mid = (minimum + maximum) / 2;
			if(mid==minimum||mid==maximum) break;
			for(int j=0;j<C;j++)
			{
				double l = P[j] - mid;
				if(l < leftbound + D)
					l = leftbound + D;
				double r = l + D * (V[j] - 1.0);
				if(r - P[j] > mid)
				{
					flag = false;
					break;
				}
				leftbound = r;
			}
			if(flag)
				maximum = mid;
			else minimum = mid;
		}
		printf("Case #%d: %.7lf\n",i,mid);
	}
}
