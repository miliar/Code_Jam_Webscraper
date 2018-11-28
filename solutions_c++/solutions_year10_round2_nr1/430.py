#include <iostream>
#include <fstream>
#include <set>
#include <string>

using namespace std;

int main()
{
	ifstream inFile("A-large.in");
	ofstream outFile("A-large.out");

	int T;
	inFile >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int N, M;
		inFile >> N >> M;
		set<string> fs;

		for (int i = 0; i < N; i++)
		{
			string dir;
			inFile >> dir;
			fs.insert(dir);
		}
		int mkdirs = 0;
		for (int i = 0; i < M; i++)
		{
			string dir;
			inFile >> dir;
			int a = 0;
			int b = a;
			while ((b = dir.find('/', b + 1)) != string::npos)
				if (fs.insert(dir.substr(a, b - a)).second)
					mkdirs++;
			if (fs.insert(dir).second)
				mkdirs++;
		}

		outFile << "Case #" << nTestCase << ": " << mkdirs << endl;
	}

	return 0;
}
