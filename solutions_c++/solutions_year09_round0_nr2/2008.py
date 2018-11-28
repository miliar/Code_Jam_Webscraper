#include <iostream>
#include <fstream>
#include <cstdlib> // for exit function
#include <algorithm>
#include <math.h>
#include <set>
#include <list>
#include <queue>
#include <vector>
#include <string>

using namespace std;

const int SIZE = 101;

int t;
struct mapp {
	int h;
	int w;
	int alt[SIZE][SIZE];
	pair<int, int> sink[SIZE][SIZE];
};

vector<mapp*> maps;

void getNextCell(mapp* m, int i, int j, int* outi, int* outj) {
	*outi = i;
	*outj = j;
	int alt1 = INT_MAX;
	int alt2 = INT_MAX;
	int alt3 = INT_MAX;
	int alt4 = INT_MAX;
	//N
	if (i - 1 >= 0)
		alt1 = m->alt[i - 1][j];
	//W
	if (j - 1 >= 0)
		alt2 = m->alt[i][j - 1];
	//S
	if (i + 1 < m->h)
		alt3 = m->alt[i + 1][j];
	//E
	if (j + 1 < m->w)
		alt4 = m->alt[i][j + 1];
	// calc min
	int minimum = min(m->alt[i][j], min(alt1, min(alt2, min(alt3, alt4))));
	if (minimum == m->alt[i][j])
		;
	else if (minimum == alt1) //N
		*outi = *outi - 1;
	else if (minimum == alt2) //W
		*outj = *outj - 1;
	else if (minimum == alt4) //E
		*outj = *outj + 1;
	else if (minimum == alt3) //S
		*outi = *outi + 1;
}

void flow(mapp* m, int i, int j) {
	if (i < 0 || i >= m->h || j < 0 || j >= m->w)
		return;
	int nexti = 0;
	int nextj = 0;
	getNextCell(m, i, j, &nexti, &nextj);
	if (i == nexti && j == nextj)
		m->sink[i][j] = make_pair<int, int>(i, j);
	else
		if (m->sink[nexti][nextj].first != -1)
			m->sink[i][j] = m->sink[nexti][nextj];
		else {
			flow(m, nexti, nextj);
			m->sink[i][j] = m->sink[nexti][nextj];
		}
}

void solve(ofstream& outdata) {
	for (int i = 0; i < t; i++) {
		outdata << "Case #" << (i + 1) << ":" << endl;
		cout << "Progress: " << i << " out of " << t << endl;
		mapp* m = maps[i];

		//for (int j = 0; j < m->h; j++) {
		//	for (int k = 0; k < m->w; k++) {
		//		cout << m->alt[j][k] << " ";
		//	}
		//	cout << endl;
		//}
		//cout << endl;

		for (int j = 0; j < m->h; j++) {
			for (int k = 0; k < m->w; k++) {
				flow(m, j, k);
			}
		}
		int letters[SIZE][SIZE];
		for (int j = 0; j < m->h; j++) {
			for (int k = 0; k < m->w; k++) {
				letters[j][k] = -1;
			}
		}
		int count = -1;
		for (int j = 0; j < m->h; j++) {
			for (int k = 0; k < m->w; k++) {
				pair<int, int> p = m->sink[j][k];
				if (letters[j][k] == -1) {
					count++;
					letters[j][k] = count;
				}
				for (int j2 = j; j2 < m->h; j2++) {
					for (int k2 = 0; k2 < m->w; k2++) {
						if (letters[j2][k2] != -1)
							continue;
						if (m->sink[j2][k2] == p) {
							letters[j2][k2] = count;
						}
					}
				}
			}
		}
		for (int j = 0; j < m->h; j++) {
			for (int k = 0; k < m->w; k++) {
				outdata << (char)('a' + letters[j][k]);
				if (k < m->w - 1)
					outdata << " ";
			}
			outdata << endl;
		}
		//cout << "Sinks:" << endl;
		//for (int j = 0; j < m->h; j++) {
		//	for (int k = 0; k < m->w; k++) {
		//		cout << "(" << m->sink[j][k].first << "," << m->sink[j][k].second << ") ";
		//	}
		//	cout << endl;
		//}
	}
}

int main() {
	ifstream indata; 
	ofstream outdata;
	indata.open("A-small.in"); // opens the file
	outdata.open("A-small.out");
	if(!indata) { // file couldn't be opened
		cerr << "Error: file could not be opened" << endl;
		exit(1);
	}
	indata >> t;
	
	maps.reserve(t);
	for (int i = 0; i < t; i++) {
		mapp* m = new mapp();
		memset(m, 0, sizeof(mapp));
		indata >> m->h;
		indata >> m->w;
		for (int j = 0; j < m->h; j++) {
			for (int k = 0; k < m->w; k++) {
				indata >> m->alt[j][k];
				m->sink[j][k] = make_pair(-1, -1);
			}
		}
		maps.push_back(m);
	}

	solve(outdata);	

	outdata.close();
	return 0;
}