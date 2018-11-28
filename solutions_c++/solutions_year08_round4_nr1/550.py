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



struct Node
{
	bool isLeaf;
	bool canChange;
	bool isAnd;
	int to0;
	int to1;
};

class Q11
{
private:
	Q11() {};
	static int left(int p)
	{
		return p * 2 + 1;
	}
	static int right(int p)
	{
		return p * 2 + 2;
	}
	static int parent(int c)
	{
		if (c == 0)
			return -1;
		return (c - 1)/ 2;
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
			int M, V;
			inpf >> M >> V;

			vector<Node> v;
			for (int i = 0; i < (M - 1) / 2; ++i)
			{
				int G, C;
				inpf >> G >> C;

				Node n;
				n.canChange = (C == 1);
				n.isAnd = (G == 1);
				n.to0 = -2;
				n.to1 = -2;
				n.isLeaf = false;

				v.push_back(n);
			}

			for (int i = 0; i < (M + 1) / 2; ++i)
			{
				int I;
				inpf >> I;

				Node n;
				n.canChange = false;
				n.isAnd = false;
				n.to0 = (I == 0) ? 0 : -1;
				n.to1 = (I == 1) ? 0 : -1;
				n.isLeaf = true;

				v.push_back(n);
			}
			int ctr = -1;

			for (int i = sz(v) - 1; i >= 0; --i)
			{
				if (!v[i].isLeaf)
				{
					v[i].to0 = INT_MAX;
					v[i].to1 = INT_MAX;
					if (v[i].isAnd)
					{
						if ((v[left(i)].to0 >= 0) && (v[right(i)].to0 >= 0))
						{
							v[i].to0 = min(v[i].to0, v[left(i)].to0 + v[right(i)].to0);
						}
						if ((v[left(i)].to0 >= 0) && (v[right(i)].to1 >= 0))
						{
							v[i].to0 = min(v[i].to0, v[left(i)].to0 + v[right(i)].to1);
							if (v[i].canChange)
								v[i].to1 = min(v[i].to1, v[left(i)].to0 + v[right(i)].to1 + 1);
						}
						if ((v[left(i)].to1 >= 0) && (v[right(i)].to0 >= 0))
						{
							v[i].to0 = min(v[i].to0, v[left(i)].to1 + v[right(i)].to0);
							if (v[i].canChange)
								v[i].to1 = min(v[i].to1, v[left(i)].to1 + v[right(i)].to0 + 1);
						}
						if ((v[left(i)].to1 >= 0) && (v[right(i)].to1 >= 0))
						{
							v[i].to1 = min(v[i].to1, v[left(i)].to1 + v[right(i)].to1);
						}
					}
					else
					{
						if ((v[left(i)].to0 >= 0) && (v[right(i)].to0 >= 0))
						{
							v[i].to0 = min(v[i].to0, v[left(i)].to0 + v[right(i)].to0);
						}
						if ((v[left(i)].to0 >= 0) && (v[right(i)].to1 >= 0))
						{
							if (v[i].canChange)
								v[i].to0 = min(v[i].to0, v[left(i)].to0 + v[right(i)].to1 + 1);
							v[i].to1 = min(v[i].to1, v[left(i)].to0 + v[right(i)].to1);
						}
						if ((v[left(i)].to1 >= 0) && (v[right(i)].to0 >= 0))
						{
							if (v[i].canChange)
								v[i].to0 = min(v[i].to0, v[left(i)].to1 + v[right(i)].to0 + 1);
							v[i].to1 = min(v[i].to1, v[left(i)].to1 + v[right(i)].to0);
						}
						if ((v[left(i)].to1 >= 0) && (v[right(i)].to1 >= 0))
						{
							v[i].to1 = min(v[i].to1, v[left(i)].to1 + v[right(i)].to1);
						}
					}
					if (v[i].to0 == INT_MAX)
						v[i].to0 = -1;
					if (v[i].to1 == INT_MAX)
						v[i].to1 = -1;

				}
			}


			if (V == 0)
			{
				ctr = v[0].to0;
			}
			else
			{
				ctr = v[0].to1;
			}

			if (ctr >= 0)
			{
				outf << "Case #" << n << ": " << ctr << endl;
			}
			else
			{
				outf << "Case #" << n << ": " << "IMPOSSIBLE" << endl;
			}

			
		}
	}
};


int _tmain(int argc, _TCHAR* argv[])
{
	Q11::go("input.txt", "output.txt");
	//Q12::go("input.txt", "output.txt");
	//Q13::go("input.txt", "output.txt");

	cout << endl << "Complete!" << endl;
	getchar();
	return 0;
}

