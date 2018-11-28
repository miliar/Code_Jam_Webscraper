#include <fstream>
#include <climits>

using namespace std;

fstream fin, fout;

void process()
{
	int n;
	fin >> n;

	int sum = 0;
	long long answer = 0;
	int min = INT_MAX;

	for (int i = 0; i < n; ++i)
	{
		int temp;
		fin >> temp;
		sum ^= temp;
		answer += temp;
		if (temp < min) min = temp;
	}

	if (sum == 0)
		fout << answer - min;
	else
		fout << "NO";
}

int main()
{
	fin.open("in.txt", fstream::in);
	fout.open("out.txt", fstream::out);

	int testcase;
	fin >> testcase;

	for (int i = 1; i <= testcase; ++i)
	{
		fout << "Case #" << i << ": ";
		process();
		fout << endl;
	}

	fin.close();
	fout.close();
	return 0;
}
