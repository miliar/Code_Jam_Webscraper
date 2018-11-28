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

using namespace std;

typedef vector <int> VI;
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPV(i, a, b) for (int i = (a); i <= (b); ++i)
#define PB push_back
#define ALL(x) x.begin(),x.end()

char strin[10000];

int k;

int main()
{
	ifstream in("D-small.in");
	ofstream out("D-small.out");
	int T, j;
	in >> T;
	cout << T << endl;
	VI aux;
	for (j = 1; j <= T; j++) {
		aux.clear();
		string S = "";
		in >> k;
		in >> S;
		int R = 10000000;
		REP(i, k) aux.PB(i);
		do {
			int counter = 0;
			string rez = "";
			REP(v, S.size())
			{
				if (v % k == 0 && v != 0) counter++;
				rez += S[counter * k + aux[v%k]];
			}
			int sol = 1;
			for (int p = 1; p < rez.size(); p++) 
				if (rez[p] != rez[p-1]) sol++;
			R = min(R, sol);
		} while (next_permutation(ALL(aux)));
		
		out << "Case #" << j << ": " << R << endl;
	}
	return 0;
}
