//Fri May 21 19:57:21 CDT 2010
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

using namespace std;

vector<string> rotate(vector<string> v)
{
	int N = v.size();
	vector<string> ret(N, string(N, '.'));
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			ret[j][N-i-1] = v[i][j];
//			cout << ret[i][j];
		}
//		cout << endl;
	}
	for (int i = N - 1; i >= 0; i--)
	{
		for (int j = 0; j < N; j++)
		{
			int k = i;
			while (k + 1 < N && ret[k][j] != '.' && ret[k + 1][j] == '.')
			{
				ret[k + 1][j] = ret[k][j];
				ret[k][j] = '.';
				k++;
			}
		}
	}
	return ret;
}

int check(vector<string> v, int K)
{
	int flag1 = 0;
	int flag2 = 0;
	int N = v.size();
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < N; j++)
		{
			if (j + K - 1 < N)
			{
				bool flag = true;
				for (int p = 1; p < K; p++)
				{
					if (v[i][j] != v[i][j + p])
					{
						flag = false;
						break;
					}
				}
				if (flag == true)
				{
					if (v[i][j] == 'B')
						flag1 = 1;
					else if (v[i][j] == 'R')
						flag2 = 1;
				}
				if (i + K - 1 < N)
				{
					flag = true;
					for (int p = 1; p < K; p++)
					{
						if (v[i][j] != v[i + p][j + p])
						{
							flag = false;
							break;
						}
					}
					if (flag)
					{
						if (v[i][j] == 'B')
							flag1 = 1;
						else if (v[i][j] == 'R')
							flag2 = 1;
					}
				}
			}
			if (i + K - 1 < N)
			{
				bool flag = true;
				for (int p = 1; p < K; p++)
				{
					if (v[i][j] != v[i + p][j])
					{
						flag = false;
						break;
					}
				}
				if (flag)
				{
					if (v[i][j] == 'B')
						flag1 = 1;
					else if (v[i][j] == 'R')
						flag2 = 1;
				}
				if (j - K + 1 >= 0)
				{
					flag = true;
					for (int p = 1; p < K; p++)
					{
						if (v[i][j] != v[i + p][j - p])
						{
							flag = false;
							break;
						}
					}
					if (flag)
					{
						if (v[i][j] == 'B')
							flag1 = 1;
						else if (v[i][j] == 'R')
							flag2 = 1;
					}
				}
			}

		}
	}
	if (flag1 == 1 && flag2 == 1)
		return 3;
	if (flag1 == 1 && flag2 != 1)
		return 1;
	if (flag1 != 1 && flag2 == 1)
		return 2;
	return 0;
}

int main(int argc, char* argv[])
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin >> T;
	for (int ncase = 1; ncase <= T; ncase++)
	{
		int N, K;
		cin >> N >> K;
		vector<string> v(N, string(N, '.'));
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				cin >> v[i][j];
			}
		}
		v = rotate(v);
//		for(int i=0; i<N; i++)
//		{
//			for(int j=0; j<N; j++)
//			{
//				cout << v[i][j];
//			}
//			cout << endl;
//		}
		int score = check(v, K);
		cout << "Case #" << ncase << ": ";
		if (score == 0)
			cout << "Neither";
		else if (score == 1)
			cout << "Blue";
		else if (score == 2)
			cout << "Red";
		else
			cout << "Both";
		cout << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
