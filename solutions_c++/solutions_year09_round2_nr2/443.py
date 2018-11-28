#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int cases = 0;
	fin >> cases;
	for (int i = 0; i < cases; i++)
	{
		string number;
		fin >> number;

		bool isDecreasing = true;
		for (int j = 1; j < (int)number.size(); j++)
		{
			if (number[j] > number[j - 1])
			{
				isDecreasing = false;
				break;
			}
		}

		string result = "";
		if (isDecreasing)
		{
			sort(number.begin(), number.end());
			int nulls = 1;
			for (int j = 0; j < (int)number.size(); j++)
			{
				if (result == "" && number[j] == '0')
				{
					nulls++;
				}
				else
				{
					if (result == "")
					{
						result += number[j];
						result += string(nulls, '0');
					}
					else
					{
						result += number[j];
					}
				}
			}
		}
		else
		{
			next_permutation(number.begin(), number.end());
			result = number;
		}
		fout << "Case #" << i + 1 << ": " << result << endl;
	}
	fin.close();
	fout.close();
	return 0;
}