#include <fstream>
#include <cmath>

using namespace std;

int digits(int number);
int main()
{
	int T, A, B;
	int n, d;
	int* numbers;
	int PowerOfTen;
	ifstream in("in2.in");
	ofstream out("out.out");
	in >> T;
	for (int i = 0; i < T; i++)
	{
		in >> A >> B;
		if (A < 10)
		{
			out << "Case #" << i + 1 << ": " << 0 << endl;
			continue;
		}
		n = 0;
		d = digits(A) - 1;
		numbers = new int[d];
		PowerOfTen = int(pow(10.0, d));
		for (int j = A; j <= B; j++)
		{
			numbers[0] = (j % 10) * PowerOfTen + j / 10;
			for (int k = 1; k < d; k++)
				numbers[k] = (numbers[k - 1] % 10) * PowerOfTen + numbers[k - 1] / 10;

			for (int k = 0; k < d; k++)
			{
				bool b = 0;
				for (int m = 0; m < k; m++)
					if (numbers[k] == numbers[m])
					{
						b = 1;
						break;
					}
				if (!b && numbers[k] > j && numbers[k] <= B)
					n++;
			}
		}
		out << "Case #" << i + 1 << ": " << n << endl;
	}
	in.close();
	out.close();
	return 0;
}

int digits(int number)
{
	int n = 0;
	while (number)
	{
		n++;
		number /= 10;
	}
	return n;
}