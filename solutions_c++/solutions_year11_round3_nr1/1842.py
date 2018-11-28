#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

//////////////////////////////////////////////////////////////////////////


struct ONE_CASE
{
	int R;
	int C;
	char P[50][50];
};

//////////////////////////////////////////////////////////////////////////

int T;

ONE_CASE allCases[50];
int results[50];

int LoadData(char * filename)
{
	fstream f(filename);
	if (!f.is_open()) {
		return 0;
	}

	int R, C;
	char ch;
	f >> T;

	for (int i = 0; i < T; ++i) {
		f >> R;
		allCases[i].R = R;
		f >> C;
		allCases[i].C = C;

		for (int j = 0; j < R; ++j) {
			for (int k = 0; k < C; ++k) {
				f >> ch;
				allCases[i].P[j][k] = ch;
			}
		}
	}

	return 1;
}

void Process()
{
	int no;
	int i, j;
	ONE_CASE * p;

	for (no = 0; no < T; ++no) {
		p = &allCases[no];

		for (i = 0; i < p->R; ++i) {
			for (j = 0; j < p->C; ++j) {
				if (p->P[i][j] == '#') {

					if (i < (p->R - 1) && j < (p->C - 1)) {
						if (p->P[i][j+1] == '#' &&
							p->P[i+1][j] == '#' &&
							p->P[i+1][j+1] == '#') {
								p->P[i][j] = '/';
								p->P[i][j+1] = '\\';
								p->P[i+1][j] = '\\';
								p->P[i+1][j+1] = '/';
						}
					}
				}
			}
		}

		results[no] = 1;
		for (i = 0; i < p->R; ++i) {
			for (j = 0; j < p->C; ++j) {
				if (p->P[i][j] == '#') {
					results[no] = 0;
				}
			}
		}
	}
}

void Output()
{
	stringstream ss;
	string s;
	fstream f("output.txt", ios::out | ios::trunc);

	int i, j, k;
	ONE_CASE * p;
	for (i = 0; i < T; ++i) {
		if (results[i] == 0) {
			ss << "Case #" << i + 1 << ":\r\n" << "Impossible\r\n";
		}
		else {
			p = &allCases[i];
			ss << "Case #" << i + 1 << ":\r\n";
			for (j = 0; j < p->R; ++j) {
				for (k = 0; k < p->C; ++k) {
					ss << p->P[j][k];
				}
				ss << "\r\n";
			}
			ss << "\r\n";
		}

		s = ss.str();
		f << ss.str();

		ss.str("");
	}

	f.close();
}

int main(int argc, char * agrv[])
{
	if (!LoadData("A-large.in")) {
		return -1;
	}

	Process();
	Output();

	return 0;
}