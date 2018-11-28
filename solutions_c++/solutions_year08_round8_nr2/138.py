#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

	int tnum, test;
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int n;
	string colors[20];
	int color[20];
	int cnum;

	int from[20], to[20];

	int b[10000];

	int getcolor(string col) {
		for (int i = 0; i < cnum; i++) {
			if (col == colors[i])
				return i;
		}
		colors[cnum] = col;
		cnum++;
		return cnum-1;
	}

	int cb(int N) {
		int res = 0;
		for (int i =  0; i < n; i++)
			if ((1 << i) & N)
				res ++;

		return res;
	}

	bool checkboard()
	{
		int buf[20];
		memset(buf, 0, sizeof(buf));
		for (int i = 0; i < 10000; i++) {
			if (b[i] < 0)
				return false;
			buf[b[i]]++;
		}
		int cols = 0;
		for (int i = 0; i < 20; i++)
			if (buf[i])
				cols++;
		return cols <= 3;
	}

int main()
{
	fin >> tnum;
	for (test = 0; test < tnum; test++) {
		cnum = 0;
		fin >> n;
		string col;
		for (int i = 0; i < n; i++) {
			fin >> col >> from[i] >> to[i];
			from[i]--; to[i]--;
			color[i] = getcolor(col);
		}
		int maxim = 1 << n;
		int answer = 100;
		for (int mask = 1; mask < maxim; mask++) {
			memset(b, -1, sizeof(b));
			for (int i =0 ; i < n; i++) {
				if (mask & (1 << i)) {
					for (int j = from[i]; j <= to[i]; j++) {
						b[j] = color[i];
					}
				}
			}
		
			if (checkboard()) {
				answer = min(answer, cb(mask));
			}
		}
		
		fout << "Case #" << (test + 1) << ": ";
		if (answer == 100)
			fout <<  "IMPOSSIBLE";
		else
			fout << answer ;
		fout << endl;
	}
	return 0;
}
