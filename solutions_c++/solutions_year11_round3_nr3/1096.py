#include <iostream>
#define NMAX 100000

using namespace std;

int main()
{
	freopen("har.in", "r", stdin);
	freopen("har.out", "w", stdout);
	
	int T, N;
	long L, H;
	long notes[NMAX];
	
	scanf("%d", &T);
	
	for (int tc = 0; tc < T; tc++)
	{
		scanf("%d %ld %ld", &N, &L, &H);
		for (int i = 0; i < N; i++)
		{
			scanf("%ld", &notes[i]);
		}

		printf("Case #%d: ", tc + 1);
		bool bf = false;
		for (long i = L; i <= H; i++)
		{
			bool f = true;
			for (int n = 0; n < N; n++)
			{
				if (i % notes[n] != 0 && notes[n] % i != 0)
				{
					f = false;
					break;
				} 
			}
			if (f)
			{
				printf("%ld\n", i);
				bf = true;
				break;
			}
		}
		if (!bf) printf("NO\n");
	}
}