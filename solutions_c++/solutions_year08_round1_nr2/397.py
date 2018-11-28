#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

#define two(X) (1<<(X))
#define contain(S,X) ((S&two(X))>0)
template<class T> int countbit(T n) {return (n==0)?0:(1+countbit(n&(n-1)));}

int C;
int N;
int M;
int like[100][10];
bool ok[100];

int main()
{
	ifstream fin("B.in");
	ofstream fout("B.out");

	fin >> C;
	for (int c = 1; c <= C; c++)
	{
		fin >> N >> M;
		memset(like, -1, sizeof(like));
		for (int i = 0; i < M; i++)
		{
			int TT, X, Y;
			fin >> TT;
			for (int j = 0; j < TT; j++)
			{
				fin >> X >> Y;
				if (like[i][X-1] != -1)
				{
					if (like[i][X-1] != Y) like[i][X-1] = 2;
				}
				else
				{
					like[i][X-1] = Y;
				}
			}
		}
		int res = -1;
		int min_malted = 987654321;
		for (int k = 0; k < two(N); k++)
		{
			memset(ok, false, sizeof(ok));
			int num_ok = 0;
			for (int i = 0; i < N; i++)
			{
				int x = contain(k, i) ? 1 : 0;
				for (int j = 0; j < M; j++)
				{
					if (ok[j]) continue;
					if (like[j][i] == x || like[j][i] == 2)
					{
						ok[j] = true;
						num_ok++;
					}
				}
			}
			if (num_ok == M)
			{
				int cnt = countbit(k);
				if (cnt < min_malted)
				{
					res = k;
					min_malted = cnt;
				}
			}
		}
		fout << "Case #" << c << ":";
		if (res == -1)
		{
			fout << " IMPOSSIBLE" << endl;
		}
		else
		{
			for (int i = 0; i < N; i++)
			{
				if (contain(res, i))
				{
					fout << " 1";
				} 
				else
				{
					fout << " 0";
				}
			}
			fout << endl;
		}
	}

	return 0;
}
