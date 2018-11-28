#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int shift(int n, int digits)
{
	int result = 0;
	int mod = n % 10;

	n /= 10;

	while (mod == 0)
	{
		mod = n % 10;
		n /= 10;
	}

	for (int i = 0;i < digits - 1;++i)
	{
		mod *= 10;
	}

	result = mod + n;

	return result;
}

int getDigits(int n)
{
	int result = 0;

	while (n > 0) 
	{
		n /= 10;
		++result;
	}

	return result;
}

int main()
{
	ifstream in("E:\\GoogleCodeJam2012\\QRound\\C-large.in");
	//ifstream in("E:\\GoogleCodeJam2012\\QRound\\B-large.in");
	ofstream out("E:\\GoogleCodeJam2012\\QRound\\c-large-out.txt");
	//ofstream out("E:\\GoogleCodeJam2012\\QRound\\b-large-out.txt");

	if (in.is_open())
	{
		int cases;

	    in >> cases;

		for (int c = 1;c <= cases;++c)
		{
			int result = 0;
			int a, b;

			in >> a >> b;

			int digits = getDigits(a);

			for (int i = a;i < b;++i)
			{
				int currentNum = i;
                int shifted = shift(currentNum, digits);

				while (shifted != currentNum)
				{
					if (shifted > i && shifted <= b)
					{
						++result;
					}

				    shifted = shift(shifted, digits);
				}
			}

			out << "Case #" << c << ": " << result << endl;
		}
	}

	return 0;
}