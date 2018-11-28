// A.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::ifstream in ("A.in");
std::ofstream out ("A.out");

int K;
long long N, A, B, C, D, x0, y0, M;
std::vector <long long> X;
std::vector <long long> Y;

void generate()
{
	X.push_back(x0);
	Y.push_back(y0);
	for (int i=1; i<N; i++)
	{
		long long x = (A * X[i-1] + B) % M;
		long long y = (C * Y[i-1] + D) % M;
		X.push_back(x);
		Y.push_back(y);
		//out << x  << " " << y << "\n";
	}
}

void input()
{
	in >> N >> A >> B >> C >> D >> x0 >> y0 >> M;
	X.clear();
	Y.clear();
}

int solve()
{
	int result = 0;
	for (int i=0; i<X.size(); i++)
	{
		for (int j=0; j<X.size(); j++)
		{
			if (i!=j)
			{
				for (int m=0; m<X.size(); m++)
				{
					if (m!=i && m!=j)
					{
						if (((X[i]+X[j]+X[m])%3 == 0) && ((Y[i]+Y[j]+Y[m]) %3 == 0))
							result++;
					}
				}
			}
		}
	}
	return result;
}

int main()
{
	in >> K;
	for (int k=0; k<K; k++)
	{
		input();
		generate();
		out << "Case #" << k+1 << ": "  << solve()/6 << "\n";
	}
	return 0;
}

