#include <iostream>
#include <cmath>
using namespace std;
#define tiao system("pause")

int c;
int x[111],y[111],r[111];
int n;

double dist(int x, int y, int xx, int yy)
{
	return sqrt((x-xx)*(x-xx) + (y-yy)*(y-yy));
}

double get(int a, int b, int c)
{
	return max((dist(x[a],y[a], x[b],y[b]) + r[a] + r[b]) / 2.0, (double)r[c]);
}

int main(void)
{
	int i,j,k,ci,cici,cicici;
	
	freopen("D-small-attempt2.in","r",stdin);
	freopen("D-small-attempt2.out","w",stdout);
	
	cin >> c;
	for (cicici=1; cicici<=c; cicici++)
	{
		cin >> n;
		for (i=1; i<=n; i++)
			cin >> x[i] >> y[i] >> r[i];
		
		if (n == 1)
		{
			printf("Case #%d: %.8lf\n",cicici,(double)r[1]);
		}
		else if (n == 2)
		{
			printf("Case #%d: %.8lf\n",cicici,(double)max(r[1], r[2]));
		}
		else
		{
			double ans(1E100);
			for (i=1; i<=3; i++)
				for (j=i+1; j<=3; j++)
					ans <?= get(i,j,6-i-j);
			printf("Case #%d: %.8lf\n",cicici,ans);
		}
		
	}
//	tiao;
	return 0;
}
