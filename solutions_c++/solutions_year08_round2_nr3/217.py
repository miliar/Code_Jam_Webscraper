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

		for (int n = 1; n <= N; ++n)
		{
			LL nn, A, B, C, D, x0, y0, M;
			inpf >> nn >> A >> B >> C >> D >> x0 >> y0 >> M;

			vector<PLL> v;
			LL X = x0;
			LL Y = y0;
			v.push_back(PLL(X, Y));
			for (int i = 1; i <= nn - 1; ++i)
			{
			  X = (A * X + B) % M;
			  Y = (C * Y + D) % M;
			  v.push_back(PLL(X, Y));
			}

			sort(v.begin(), v.end(), pllless);

			int ctr = 0;
			for (int i1 = 0; i1 < sz(v); ++i1)
			{
				for (int i2 = i1 + 1; i2 < sz(v); ++i2)
				{
					for (int i3 = i2 + 1; i3 < sz(v); ++i3)
					{
						if (neq(v[i1], v[i2]) && neq(v[i1], v[i3]) && neq(v[i2], v[i3]))
						{
							if ((((v[i1].first + v[i2].first + v[i3].first) % 3) == 0) &&
							    (((v[i1].second + v[i2].second + v[i3].second) % 3) == 0))
							{
								++ctr;
							}
						}
					}	
				}
			}

			outf << "Case #" << n << ": " << ctr << endl;
		}
	}
};



set<vector<int> > mem;

class Q12
{
private:
	Q12() {};
	static set<int> disp(int c)
	{
		set<int> res;
		for (int p = 2; p <= c; ++p)
		{
			while (c % p == 0)
			{
				c = c / p;
				if (res.find(p) == res.end())
				{
					res.insert(p);
				}
			}
		}
		return res;
	}
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
			int A, B, P;
			inpf >> A >> B >> P;

			vector<int> cat(B - A + 1, -1);
			int lastcat = -1;
			queue<int> q;
			int toC = B - A + 1;
			while (toC > 0)
			{
				if (q.empty())
				{
					for (int c = A; c <= B; ++c)
					{
						if (cat[c - A] < 0)
						{
							q.push(c);
							++lastcat;
							cat[c - A] = lastcat;
							break;
						}
					}
				}

				int c = q.front(); q.pop();
				for (int c2 = A; c2 <= B; ++c2)
				{
					if ((c2 != c) && (cat[c2 - A] < 0))
					{
						set<int> pr1 = disp(c);
						set<int> pr2 = disp(c2);
						for (set<int>::const_iterator it = pr1.begin(); it != pr1.end(); ++it)
						{
							if ((pr2.find(*it) != pr2.end()) && (*it >= P))
							{
								cat[c2 - A] = cat[c - A];
								q.push(c2);
								break;
							}
						}
					}
				}

				--toC;
			}			

			outf << "Case #" << n << ": " << lastcat + 1 << endl;
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
			mem.clear();

			int K, nn;
			inpf >> K >> nn;

			vector<int> d;
			for (int i = 0; i < nn; ++i)
			{
				int di;
				inpf >> di;
				d.push_back(di);
			}

			vector<int> deck(K, -1);
			vector<int> empties;
			for (int i = 0; i < K; ++i)
			{
				empties.push_back(i);
			}

			int curpos = 0;
			for (int i = 1; i <= K; ++i)
			{
				int ctr = 1;
				while (ctr < i)
				{
					while (deck[curpos] >= 0)
					{
						++curpos;
						if (curpos >= K)
							curpos = 0;
					}
					++ctr;
					++curpos;
					if (curpos >= K)
						curpos = 0;
					while (deck[curpos] >= 0)
					{
						++curpos;
						if (curpos >= K)
							curpos = 0;
					}
				}
				deck[curpos] = i;
				++curpos;
				if (curpos >= K)
					curpos = 0;
			}

			outf << "Case #" << n << ":";
			for (int i = 0; i < sz(d); ++i)
			{
				outf << " " << deck[d[i] - 1];
			}	
			outf << endl;
		}
	}
};



int _tmain(int argc, _TCHAR* argv[])
{
	//Q11::go("input.txt", "output.txt");
	//Q12::go("input.txt", "output.txt");
	Q13::go("input.txt", "output.txt");

	cout << endl;
	getchar();
	return 0;
}

