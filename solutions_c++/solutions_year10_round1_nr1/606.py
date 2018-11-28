/*
 * Author: rush
 * Created Time:  2010年05月22日 星期六 09时12分07秒
 * File Name: icpc/GCJ0522/A.cpp
 */
#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;
typedef long long LL;
int T, N, K;
char board[55][55], rotated[55][55];
bool Rwin, Bwin;

void update(char x)
{
	if (x == 'R') Rwin = true;
	else if (x == 'B') Bwin = true;
}

void check()
{
	Rwin = Bwin = false;
	int cnt;
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
		{
			cnt = 0;
			for (int k = i; k < N; ++k)
				if (rotated[k][j] == rotated[i][j])
					++cnt;
				else
					break;
			if (cnt >= K) update(rotated[i][j]);

			cnt = 0;
			for (int k = j; k < N; ++k)
				if (rotated[i][k] == rotated[i][j])
					++cnt;
				else
					break;
			if (cnt >= K) update(rotated[i][j]);

			cnt = 0;
			for (int k = 0; i + k < N && j - k >= 0; ++k)
				if (rotated[i + k][j - k] == rotated[i][j])
					++cnt;
				else
					break;
			if (cnt >= K) update(rotated[i][j]);
			
			cnt = 0;
			for (int k = 0; i + k < N && j + k < N; ++k)
				if (rotated[i + k][j + k] == rotated[i][j])
					++cnt;
				else
					break;
			if (cnt >= K) update(rotated[i][j]);
		}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	for (int id = 1; id <= T; ++id)
	{
		cin >> N >> K;
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
			{
				cin >> board[i][j];
				rotated[j][N - 1 - i] = board[i][j];
			}
		for (int j = 0; j < N; ++j)
		{
			for (int i = 1; i <= N - 1; ++i)
				for (int k = 0; k < N; ++k)
					if (k + 1 < N && rotated[k + 1][j] == '.')
						swap(rotated[k][j], rotated[k + 1][j]);
		}
		/*
		for (int i = 0; i < N; ++i)
		{
			for (int j = 0; j < N; ++j)
				cout << rotated[i][j];
			cout << endl;
		}
		*/
		check();
		cout << "Case #" << id << ": ";
		if (Rwin && Bwin)
			cout << "Both" << endl;
		else if (Rwin)
			cout << "Red" << endl;
		else if (Bwin)
			cout << "Blue" << endl;
		else
			cout << "Neither" << endl;
	}

    return 0;
}
