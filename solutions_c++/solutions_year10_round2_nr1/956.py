# include <cstdio>
# include <iostream>
# include <algorithm>
using namespace std;

struct tDir
{
	bool useful;
	char dir[110];
} inp[210];


bool cmp(const tDir &x, const tDir &y)
{
	return (strcmp(x.dir, y.dir) < 0 || !strcmp(x.dir, y.dir) && !x.useful && y.useful);
}


int calc(int x)
{
	int p = 0, q = 0;
	
	if (x)
	{
		for (p = 0; inp[x].dir[p] == inp[x - 1].dir[p] && inp[x].dir[p]; p++);
		if (inp[x].dir[p]) 
		{
			p++;
			q = 1;
		}
	}	
	
	for (; inp[x].dir[p]; p++)
		if (inp[x].dir[p] == '/') q++;

	return q;
}


int main()
{
	int i, t, n, m, all, circle, ans;
	
	
//	freopen("A-large.in", "rt", stdin);
//	freopen("A-large.out", "wt", stdout);
	for (cin >> t, circle = 1; circle <= t; circle++)
	{
		cin >> n >> m;
		all = 0;

		while (n--)
		{
			inp[all].useful = false;
			scanf("%s", inp[all++].dir);
		}
		while (m--)
		{
			inp[all].useful = true;
			scanf("%s", inp[all++].dir);
		}

		sort(inp, inp + all, cmp);
		
		ans = 0;
		for (i = 0; i < all; i++)		
			if (inp[i].useful)		
				ans += calc(i);			

		cout << "Case #" << circle << ": " << ans << endl;
	}
	
	
//	fclose(stdout);
//	fclose(stdin);
	
	return 0;
}