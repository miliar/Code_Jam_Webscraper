#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <utility>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int NN, TT;
int N, Target;
int Gates[20000];
int Changes[2000];
int Values[20000];
int P[20000][2];

int main()
{
	cin >> NN;
	for (TT = 1; TT <= NN; TT++)
	{
		cin >> N >> Target;
		for (int J = 1; J <= (N - 1) / 2; J++)
			cin >> Gates[J] >> Changes[J];
		for (int J = (N + 1) / 2; J <= N; J++)
			cin >> Values[J];
		for (int X = N; X >= 1; X--)
		{
			if (X * 2 > N)
				P[X][Values[X]] = 0,
				P[X][1 - Values[X]] = -1;
			else
			{
				P[X][0] = P[X][1] = -1;
				int Y = X * 2;
				int Z = Y + 1;
				for (int I = 0; I < 2; I++) if (P[Y][I] >= 0)
					for (int J = 0; J < 2; J++) if (P[Z][J] >= 0)
					{
						int V = Gates[X] == 1 ? (I & J) : (I | J);
						if (P[X][V] < 0 || P[X][V] > P[Y][I] + P[Z][J])
							P[X][V] = P[Y][I] + P[Z][J];
						if (Changes[X] == 0) continue;
						V = Gates[X] == 0 ? (I & J) : (I | J);
						if (P[X][V] < 0 || P[X][V] > P[Y][I] + P[Z][J] + 1)
							P[X][V] = P[Y][I] + P[Z][J] + 1;
					}
			}
		}
		cout << "Case #" << TT << ": ";
		if (P[1][Target] >= 0) cout << P[1][Target];
		else cout << "IMPOSSIBLE";
		cout << endl;
	}
	return 0;
}
