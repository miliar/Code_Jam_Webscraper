#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define REP(a,b) for (int a=0; a<b; ++a)

int main() 
{
	ifstream fin("b.in");
	ofstream fout("b.out");

	int tc, c, d, p, v;

	fin >> tc;

	REP(t,tc) {
		vector <int> true_pos;
		fin >> c >> d;

		REP(i,c) {
			fin >> p >> v;
			REP(j,v) true_pos.push_back(p);
		}

		double tlo = 0, thi = 1e16, tmid;

		while (thi - tlo > 1e-10) {
			vector <double> push_pos;
			tmid = (thi+tlo)/2;
			//tmid = 0;
			push_pos.push_back((double)true_pos[0]-tmid);

			bool ok = true;
			for (int i = 1; i < true_pos.size(); ++i) {
				double clp = push_pos[i-1]+d;
				if (fabs((double)true_pos[i]-clp) <= tmid) {
					push_pos.push_back(clp);
				} else if (true_pos[i] > clp) {
					push_pos.push_back(true_pos[i]-tmid);
				} else {
					ok = false;
					break;
				}
			}

			if (!ok) {
				tlo = tmid;
			} else
				thi = tmid;
		}

		fout.precision(10);
		fout << "Case #" << t+1 << ": " << fixed << tlo << endl;
	}

	fout.close();

	return 0;
}