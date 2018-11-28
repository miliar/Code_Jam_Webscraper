#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int total[128];
	int T;
	cin >> T;
	for (int t = 1; t <=T; ++t)
	{
		int N, S, p;
		cin >> N >> S >> p;
		for (int i=0; i<N; ++i)
			cin >> total[i];

		int res=0;
		for (int i = 0; i < N; ++i)
		{
			int canDo=0, canS=0;
			for (int a = 0; a <= 10; a++)
				for (int b = a; b <= 10; b++)
				{

					int c = total[i] - a - b;
					if (c<b)
						continue;
					if (c-a > 2)
						continue;
					if (c-a == 2)
					{
						if (c>=p)
							canS=1;
					}
					else
					{
						if (c>=p)
							canDo=1;
					}
				}

			if(canDo)
				res++;
			else
			{
				if (S && canS)
				{
					S--;
					res++;
				}
			}
		}

		cout << "Case #" << t << ": " << res << endl;
	}

	return 0;
}