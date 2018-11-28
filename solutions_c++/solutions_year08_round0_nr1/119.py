#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

#define INF 1000000000

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	string s[128];
	string q[1024];
	int sn, qn;

	int test, tnum;
	int result;

	void readdata()
	{
		char buf[1024];
		result = 0;
		fin >> sn;
		fin.getline(buf, 1024);
		for (int i = 0; i < sn; i++) {
			fin.getline(buf, 1024);
			s[i] = string(buf);
		}
		fin >> qn;
		fin.getline(buf, 1024);
		for (int i = 0; i < qn; i++) {
			fin.getline(buf, 1024);
			q[i] = string(buf);
		}
	}

	void run()
	{
		if (qn < 2) {
			result = 0;
			return;
		}
		int a[128];
		memset(a, 0, sizeof(a));

		for (int j = 0; j < sn; j++) {
			if (s[j] == q[qn - 1])
				a[j] = INF;
		}

		for (int i = qn - 1; i >= 1; i--) {
			for (int j = 0; j < sn; j++) {
				if (s[j] == q[i]) {
					int mi = INF;
					for (int k = 0; k < sn; k++) {
						if (k == j) continue;
						mi = min(mi, a[k]);
					}
					a[j] = mi + 1;
				}
			}
			for (int j = 0; j < sn; j++) {
				if (s[j] == q[i - 1])
					a[j] = INF;
			}
		}
		result = a[0];
		for (int i = 1; i < sn; i++)
			result = min(result, a[i]);
	}

	void outputdata()
	{
		fout << "Case #" << (test + 1) << ": " << result << endl;
	}

int main()
{
	fin >> tnum;
	for (test = 0; test < tnum; test++) {
		readdata();
		run();
		outputdata();
	}
	return 0;
}
