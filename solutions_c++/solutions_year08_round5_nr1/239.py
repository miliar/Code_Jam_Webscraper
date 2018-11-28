// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <fstream>
#include <algorithm>
#include <limits>
#include <queue>
#include <stdexcept>

#include <math.h>
static const double pi = 3.1415926535;

using namespace std;


typedef long long LL;
typedef pair<LL, LL> PLL;

#define sz(v) ((int)v.size())
#define abs(x) (((x) >= 0) ? (x) : -(x))

bool pllless(PLL p1, PLL p2)
{
	return (p1.first < p2.first) || ((p1.first == p2.first) && (p1.second < p2.second));
}

bool neq(PLL p1, PLL p2)
{
	return ((p1.first != p2.first) || (p1.second != p2.second));
}


class Q11
{
private:
	Q11() {};
	
public:
	static void go(string inputFilePath, string outputFilePath)
	{
		ifstream inpf(inputFilePath.c_str());
		ofstream outf(outputFilePath.c_str());

		if (!inpf.good() || !outf.good())
		{
			throw(std::invalid_argument("Can't open input or output file!"));
		}

		int N;
		inpf >> N;

		const int M = 304;

		for (int n = 1; n <= N; ++n)
		{
			int L;
			inpf >> L;

			vector<vector<int> > mp(M * 2 + 1, vector<int>(M * 2 + 1, 0));
			int x = M;
			int y = M;
			int dir = 0;
			for (int l = 0; l < L; ++l)
			{
				string S;
				int T;
				inpf >> S >> T;
				
				for (int t = 0; t < T; ++t)
				{
					for (int s = 0; s < sz(S); ++s)
					{
						mp[y][x] = 1;
						switch(S[s])
						{
						case 'F':
							switch (dir)
							{
							case 0: y++; mp[y][x] = 1; y++; break;
							case 1: x++; mp[y][x] = 1; x++; break;
							case 2: y--; mp[y][x] = 1; y--; break;
							case 3: x--; mp[y][x] = 1; x--; break;
							}
							break;
						case 'R':
							dir = (dir + 1) % 4;
							break;
						case 'L':
							dir -= 1;
							if (dir < 0)
								dir = 3;
							break;
						} 
					}
				}
			}
			if ((y != M) || (x != M))
			{
				throw(-1);
			}


			queue<pair<int, int> > q;
			q.push(pair<int, int>(0, 0));
			while (!q.empty())
			{
				pair<int, int> p = q.front();
				q.pop();
				if ((p.first >= 0) && (p.first <= M * 2) && (p.second >= 0) && (p.second <= M * 2))
				{
					if (mp[p.first][p.second] == 0)
					{
						mp[p.first][p.second] = -1;
						q.push(pair<int, int>(p.first - 1, p.second));
						q.push(pair<int, int>(p.first + 1, p.second));
						q.push(pair<int, int>(p.first, p.second - 1));
						q.push(pair<int, int>(p.first, p.second + 1));
					}
				}
			}

			for (int x = 0; x < M * 2; ++x)
			{
				int state = 0;

				for (int y = 0; y < M * 2; ++y)
				{
					if (mp[y][x] == 1)
					{
						if (state)
						{
							int y2 = y - 1;
							while (mp[y2][x] != 1)
							{
								mp[y2][x] = 2;
								--y2;
							}
						}
						state = 1 - state;
						if (state)
						{
							while ((mp[y][x] == 1) || (mp[y][x] == 0))
							{
								++y;
							}
						}
					}
				}
			}

			for (int y = 0; y < M * 2; ++y)
			{
				int state = 0;

				for (int x = 0; x < M * 2; ++x)
				{
					if (mp[y][x] == 1)
					{
						if (state)
						{
							int x2 = x - 1;
							while (mp[y][x2] != 1)
							{
								mp[y][x2] = 2;
								--x2;
							}
						}
						state = 1 - state;
						if (state)
						{
							while ((mp[y][x] == 1) || (mp[y][x] == 0))
							{
								++x;
							}
						}
					}
				}
			}


			LL ctr = 0;

			for (int y = 0; y < M * 2 - 1; ++y)
			{
				for (int x = 0; x < M * 2 - 1; ++x)
				{
					if ((mp[y][x] > 0) && (mp[y + 1][x] > 0) && (mp[y][x + 1] > 0) && (mp[y + 1][x + 1] > 0))
					{
						if ((mp[y][x] > 1) || (mp[y + 1][x] > 1) || (mp[y][x + 1] > 1) || (mp[y + 1][x + 1] > 1))
						{
							++ctr;
						}
					}
				}
			}

			outf << "Case #" << n << ": " << ctr / 4 << endl;			
		}
	}
};



class Q12
{
private:
	Q12() {};
public:
	static void go(string inputFilePath, string outputFilePath)
	{
		ifstream inpf(inputFilePath.c_str());
		ofstream outf(outputFilePath.c_str());

		if (!inpf.good() || !outf.good())
		{
			throw(std::invalid_argument("Can't open input or output file!"));
		}

		int N;
		inpf >> N; 

		for (int n = 1; n <= N; ++n)
		{
			LL N, M;
			inpf >> N >> M;

			outf << "Case #" << n << ": " << "IMPOSSIBLE" << endl;	
		}
	}
};


class Q13
{
private:
	Q13() {};
public:
	static void go(string inputFilePath, string outputFilePath)
	{
		ifstream inpf(inputFilePath.c_str());
		ofstream outf(outputFilePath.c_str());

		if (!inpf.good() || !outf.good())
		{
			throw(std::invalid_argument("Can't open input or output file!"));
		}

		int N;
		inpf >> N;

		for (int n = 1; n <= N; ++n)
		{
			int k;
			string S;
	
			inpf >> k >> S;

			
			outf << "Case #" << n << ": " << k << endl;		
		}
	}
};

class Q14
{
private:
	Q14() {};
public:
	static void go(string inputFilePath, string outputFilePath)
	{
		ifstream inpf(inputFilePath.c_str());
		ofstream outf(outputFilePath.c_str());

		if (!inpf.good() || !outf.good())
		{
			throw(std::invalid_argument("Can't open input or output file!"));
		}

		int N;
		inpf >> N;

		for (int n = 1; n <= N; ++n)
		{
			int T;
	
			inpf >> T;

			outf << "Case #" << n << ": " << T << endl;		
		}
	}
};


int _tmain(int argc, _TCHAR* argv[])
{
	Q11::go("input.txt", "output.txt");
	//Q12::go("input.txt", "output.txt");
	//Q13::go("input.txt", "output.txt");
	//Q14::go("input.txt", "output.txt");

	cout << endl << "Complete!" << endl;
	getchar();
	return 0;
}

