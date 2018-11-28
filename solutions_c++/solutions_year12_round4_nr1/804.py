#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <set>
#include <ctime>
using namespace std;

struct Circle
{
	double x;
	double y;
	int r;
};

int main()
{
	srand(time(NULL));
	freopen("output.txt", "w", stdout);
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		int n, w, l;
		cin >> n >> w >> l;
		vector<Circle> a(n);
		for (int i = 0; i < n; i++)
		{
			cin >> a[i].r;
		}

		int randX, randY;
		bool gotcha = false;
		while (!gotcha)
		{
			for (int i = 0; i < n; i++)
			{
				randX = rand();
				a[i].x = (randX * randX) % w + 1.0 / rand();

				randY = rand();
				a[i].y = (randY * randY) % l + 1.0 / rand();
			}

			bool flag = false;
			for (int i = 0; i < n && !flag; i++)
			{
				for (int j = i + 1; j < n && !flag; j++)
				{
					if (pow(a[i].r + a[j].r, 2.0) > pow(a[i].x - a[j].x, 2.0) + pow(a[i].y - a[j].y, 2.0))
					{
						flag = true;
					}
				}
			}

			gotcha = !flag;
		}

		//cout << "Case #" << tc << ":";
		printf("Case #%d:", tc);
		for (int i = 0; i < n; i++)
		{
			printf(" %.8lf %.8lf", a[i].x, a[i].y);
			//cout << " " << a[i].x << " " << a[i].y;
		}
		putchar('\n');
		//cout << endl;
	}

	return 0;
}