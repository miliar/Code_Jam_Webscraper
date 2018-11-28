#include <iostream>
#include <fstream>
using namespace std;

char buffer[40][40];
int number[40];

int main()
{
	fstream file("A.in");
	fstream output("A.out", ios_base::out);

	int caseCount = 0, caseIndex = 0;
	file >> caseCount;

	while (++caseIndex <= caseCount)
	{
		int n;
		file >> n;
		for (int i = 0; i < n; ++ i)
		{
			for (int j = 0; j < n; ++ j)
			{
				file >> buffer[i][j];
				number[i] = 0;
				for (int k = n - 1; k >= 0; -- k) {
					if (buffer[i][k] == '1') {
						number[i] = k;
						break;
					}
				}
			}
		}

		int ret = 0;
		for (int i = 0; i < n; ++ i)
		{
			int next = i;
			for (; next < n && number[next] > i; ++ next);
			for (int j = next; j > i; -- j)
			{
				swap(number[j], number[j - 1]);
				++ ret;
			}
		}

		output << "Case #" << caseIndex << ": "<< ret << endl;
	}



	file.close();
	output.close();
	return 0;
}