#include <iostream>
#include <queue>

#define debug(n, s, ...) \
	if (i == n)\
		fprintf(stderr, s, ## __VA_ARGS__);

#define debug_rkn(n) \
	if (i == n) \
		fprintf(stderr, "R: %d; k: %d; N: %d;\n", R, k, N);

using namespace std;

int main()
{
	int T;
	int R, k, N;

	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int Euros = 0;
		queue<int> q;
		queue<int> rc;

		scanf("%d%d%d", &R, &k, &N);
		int total = 0;
		for (int j = 0; j < N; j++)
		{
			int tmp;
			scanf("%d",&tmp);
			q.push(tmp);
			total += tmp;
		}
		if (total <= k)
			printf("Case #%d: %d\n", i+1, total*R);
		else {
			for (int j = 0; j < R; j++)
			{
				int tmp = 0;
				while ((tmp+q.front()) <= k)
				{
					tmp+=q.front();
					rc.push(q.front());
					q.pop();
				}
				Euros+=tmp;
				while (!rc.empty())
				{
					q.push(rc.front());
					rc.pop();
				}
			}
			printf("Case #%d: %d\n", i+1, Euros);
		}
		Euros = 0;
		/*
		while(!rc.empty())
			rc.pop();
		while(!q.empty())
			q.pop();
		*/
	}

	return 0;
}

