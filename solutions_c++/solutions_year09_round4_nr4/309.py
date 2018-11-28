#define _CRT_SECURE_NO_WARNINGS
#include "stdio.h"
#include <cmath>
#include <cassert>
#include "iostream"
#include "sstream"
#include "string"
#include "algorithm"
#include "vector"
#include "queue"
#include "map"

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

#define all(s) s.begin(), s.end()

const int INF = 1000000000;

struct s_s
{
	int x, y, r;
};



int get_height (vector<string> & mp, int x, int y, int n)
{
	int res = 0;
	while (y < n - 1 && mp[y + 1][x] == '.')
		res++, y++;
	return res;
}


int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);


	int test_count;
	cin >> test_count;



	for (int test = 0; test < test_count ; test++)
	{
		fprintf(stderr, "%d\n", test);

		string s;
//		getline(cin, s);
//		cin >> s;

		int n;
		cin >> n;
		vector<s_s> a(n);
		for (int i = 0; i < n ; i++)
		{
			s_s st;
			cin >> st.x >> st.y >> st.r;
			a[i] = st;
		}

		double best = INF;

		if (n == 3)
		for (int i = 0; i < n ; i++)
		{
			for (int j = i + 1; j < n ; j++)
			{
				double dist = sqrt((double)(a[i].x - a[j].x)*(a[i].x - a[j].x) + (a[i].y - a[j].y)*(a[i].y - a[j].y));
				dist += a[i].r + a[j].r;
		
	
				int k = 0;
				for ( ; k == i || k == j; ++k);
				double cur = max(dist / 2, a[k].r + 0.0);
				best = min(best, cur);

			}
		}

		if (n == 2)
		{
			best = max(a[0].r, a[1].r);
		}

		if (n == 1)
			best = a[0].r;
		
		printf("Case #%d: %.6f\n", test + 1, best);
		
	}

}