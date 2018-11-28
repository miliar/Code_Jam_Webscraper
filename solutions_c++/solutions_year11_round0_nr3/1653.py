#include <fstream>

using namespace::std;
int main()
{
	int T, N;
	int c, result, total;
	int min;
	int i, j;
	ifstream input("D:\\in", ifstream::in);
	ofstream output("D:\\out", ofstream::out);
	input >> T;
	total = 0;
	for (i = 0; i < T; i++)
	{
		input >> N;
		input >> c;
		min = c;
		result = c;
		total += c;
		for (j = 1; j < N; j++)
		{
			input >> c;
			total += c;
			result ^=  c;
			if (min > c)
				min = c;
		}

		if (result != 0)
		{
			output << "Case #" << i + 1 << ": NO" << endl;
		}
		else
		{
			output << "Case #" << i + 1 << ": " << total - min << endl;
		}

		total = 0;
	}
	return 0;
}