#include <fstream>
#include <cstdlib>

using namespace std;

fstream fin, fout;

void process()
{
	int n;
	fin >> n;

	int Orange[2]; // 0: time, 1: pos
	int Blue[2]; // 0: time, 1:pos

	Orange[0] = 0;
	Orange[1] = 1;
	Blue[0] = 0;
	Blue[1] = 1;

	int last = 0;

	for (int i = 0; i < n; ++i)
	{
		char ch;
		int pos;
		fin >> ch >> pos;
		if (ch == 'O')
		{
			int temp = abs(Orange[1] - pos) + 1 + Orange[0];
			if (temp <= last) temp = last + 1;
			Orange[0] = temp;
			Orange[1] = pos;
			last = temp;
		}
		else // ch == 'B'
		{
			int temp = abs(Blue[1] - pos) + 1 + Blue[0];
			if (temp <= last) temp = last + 1;
			Blue[0] = temp;
			Blue[1] = pos;
			last = temp;
		}
	}

	fout << last;
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
