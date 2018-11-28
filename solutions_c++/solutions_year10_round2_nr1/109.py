
	#include <cstdlib>
	#include <cstdio>
	#include <string>
	#include <algorithm>
	#include <iostream>

	using namespace std;

	int N, n, m, curpos, ans, countc;

	string val[100005];
	int last[100005], prev[100005];

	int add(string s)
	{
		int p;
		for (p = last[curpos]; p >= 0 && val[p] != s; p = prev[p]);
//			if (n == 8 && m == 5 && curpos == 0 && s == "7")
//			{
//				printf("%d ", p);
//				cout << val[p] << endl;
//			}
		if (p == -1)
		{
			ans ++;
			val[countc] = s;
			prev[countc] = last[curpos];
			last[curpos] = countc;
			curpos = countc;
			countc ++;
		}
		else
			curpos = p;
	}

	int ins()
	{
		char c = getchar();
		string s = "";
		curpos = 0;
		for (c = getchar(); c != '\n'; c = getchar())
		{
			if (c != '/')
				s = s + c;
			else
			{
//				if (n == 8 && m == 5)
//					cout << s << ' ' << curpos << endl;
				add(s);
//				if (n == 8 && m == 5)
//					cout << s << ' ' << ans << ' ' << curpos << endl;
				s = "";
			}
		}
//		if (n == 8 && m == 5)
//			cout << s << ' ' << curpos << endl;
		add(s);
//		if (n == 8 && m == 5)
//			cout << s << ' ' << ans << ' ' << curpos << endl;
	}

	int work()
	{
		scanf("%d%d\n", &n, &m);
		countc = 1;
		memset(last, -1, sizeof(last));
		for (int i = 0; i < n; i ++)
			ins();
		ans = 0;
		//if (n == 0)	ans --;
		for (int i = 0; i < m; i ++)
			ins();
		printf("%d\n", ans);
	}

	int main()
	{
		freopen("A-large.in", "r", stdin);
		freopen("A.out", "w", stdout);
		scanf("%d", &N);
		for (int i = 1; i <= N; i ++)
		{
			printf("Case #%d: ", i);
			work();
		}
		return 0;
	}
