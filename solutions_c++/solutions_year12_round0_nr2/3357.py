#include <fstream>
#include <map>
#include <string>
#include <iostream>

using namespace std;

int main()
{
	ifstream file("problem_b.txt");

	if (file.is_open())
	{
		int T;
		file >> T;

		string line;
		getline (file, line);

		int N, S, p, tp, div, rst, res;

		for (int i = 1; i <= T; i++)
		{
			file >> N >> S >> p;

			res = 0;
			for (int h = 0; h < N; h++)
			{
				file >> tp;

				if (tp < p) continue;

				div = tp / 3;
				rst = tp % 3;

				switch (rst)
				{
				case 0:
					if (div >= p)
					{
						res++;
					}
					else if (S > 0 && div + 1 >= p)
					{
						res++;
						S--;
					}
					break;
				case 1:
					if (div + 1 >= p)
					{
						res++;
					}
					break;
				case 2:
					if (div + 1 >= p)
					{
						res++;
					}
					else if (S > 0 && div + 2 >= p)
					{
						res++;
						S--;
					}
					break;
				}
			}

			cout << "Case #" << i << ": "<< res << endl;
		}

		file.close();
	}

	return 0;
}
