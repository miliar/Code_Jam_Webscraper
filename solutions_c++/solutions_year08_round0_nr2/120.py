#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int test, tnum;
	int resA, resB;
	int n;

	void init()
	{
		resA = resB = 0;
		n = 0;
	}

	struct dep {
		int time;
		char type;
		bool is_start;
	} D[500];

	int parsetime(string s)
	{
		int h = (s[0] - '0') * 10 + (s[1] - '0');
		int m = (s[3] - '0') * 10 + (s[4] - '0');
		return h * 60 + m;
	}

	void readdata()
	{
		int T, na, nb;
		string sbeg, send;
		fin >> T;
		fin >> na >> nb;
		for (int i = 0; i < na; i++) {
			fin >> sbeg >> send;
			D[n].time = parsetime(sbeg);
			D[n + 1].time = parsetime(send) + T;
			D[n].type = 'A';
			D[n + 1].type = 'B';
			D[n].is_start = true;
			D[n + 1].is_start = false;
            n += 2;
		}
		for (int i = 0; i < nb; i++) {
			fin >> sbeg >> send;
			D[n].time = parsetime(sbeg);
			D[n + 1].time = parsetime(send) + T;
			D[n].type = 'B';
			D[n + 1].type = 'A';
			D[n].is_start = true;
			D[n + 1].is_start = false;
            n += 2;
		}
	}

	void outputdata()
	{
		fout << "Case #" << (test + 1) << ": " << resA << " " << resB << endl;
	}

	bool Less(dep a, dep b) {
		if (a.time < b.time)
			return true;
		if (a.time == b.time && a.is_start == false && b.is_start == true)
			return true;
		return false;
	}

	void run()
	{
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (Less(D[j], D[i]))
					swap(D[i], D[j]);
			}
		}
		/*for (int i = 0; i < n; i++) {
			cout << D[i].time << ' ' << D[i].time / 60 << ":" << D[i].time % 60 << ' '
				<< D[i].type << ' ' << D[i].is_start << endl;
		}*/
		int restA = 0, restB = 0;
		for (int i = 0; i < n; i++) {
			if (D[i].is_start) {
				if (D[i].type == 'A') {
					if (restA > 0)
						restA--;
					else
						resA++;
				} else {
					if (restB > 0)
						restB--;
					else
						resB++;
				}
			} else {
				if (D[i].type == 'A')
					restA++;
				else
					restB++;
			}
		}
	}

int main()
{
    fin >> tnum;
	for (test = 0; test < tnum; test++) {
		init();
		readdata();
		run();
		outputdata();
	}
	return 0;
}
