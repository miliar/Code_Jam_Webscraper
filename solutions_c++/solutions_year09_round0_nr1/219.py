#define _USE_MATH_DEFINES
#include <numeric>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <sstream>
using namespace std;
#pragma warning(disable : 4996 4018)
#pragma comment(linker, "/STACK:16777216")

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int L, D, N;
	cin >> L >> D >> N;

	string words[5000];
	for(int i = 0; i < D; i++)
	{
		cin >> words[i];
	}

	for(int i = 0; i < N; i++)
	{
		fprintf(stderr, "%i\n", i);
		int j, k, c = 0;
		string word;
		cin >> word;
		for(j = 0; j < D; j++)
		{
			int l = 0;
			for(k = 0; k < L; k++)
			{
				if(word[l] == '(')
				{
					bool f = true;
					while(word[l] != ')')
					{
						if(word[l] == words[j][k])
							f = false;
						l++;
					}
					if(f)
						break;
				}
				else if(word[l] != words[j][k])
					break;
				l++;
			}
			if(k == L)
				c++;
		}
		printf("Case #%i: %i\n", i + 1, c);
	}

	return 0;
}
