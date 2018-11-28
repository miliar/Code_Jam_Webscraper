#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

typedef struct _circle {
	int x,y,r;
} circle;

double dist(int x1, int y1, int x2, int y2)
{
	return sqrt((double)((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)));
}

int main()
{
	int cas;
	cin >> cas;
	for (int xxx=1; xxx<=cas; ++xxx)
	{
		int n;
		circle c[4];

		cin >> n;
		for (int i=1; i<=n; ++i)
			cin >> c[i].x >> c[i].y >> c[i].r;

		if (n == 1)
		{
			printf("Case #%d: %.6lf\n", xxx, c[1].r*1.0);
		}
		else if (n == 2)
		{
			printf("Case #%d: %.6lf\n", xxx, max(c[1].r, c[2].r) * 1.0);
		}
		else
		{
			double mymin = 1000000000;
			for (int i=1; i<=3; ++i)
			{
				for (int j=i+1; j<=3; ++j)
				{
					double dd = (dist(c[i].x, c[i].y, c[j].x, c[j].y) + c[i].r + c[j].r) / 2;
					double ff;
					for (int k=1; k<=3; ++k)
					{
						if (k != i && k != j)
						{
							ff = c[k].r;
						}
					}
					mymin = min(max(dd, ff), mymin);
				}
			}
			printf("Case #%d: %.6lf\n", xxx, mymin);
		}
	}
}

/*#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int pos[100];
int n;

int main()
{
	int cas;
	cin >> cas;
	for (int xxx=1; xxx<=cas; ++xxx)
	{
		memset(pos, 0, sizeof(pos));
		string tmp;
		cin >> n;
		for (int i=1; i<=n; ++i)
		{
			cin >> tmp;
			for (int j=n-1; j>=0; --j)
			{
				if (tmp[j] == '1')
				{
					pos[i] = j+1;
					break;
				}
			}
		}

		int move = 0;
		for (int i=1; i<=n; ++i)
		{
			if (pos[i] > i)
			{
				int find = 100000;
				for (int j=i+1; j<=n; ++j)
				{
					if (pos[j] <= i)
					{
						find = j;
						break;
					}
				}

				for (int j=find; j>i; --j)
				{
					int t = pos[j];
					pos[j] = pos[j-1];
					pos[j-1] = t;
				}

				move += find - i;
			}
		}

		cout << "Case #" << xxx << ": " << move << endl;
	}

	return 0;
}*/