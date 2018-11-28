#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <stack>

using namespace std;

typedef unsigned long long ull;
typedef unsigned int uint;

int main(int argc, char **argv)
{
	int T;
	freopen("C-small.in", "rb", stdin);
	freopen("C-small.out", "wb", stdout);

	scanf("%d", &T);
	for(int t = 0; t < T; t++)
	{
		printf("Case #%d: ", t + 1);

		uint N;
		ull L, H;
		scanf("%u %llu %llu", &N, &L, &H);
		vector<ull> frequencies(N);
		for(uint i = 0; i < N; i++)
		{
			scanf("%llu", &frequencies[i]);
		}

		for(; L <= H; L++)
		{
			uint i;
			for(i = 0; i < frequencies.size(); i++)
			{
				if(L % frequencies[i] != 0 && frequencies[i] % L != 0)
				{
					break;
				}
			}

			if(i == frequencies.size())
			{
				printf("%llu\n", L);
				break;
			}
		}

		if(L > H)
		{
			printf("NO\n");
		}
	}

	fclose(stdin);
	fclose(stdout);
}