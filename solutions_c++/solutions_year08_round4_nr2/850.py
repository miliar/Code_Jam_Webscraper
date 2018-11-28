// B.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>

std::ifstream in ("B.in");
std::ofstream out ("B.out");

int K;
int A;
int X1;
int Y1;
long long X2, Y2, X3, Y3;
int N, M;
bool possible;

void input()
{
	in >> N >> M >> A;
}

void solve1()
{
	possible = false;
	for (X1 = 0; X1 <=N; X1++)
	{
		for (X3 = 0; X3<= N; X3++)
		{
			for (Y2=0; Y2<=M; Y2++)
			{
				for (Y3=0; Y3<=M; Y3++)
				{
					long long p = Y2*X3 - Y2*X1 + Y3*X1;
					if (p==A)
					{
						possible = true;
						X2 = 0;
						Y1 = 0;
						break;
					}
				}
				if (possible)
					break;
			}
			if (possible)
					break;
		}
		if (possible)
					break;
	}
}

void solve()
{
	int x = sqrt ((double)A);
	int d1, d2;
	possible = false;
	while (x>0 && possible!=true)
	{
		while (A%x)
		{
			x--;
		}
		d1 = x;
		d2 = A/x;

		if (std::min(d1, d2)> std::min (N, M) || std::max(d1, d2)> std::max (N, M) )
		{
			possible = false;
			x--;
			
		}
		else
			possible = true;
	}
	if (!possible)
	{
		solve1();
		return;
	}

	possible = true;
	X1 = 0;
	Y1 = 0;
	if (N < M)
	{
		X2 = std::min (d1, d2);
		Y2 = 0;
		X3 = 0;
		Y3 = std::max (d1, d2);
	}
	else
	{
		X2 = std::max (d1, d2);
		Y2 = 0;
		X3 = 0;
		Y3 = std::min (d1, d2);
	}
	
}



int main()
{
	in >>K;
	for (int k=0; k<K; k++)
	{
		input();
		solve1();
		if (!possible)
		{
			out << "Case #" << k+1 << ": IMPOSSIBLE" <<  "\n";
		}
		else
		{
			out << "Case #" << k+1 << ": " << X1 << " " << Y1 << " "<< X2 << " "<< Y2 << " "<< X3 << " "<< Y3 <<  "\n";
		}
	}
	return 0;
}