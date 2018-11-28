// Hexagon.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<LL> VL;
#define FORE(it, c, T) for(T::iterator it = c.begin(); it != c.end(); it++)
#define FORI(i, n) for(int i = 0; i < (n); i++)
#define FORIS(i, s, n) for(int i = (s); i < (n); i++)
#define CLEAR(a, n) memset(a, n, sizeof(a))
#define PB(n) push_back(n)
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(), (c).end()
#define NUM 55

#define FOLDER(file) "c:\\Projects\\coding\\cj\\2010\\QualificationRound\\C\\"file

LL mem_R[10000];
LL mem_S[10000];
LL g[10000];

int main(int argc, char* argv[])
{
//	ifstream in(FOLDER("C-test.in"));
//	ofstream out(FOLDER("C-test.out"));
//	ifstream in(FOLDER("C-small-attempt0.in"));
//	ofstream out(FOLDER("C-small-attempt0.out"));
	ifstream in(FOLDER("C-large.in"));
	ofstream out(FOLDER("C-large.out"));

	LL T, R, k, N;
	in >> T;
	FORI(ncase, T) {
		in >> R >> k >> N;
		FORI(i, N)
			in >> g[i];

		FORI(i, N)
			mem_R[i] = mem_S[i] = -1;
		mem_R[0] = mem_S[0] = 0;

		LL tot = 0;
		FORI(i, N) tot += g[i];
		LL S = 0;
		if(tot <= k) 
			S = R*tot;
		else {
			int cur = 0;
			while(R > 0) {
				LL spc = k;
				while(spc > 0) {
					if(g[cur] <= spc) {
						S += g[cur];
						spc -= g[cur];
						cur++;
						if(cur >= N) cur -= N;
					} else
						break;
				}
				R--;
				if(mem_R[cur] != -1) {
					LL Rs = mem_R[cur] - R;
					LL Ss = S - mem_S[cur];
					LL tms = R / Rs;
					if(tms > 0) {
						R -= Rs*tms;
						S += Ss*tms;
					}
				}
				mem_R[cur] = R;
				mem_S[cur] = S;
			}
		}
		out << "Case #" << (ncase+1) << ": " << S << endl;
	}
	return 0;
}
