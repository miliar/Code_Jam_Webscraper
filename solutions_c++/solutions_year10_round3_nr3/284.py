#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>
#include <math.h>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <fstream>
#include <cstdio>
#include <utility>

using namespace std;

typedef vector <int> VI;
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPV(i, a, b) for (int i = (a); i <= (b); ++i)
#define PB push_back
#define ALL(x) x.begin(),x.end()

int Table[600][600];
const int iksz[]     = {1, 0, -1, 0};
const int ipszilon[] = {0, 1, 0, -1};

bool verif(int x, int y, int size) {
	for (int i = x; i < x+size; i++)
		for (int j = y; j < y+size; j++) {
			int valCur = Table[j][i];
			if (valCur == 2) 
				return false;
			for (int a = 0; a < 4; a++) {
				int tmpX = i + iksz[a];
				int tmpY = j + ipszilon[a];
				if (tmpX < x || tmpX >= x+size || tmpY < y || tmpY >= y+size)
					continue;
				int tmp = Table[tmpY][tmpX];
				if (tmp == 2)
					return false;
				if (tmp == valCur)
					return false;
			}
		}
	for (int i = x; i < x+size; i++)
		for (int j = y; j < y+size; j++)
			Table[j][i] = 2;

	return true;
}

void kiir(int M, int N) {
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++)
			cout << Table[i][j] << " ";
		cout << endl;
	}
}

int main() {
	ifstream in("C-small.in");
	ofstream out("C-small.out");
	int T;
	in >> T;
	for (int v = 1; v <= T; v++) {
		cout << v << endl;
		int M, N;
		in >> M >> N;
		for (int i = 0; i < M; i++) {
			string S;
			in >> S;
			int index = 0;
			for (size_t j = 0; j < S.size(); j++) {
				int hexDig;
				if ('0' <= S[j] && S[j] <= '9') hexDig = S[j] - '0';
				if ('A' <= S[j] && S[j] <= 'F') hexDig = S[j] - 'A' + 10;
				for (int a = 0; a < 4; a++)
					Table[i][index++] = (hexDig >> (3 - a)) & 1;
			}
		}

		vector <int> R(600, 0);
		for (int i = min(M, N); i > 0; i--)
			for (int k = 0; k < M - i + 1; k++)
				for (int j = 0; j < N - i + 1; j++)
					if (verif(j, k, i))
						R[i]++;

		int rez = 0;
		for (int i = 0; i < 600; i++)
			if (R[i] > 0)
				rez++;
		out << "Case #" << v << ": " << rez << endl;
		for (int i = 599; i > 0; i--)
			if (R[i] > 0)
				out << i << " " << R[i] << endl;
	}
	return 0;
}



