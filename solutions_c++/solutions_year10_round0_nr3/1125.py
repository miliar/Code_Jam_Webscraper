#include <fstream>
#include <vector>

using namespace std;

#define REP(a,b) for(int a=0;a<b;++a)

int main()
{
	ifstream fin("c.in");
	ofstream fout("c.out");

	int t, R, k, N;
	long long res, csum;
	vector <int> g;
	vector <int> ride;
	vector <int> pos;

	fin >> t;

	for (int tc = 1; tc <= t; ++tc) {
		fin >> R >> k >> N;

		g.resize(N);
		REP(i,N) fin >> g[i];

		ride.clear();
		pos.resize(N); REP(i,N) pos[i] = -1;
		int spos = 0, ix = 0;
		int pre, cl;

		while (true) {
			int cpos = spos, np = 0;
			do {
				if (np + g[cpos] > k) break;
				np += g[cpos];
				cpos = (cpos+1)%N;
			} while (cpos != spos);
			pos[spos] = ix;
			ride.push_back(np);
			if (pos[cpos] != -1) {
				pre = pos[cpos];
				cl = ix - pos[cpos] + 1;
				break;
			}
			spos = cpos;
			++ix;
		}

		res = 0;
		if (R <= pre) {
			REP(i,R) res += ride[i];
		} else {
			REP(i,pre) res += ride[i];
			R -= pre;
			REP(i,R%cl) res += ride[i+pre];
			csum = 0;
			REP(i,cl) csum += ride[pre+i];
			res += csum*(R/cl);
		}

		fout << "Case #" << tc << ": " <<  res << endl;
	}

	fin.close();
	fout.close();

	return 0;
}