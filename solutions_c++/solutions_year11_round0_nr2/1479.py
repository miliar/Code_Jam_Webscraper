#include <fstream>
#include <string>
#include <cstring>

#include <iostream>

using namespace std;

fstream fin, fout;

void process()
{
	int c, d;
	char combine[255][255];
	bool destroy[255][255];

	memset(combine, 0, sizeof combine);
	memset(destroy, 0, sizeof destroy);

	fin >> c;
	for (int i = 0; i < c; ++i)
	{
		string temp;
		fin >> temp;
		combine[temp[0]][temp[1]] = temp[2];
		combine[temp[1]][temp[0]] = temp[2];
	}

	fin >> d;
	for (int i = 0; i < d; ++i)
	{
		string temp;
		fin >> temp;
		destroy[temp[0]][temp[1]] = true;
		destroy[temp[1]][temp[0]] = true;
	}

	int n;
	fin >> n;

	char answer[110];
	int len = 0;

	for (int i = 0; i < n; ++i)
	{
		char ch;
		fin >> ch;
		if (len >= 1 && combine[answer[len - 1]][ch] != 0)
			answer[len - 1] = combine[answer[len - 1]][ch];
		else {
			bool empty = false;
			for (int j = 0; j < len; ++j)
				if (destroy[answer[j]][ch])
				{
					len = 0;
					empty = true;
					break;
				}
			if (!empty)
			{
				answer[len] = ch;
				++len;
			}
		}
	}

	if (len >= 1) fout << answer[0];
	for (int i = 1; i < len; ++i)
		fout << ", " << answer[i];
}

int main()
{
	fin.open("in.txt", fstream::in);
	fout.open("out.txt", fstream::out);

	int testcase;
	fin >> testcase;
	for (int i = 1; i <= testcase; ++i)
	{
		fout << "Case #" << i << ": [";
		process();
		fout << "]" << endl;
	}

	fin.close();
	fout.close();
	return 0;
}
