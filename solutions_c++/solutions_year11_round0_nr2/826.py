#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <algorithm>
#include <vector>

static const char base[] = "QWERASDF";

bool isbase(char c)
{
	return strchr(base, c);
}

int index(char c)
{
	assert(isbase(c));
	return strchr(base, c) - base;
}


void solve()
{
	int c;
	char T[8][8] = {0}, buff[4];
	bool O[8][8] = {0}, P[8] = {0};
	scanf("%d", &c);
	while (c--)
	{
		scanf("%s", buff);
		T[index(buff[0])][index(buff[1])] = T[index(buff[1])][index(buff[0])] = buff[2];
	}
	scanf("%d", &c);
	while (c--)
	{
		scanf("%s", buff);
		O[index(buff[0])][index(buff[1])] = O[index(buff[1])][index(buff[0])] = true;
	}
	scanf("%d ", &c);
	static std::vector<char> output;
	output.clear();
	while (c--)
	{
		char curr = getchar();
		if (!output.empty() && isbase(output.back()) && T[index(output.back())][index(curr)])
			output.back() = T[index(output.back())][index(curr)];
		else
		{
			output.push_back(curr);
			P[index(curr)] = true;
			for (int i = 0; i < 8; i++)
				if (P[i] && O[index(curr)][i])
				{
					std::fill(P, P + 8, false);
					output.clear();
					break;
				}
		}
	}
	putchar('[');
	for (auto it = output.begin(); it != output.end(); it++)
	{
		if (it != output.begin())
			printf(", ");
		printf("%c", *it);
	}
	puts("]");
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
}