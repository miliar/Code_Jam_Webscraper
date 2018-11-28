#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

ifstream fin("D-small-attempt1.in");
ofstream fout("D-small-attempt1.out");

#define cin fin
#define cout fout

struct Tp
{
	double x, y, r;
};

Tp p[50];
int n;

int list1[50], list2[50];
int l1, l2;
double ans;

double dist(Tp & a, Tp & b)
{
	return sqrt((a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y));
}

double count(int * a, int m)
{
	if (m == 1)
		return p[a[0]].r * 2.0;
	if (m == 2)
		return p[a[0]].r + p[a[1]].r + dist(p[a[0]], p[a[1]]);

	return 0.0;
}

void dfs(int now)
{
	if (now >= n)
	{
		double r1 = count(list1, l1);
		double r2 = count(list2, l2);

		if (r2 > r1) r1 = r2;
		if (r1 < ans || ans < 0) ans = r1;
			
		return;
	}

	if (l1 < 2)
	{
		list1[l1] = now;
		l1++;
		dfs(now+1);
		l1--;
	}

	if (l2 < 2)
	{
		list2[l2] = now;
		l2++;
		dfs(now+1);
		l2--;
	}
}

int main()
{
	int cases;

	cout.precision(8);
	cout.flags(ios::fixed);

	cin >> cases;
	for (int i = 1; i <= cases; i++)
	{
		cin >> n;
		for (int j = 0; j < n; j++)
			cin >> p[j].x >> p[j].y >> p[j].r;

		l1 = l2 = 0;
		ans = -1;
		dfs(0);

		cout << "Case #" << i << ": " << ans / 2.0 << endl;
	}

	return 0;
}

