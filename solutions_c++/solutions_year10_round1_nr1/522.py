#include <iostream>
#include <fstream>
#include <memory.h>
#include <cmath>

using namespace std;

#define oo 1000000000
#define MAXN 60

ifstream in("input.txt");
ofstream out("output.txt");

char map[MAXN][MAXN];
char tmp[MAXN], tn;

int main()
{
	int T;
	in >> T;
	int N, K;
	for (int t = 1; t <= T; t++)
	{
		in >> N >> K;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				in >> map[i][j];
		for (int i = N - 1; i >= 0; i--)
		{
			tn = 0;
			for (int j = N - 1; j >= 0; j--)
			{
				if (map[i][j] != '.')
					tmp[tn++] = map[i][j];
			}
			for (int j = N - 1; j > N - 1 - tn; j--)
				map[i][j] = tmp[N - 1 - j];
			for (int j = N - 1 - tn; j >= 0; j--)
				map[i][j] = '.';
		}
		bool isb = false, isr = false;
		bool t1, t2;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				if (i + 1 >= K)
				{
					t1 = t2 = true;
					for (int d = i; d >= i + 1 - K; d--)
					{
						t1 = t1 && (map[d][j] == 'B');
						t2 = t2 && (map[d][j] == 'R');
					}
					isb = isb || t1;
					isr = isr || t2;
				}
				if (j + 1 >= K)
				{
					t1 = t2 = true;
					for (int d = j; d >= j + 1 - K; d--)
					{
						t1 = t1 && (map[i][d] == 'B');
						t2 = t2 && (map[i][d] == 'R');
					}
					isb = isb || t1;
					isr = isr || t2;
				}
				int ss = min(i + 1, j + 1);
				if (ss >= K)
				{
					t1 = t2 = true;
					for (int d = 0; d < K; d++)
					{
						t1 = t1 && (map[i - d][j - d] == 'B');
						t2 = t2 && (map[i - d][j - d] == 'R');
					}
					isb = isb || t1;
					isr = isr || t2;
				}
				ss = min(N - i, j + 1);
				if (ss >= K)
				{
					t1 = t2 = true;
					for (int d = 0; d < K; d++)
					{
						t1 = t1 && (map[i + d][j - d] == 'B');
						t2 = t2 && (map[i + d][j - d] == 'R');
					}
					isb = isb || t1;
					isr = isr || t2;
				}
			}
		}
		out << "Case #" << t << ": ";
		if (isb && isr)
			out << "Both" << endl;
		else if (isr)
			out << "Red" << endl;
		else if (isb)
			out << "Blue" << endl;
		else
			out << "Neither" << endl;
	}
	return 0;
}