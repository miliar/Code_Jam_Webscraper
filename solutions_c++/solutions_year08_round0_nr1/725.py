// universe.cpp : main project file.

#include "stdafx.h"
#include <fstream>
#include <string>
#include <set>

using namespace std;

int main()
{
    ifstream fin ("A-large.in");
	ofstream fout ("file.out");

	int N;
	fin >> N;
	for (int i = 0; i < N; ++i) {
		int S; int Q;
		fin >> S;
		string temp;
		getline(fin, temp);
		for (int j = 0; j < S; ++j) {
			getline(fin, temp);
		}

		set <string> used;
		int count = 0;

		fin >> Q;
		getline(fin, temp);
		for (int k = 0; k < Q; ++k) {
			getline(fin, temp);
			used.insert(temp);
			if (used.size() == S) {
				count++;
				used.clear();
				used.insert(temp);
			}
		}

		fout << "Case #" << i + 1 << ": " << count << endl;
	}
    return 0;
}
