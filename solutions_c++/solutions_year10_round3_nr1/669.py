# include <algorithm>
# include <iostream>
using namespace std;

struct tStair
{
	int a, b;
} stair[1010];


bool cmp(const tStair &x, const tStair &y)
{
	return x.a < y.a;
}

int main()
{
	int t, i, j, n, ans, circle;

	
//	freopen("A-large.in", "rt", stdin);
//	freopen("A-large.out", "wt", stdout);

	for (cin >> t, circle = 1; circle <= t; circle++)
	{
		ans = 0;
		
		cin >> n;
		for (i = 0; i < n; i++)
			cin >> stair[i].a >> stair[i].b;
		sort(stair, stair + n, cmp);
		
		for (i = 1; i < n; i++)		
			for (j = i - 1; j >= 0; j--)
				if (stair[j].b > stair[i].b) ans++;
		
		cout << "Case #" << circle << ": " << ans << endl;
	}

//	fclose(stdout);
//	fclose(stdin);	
	return 0;
}