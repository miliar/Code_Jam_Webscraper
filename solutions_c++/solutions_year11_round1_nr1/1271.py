//acm header include 
#include<iostream>
#include<list>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int Pd, Pg, n;
	int T, t;
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		scanf("%d %d %d", &n, &Pd, &Pg);
		printf("Case #%d: ", t);
		bool possible = true;
		int fenmu = 100;

		if (Pd < 100 && Pg == 100)  possible = false;

		if (Pd % 2 == 0){ Pd /= 2; fenmu /=2; }
		if (Pd % 2 == 0){ Pd /= 2; fenmu /=2; }

		if (Pd % 5 == 0){ Pd /= 5; fenmu /=5; }
		if (Pd % 5 == 0){ Pd /= 5; fenmu /=5; }

		// w�ǽ���Ӯ�ĳ���
		// ���Կ϶�w��Pd�ı����� D��febmu�ı���
		if (fenmu > n) possible = false;
		
		

		if (Pd > 0 && Pg == 0)  possible = false;

		if (possible) printf("Possible\n");
		else printf("Broken\n");
	}

	return 0;
}