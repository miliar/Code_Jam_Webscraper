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


/*
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
*/
/*
#define abs(x) (((x) >= 0) ? (x) : -(x))

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
			LL A;
			inpf >> N >> M >> A;

			LL x1a = -1;
			LL y1a = -1;
			LL x2a = -1, y2a = -1, x3a = -1, y3a = -1;
			bool stop = false;
			LL x1 = 0;
			LL y1 = 0;
					for (LL x2 = -N; x2 <= N && !stop; ++x2)
					{
						for (LL y2 = -M; y2 <= M && !stop; ++y2)
						{
							for (LL x3 = -N; x3 <= N && !stop; ++x3)
							{
								for (LL y3 = -M; y3 <= M && !stop; ++y3)
								{
									LL S2 = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2);
									if (abs(S2) == A)
									{
										x1a = x1;
										y1a = y1;
										x2a = x2;
										x3a = x3;
										y2a = y2;
										y3a = y3;

										if (x2a < 0)
										{
											x3a += -x2a;
											x1a += -x2a;
											x2a = 0;
										}
										if (x3a < 0)
										{
											x2a += -x3a;
											x1a += -x3a;
											x3a = 0;
										}
										if (y2a < 0)
										{
											y3a += -y2a;
											y1a += -y2a;
											y2a = 0;
										}
										if (y3a < 0)
										{
											y2a += -y3a;
											y1a += -y3a;
											y3a = 0;
										}
										
										if ((x1a <= N) && (x2a <= N) && (x3a <= N) &&
											(y1a <= M) && (y2a <= M) && (y3a <= M))
											stop = true;
									}
								}
							}
						}
					}


			int S = x1a * (y2a - y3a) + x2a * (y3a - y1a) + x3a * (y1a - y2a);
			if (((abs(S) != A) || (x2a > N) || (y2a > M) || (x3a > N) || (y3a > M)) && (stop))
				cout << n;

			if (!stop)
				outf << "Case #" << n << ": " << "IMPOSSIBLE" << endl;	
			else
				outf << "Case #" << n << ": " << x1a << " " << y1a << " " << x2a << " " << y2a << " " << x3a << " " << y3a << endl;		
		}
	}
};
*/


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

			int len = INT_MAX;

			vector<int> v;
			for (int i = 0; i < k; ++i)
				v.push_back(i);

			do
			{
				string P;
				int j = 0;
				for (int i = 0; i < sz(S); i += k)
				{
					for (int l = 0; l < sz(v); ++l)
						P.push_back(S[i + v[l]]);
				}

				int ctr = 0;
				char cur = '-';
				for (int l = 0; l < sz(P); ++l)
				{
					if (P[l] != cur)
					{
						cur = P[l];
						++ctr;
					}
				}
				len = min(len, ctr);
			} while	(next_permutation(v.begin(), v.end()));

			outf << "Case #" << n << ": " << len << endl;		
		}
	}
};

int _tmain(int argc, _TCHAR* argv[])
{
	//Q11::go("input.txt", "output.txt");
	//Q12::go("input.txt", "output.txt");
	Q13::go("input.txt", "output.txt");

	cout << endl << "Complete!" << endl;
	getchar();
	return 0;
}

