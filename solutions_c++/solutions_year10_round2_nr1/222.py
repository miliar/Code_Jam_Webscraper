#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <math.h>
#include <set>

using namespace std;

int main()
{
	ifstream fin("large.in");
	ofstream fout("large.out");
	int M, N, T;
	fin >> T;

	for (int tk = 1; tk <= T; tk++)
	{
		string s;
		set <string> w;
		fin >> N >> M;
		for (int i = 0; i < N; i++)
		{
			fin >> s;
			s.append("/");
			for (int j = 1; j < s.length(); j++)
				if (s[j] == '/') w.insert(s.substr(1, j));
		};
		int k = 0;
		for (int i = 0; i < M; i++)
		{
			fin >> s;
			s.append("/");
			for (int j = 1; j < s.length(); j++)
				if (s[j] == '/' && w.find(s.substr(1, j)) == w.end()) 
				{
					w.insert(s.substr(1, j));
					k++;
				};
		};
		fout << "Case #" << tk << ": " << k << endl;
	};

	fin.close();
	fout.close();
};