#include <vector>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(void) {
	int i, j, k, nrEngine, nrQuery, nrTest;
	vector <string> Engines, Queries;
	string auxSt;
	vector <int> auxBuf;
	ifstream in("A-large.in");
	ofstream out("A-large.out");

	in >> nrTest;

	for (i = 1; i <= nrTest; i++) {
			int rez = 0, curPoz = 0;
			Engines.clear(); Queries.clear();
			in >> nrEngine;
			auxBuf.resize(nrEngine);
			j = 0;
			while (getline(in, auxSt) && j < nrEngine) {
				j++;
				if (auxSt != "") Engines.push_back(auxSt);
			}
			if (auxSt != "") Engines.push_back(auxSt);
			in >> nrQuery;
			j = 0;
			while(getline(in, auxSt) && j < nrQuery) {
				j++;
				if (auxSt != "") Queries.push_back(auxSt);
			}
			if (auxSt != "") Queries.push_back(auxSt);

			while (curPoz < Queries.size()) {
				for (j = 0; j < Engines.size(); j++) auxBuf[j] = 1000000;
				for (j = 0; j < Engines.size(); j++) 
					for (k = curPoz; k < Queries.size(); k++) {
						if (Queries[k] == Engines[j]) auxBuf[j] = min(auxBuf[j], k);
					}
				cout << "rez: " << rez << endl;
				for (int h = 0; h < Engines.size(); h++) cout << auxBuf[h] << " "; cout << endl;
				for (j = 0; j < Engines.size(); j++) if (auxBuf[j] == 1000000) {
					out << "Case #" << i << ": " << rez << endl;
					goto end;
				}
				for (j = 0; j < Engines.size(); j++) curPoz = max(curPoz, auxBuf[j]);
				rez++;
			}
			out << "Case #" << i << ": " << rez << endl;
			end:;
	}

	return 0;
}
