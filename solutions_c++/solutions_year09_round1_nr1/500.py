#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

bool flags[100000];
bool bases[11];

bool test(int number, int base)
{
	memset(flags, false, sizeof(flags));
	while (true)
	{
		if (flags[number]) {
			return false;
		}
		flags[number] = true;
		int ret = 0;
		while (number > 0)
		{
			int tmp = number % base;
			ret += tmp * tmp;
			number /= base;
		}
		if (ret == 1) {
			return true;
		}
		number = ret;
	}
}

int main()
{
	fstream file("A.in");
	fstream output("A.out", ios_base::out);

	int caseIndex = 0, caseCount = 0;
	file >> caseCount;
	file.get();

	while (++ caseIndex <= caseCount)
	{
		memset(bases, false, sizeof(bases));
		string line;
		getline(file, line);
		istringstream ss(line);
		int t;
		while (ss >> t)
		{
			bases[t] = true;
		}
		int ret = 2;
		while (true)
		{
			bool done = false;
			for (int i = 2; i < 11 && !done; ++ i)
			{
				if (bases[i] && !test(ret, i)) {
					done = true;
				}
			}
			if (!done) {
				output << "Case #" << caseIndex << ": " << ret << endl;
				break;
			}
			++ ret;
		}
	}

	file.close();
	output.close();
	return 0;
}