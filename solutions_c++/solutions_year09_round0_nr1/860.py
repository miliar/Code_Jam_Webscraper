#define _CRT_SECURE_NO_DEPRECATE
#ifdef NDEBUG
	#define _SECURE_SCL 0
#endif
#include <iostream>
#include <memory>
#include <vector>
#include <algorithm>
#include <string>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

int TT;
int L, D, N;
char Words[5000][16];
bool Marks[16][26];
string Pattern;

int main()
{
	cin >> L >> D >> N;
	for (int I = 0; I < D; I++) cin >> Words[I];
	for (int TT = 1; TT <= N; TT++)
	{
		cin >> Pattern;
		memset(Marks, 0, sizeof Marks);
		int Pos = 0;
		for (int I = 0; I < L; I++)
		{
			if (Pattern[Pos] == '(')
			{
				for (Pos++; Pattern[Pos] != ')'; Pos++) Marks[I][Pattern[Pos] - 'a'] = true;
				Pos++;
			}
			else
			{
				Marks[I][Pattern[Pos] - 'a'] = true;
				Pos++;
			}
		}
		int Count = 0;
		for (int I = 0; I < D; I++)
		{
			bool Matched = true;
			for (int J = 0; J < L; J++)
				if (!Marks[J][Words[I][J] - 'a'])
				{
					Matched = false;
					break;
				}
			if (Matched) Count++;
		}
		printf("Case #%d: %d\n", TT, Count);

	}
	return 0;
}