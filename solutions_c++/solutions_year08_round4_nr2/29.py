#include <iostream>
#include <fstream>

using namespace std;

int T;
long long N, M, A;

long long factor(long long P)
{
	if (P == 0) return 0;
	long long start = P / M;
	if (start * M < P) start++;
	while (start <= N && P % start > 0) start++;
	if (start <= N)
		return start;
	else
		return -1;
}

int main()
{
	ifstream input;
	ofstream output;
	input.open("B-large.in");
	output.open("B-large.out");

	input >> T;
	for (int c = 0; c < T; c++)
	{
		input >> N >> M >> A;

		long long x2, y2, x3, y3;
		x2 = -1;

		long long p = 0;
		while (A + p <= N * M)
		{
			long long x = factor(A + p);
			long long y = factor(p);
			
			if (x >= 0 && y >= 0)
			{
				x2 = x;
				y3 = (A + p) / x;
				x3 = y;
				if (x3 > 0)
					y2 = p / y;
				else
					y2 = 0;
				break;
			}
			p++;
		}

		output << "Case #" << c + 1 << ": ";
		if (x2 >= 0)
			output << "0 0 " << x2 << " " << x3 << " " << y2 << " " << y3 << endl;
		else
			output << "IMPOSSIBLE" << endl;
	}

	input.close();
	output.close();
}

