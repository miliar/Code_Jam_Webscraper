#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>

using namespace std;

int powTen[8];

void init()
{
	powTen[0] = 1;
	for (int i = 1; i < 8; i++)
	{
		powTen[i] = powTen[i - 1] * 10;
	}
}

int digitCount(int x)
{
	int res = 0;
	while (x > 0)
	{
		x = x / 10;
		res++;
	}
	return res;
}

int rotate(int x, int times, int digCnt)
{
	int res = x / powTen[times] + powTen[digCnt - times] * (x % powTen[times]);
	return res;
}

int main(int argc, char* argv[])
{
	ifstream infile ("D:\\work\\codejam\\2012\\Qualifications\\ProbC_RecycledNumbers\\C-large.in");

	init();
	
	int p = digitCount(123456);
	int y = rotate(123456, 6, p);

	if (infile.is_open())
	{
		int T = 0;
		int A = 0; 
		int B = 0;
		infile >> T;
		int ms[10];
		
		for (int p = 1; p <= T; p++)
		{
			int cnt = 0;
			infile >> A >> B;
			int digCnt = digitCount(A);
			int mcnt = 0;

			for (int n = A; n < B; n++)
			{
				memset(ms, 0, 10 * sizeof(int));
				mcnt = 0;	
				for (int q = 1; q < digCnt; q++)
				{
					int m = rotate(n, q, digCnt);
					if (m > n && m <= B)
					{
						bool found = false;
						for (int w = 0; w < mcnt; w++)
						{
							if (ms[w] == m)
							{
								found = true; 
								break;
							}
						}
						if (!found)
						{
							ms[mcnt] = m;
							mcnt++;
							cnt++;
						}
					}
				}
			}

			cout << "Case #" << p << ": " << cnt << endl;
		}
	}

	return 0;
}