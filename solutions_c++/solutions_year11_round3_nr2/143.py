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
	freopen("B-large.in", "rb", stdin);
	freopen("B-large.out", "wb", stdout);

	scanf("%d", &T);
	for(int t = 0; t < T; t++)
	{
		printf("Case #%d: ", t + 1);

		uint L, N, C;
		ull tb;
		scanf("%u %llu %u %u", &L, &tb, &N, &C);
		vector<ull> length(N);
		for(uint i = 0; i < C; i++)
		{
			int a;
			scanf("%d", &a);
			for(uint j = i; j < N; j += C)
			{
				length[j] = a * 2;
			}
		}

		ull dist = 0;
		uint star = 0;
		ull tnow = 0;
		while(star < N && tb > 0)
		{
			if((length[star]) <= tb)
			{
				tb -= length[star];
				tnow += length[star];
				
				star++;
			}
			else
			{
				dist = tb;
				tnow += tb;
				tb = 0;
			}
		}

		length = vector<ull> (length.begin() + star, length.end());
		N = length.size();
		if(N > 0)
		{
			length[0] -= dist;

			vector< pair<ull, uint> > tosortlen(N);
			for(uint i = 0; i < N; i++)
			{
				tosortlen[i].first = length[i];
				tosortlen[i].second = i;
			}

			sort(tosortlen.rbegin(), tosortlen.rend());

			L = min(L, tosortlen.size());
			for(uint i = 0; i < L; i++)
			{
				length[tosortlen[i].second] /= 2;
			}

			for(uint i = 0; i < N; i++)
			{
				tnow += length[i];
			}
		}

		printf("%llu\n", tnow);
	}

	fclose(stdin);
	fclose(stdout);
}