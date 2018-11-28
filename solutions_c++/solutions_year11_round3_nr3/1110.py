#include <cstdio>

int notes[20000];

int main()
{
	int cases;
	scanf("%d", &cases);
	for (int T = 1; T <= cases; T++)
	{
		int i, N, H, L;
		scanf("%d %d %d", &N, &L, &H);
		for (i = 0; i < N; i++)
			scanf ("%d", &notes[i]);
		bool flag = false;
		for (i = L; i <= H && !flag; i++)
		{
			int j;
			for (j = 0; j < N ; j++)
			{
				if (notes[j] < i && !(i%notes[j]))
					continue;
				if (i <= notes[j] && !(notes[j]%i))
					continue;
				break;
			}
			if (j >= N)
			{
				flag = true;
				break;
			}
		}
		printf("Case #%d: ", T);
		if (flag)
			printf("%d\n", i);
		else
			printf("NO\n");
	}
	return 0;
}