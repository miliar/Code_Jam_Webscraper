#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

//////////////////////////////////////////////////////////////////////////

struct BUTTON
{
	char color;
	int num;
};

struct ONE_CASE
{
	int N;
	int bN;
	int oN;
	BUTTON seq[100];
	int btnB[100];
	int btnO[100];
};

//////////////////////////////////////////////////////////////////////////

int T;

ONE_CASE allCases[100];
int results[100];

int LoadData(char * filename)
{
	char color;
	int N, num, bN, oN;
	fstream f(filename);
	if (!f.is_open()) {
		return 0;
	}

	f >> T;

	for (int i = 0; i < T; ++i) {
		f >> N;
		allCases[i].N = N;
		bN = oN = 0;
		for (int j = 0; j < N; ++j) {
			f >> color >> num;
			allCases[i].seq[j].color = color;
			allCases[i].seq[j].num = num;
			if (color == 'O') {
				allCases[i].btnO[oN++] = num;
			} else {
				allCases[i].btnB[bN++] = num;
			}
		}

		allCases[i].bN = bN;
		allCases[i].oN = oN;
	}

	return 1;
}

void Process()
{
	int no;
	for (no = 0; no < T; ++no) {
		ONE_CASE * p = allCases + no;
		int sec = 0;
		int i, curO, curB, nextO, nextB;
		char color;
		int N = p->N, bN = p->bN, oN = p->oN, bNidx = 0, oNidx = 0;

		curO = curB = 1;

		for (i = 0; i < N;) {
			if (bNidx < bN) {
				nextB = p->btnB[bNidx];
			} else {
				nextB = 0;
			}

			if (oNidx < oN) {
				nextO = p->btnO[oNidx];
			} else {
				nextO = 0;
			}

			color = p->seq[i].color;

			if (color == 'O') {
				if (nextO) {
					if (curO == nextO) {
						++nextO;
						++oNidx;

						++i;
					} else if (curO < nextO){
						++curO;
					} else {
						--curO;
					}
				}
				if (nextB) {
					if (curB == nextB) {
						;
					} else if (curB < nextB){
						++curB;

					} else {
						--curB;

					}
				}
			} else {
				if (nextB) {
					if (curB == nextB) {
						++nextB;
						++bNidx;
						++i;
					} else if (curB < nextB){
						++curB;
					} else {
						--curB;
					}
				}
				if (nextO) {
					if (curO == nextO) {
						;
					} else if (curO < nextO){
						++curO;

					} else {
						--curO;
					}
				}

			}

			++sec;
		}

		results[no] = sec;
	}
}

void Output()
{
	stringstream ss;
	fstream f("output.txt", ios::out | ios::trunc);

	int secs;
	for (int i = 0; i < T; ++i) {
		secs = results[i];
		ss << "Case #" << i + 1 <<": " << secs << "\r\n";
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