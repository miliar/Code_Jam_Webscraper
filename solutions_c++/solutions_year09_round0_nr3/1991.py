#include <cstdio>
#include <cstring>

const int n = 19;
const char pat[] = "welcome to code jam";

int m;
char buf[520];

int mem[30][500];

const int modulus = 1000;

int count(int I, int J)
{
	if (mem[I][J] >= 0)
	{
		return mem[I][J];
	}
	else if (I == n)
	{
		return mem[I][J] = 1;
	}
	else
	{
		int sum = 0;
		for (int k = J; k < m; ++k)
		{
			if (buf[k] == pat[I])
			{
				sum += count(I + 1, k) % modulus;
			}
		}

		return mem[I][J] = sum % modulus;
	}
}

int main()
{
	int N;

	scanf("%d\n", &N);

	for (int t = 1; t <= N; ++t)
	{
		memset(mem, 0xFF, sizeof(mem));

		gets(buf);
		m = strlen(buf);

		printf("Case #%d: %0.4d\n", t, count(0, 0));
	}

	return 0;
}
