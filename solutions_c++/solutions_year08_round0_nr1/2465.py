#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int n;
	cin >> n;
	
	for (int i=0; i<n; ++i) {
		int ns;
		cin >> ns;
		cin.ignore();
		vector<string> sgn(ns);
		for(int j=0; j<ns; ++j) {
			string nm;
			getline(cin, nm);
			sgn[j] = nm;
		}
		
		int nq;
		cin >> nq;
		cin.ignore();
		vector<string> qv(nq);
		for (int j=0; j<nq; ++j) {
			string nm;
			getline(cin, nm);
			qv[j] = nm;
		}
		
		if (nq == 0) cout << "Case #" << i+1 << ": 0\n";
		else {
			int nx = -1, npq = 0;
		
			while (npq < nq) {
				int mxq = 0;
				vector<string>::iterator svi = qv.begin() + npq;
				vector<string>::iterator fsi;
				for (int j=0; j<ns; ++j) {
					fsi = find(svi, qv.end(), sgn[j]);
					int cpq = fsi - svi;
					if (fsi == qv.end()) { mxq = cpq; break; }
					if (cpq > mxq) mxq = cpq;				
				}
				npq += mxq;
				++nx;
			}
		
			cout << "Case #" << i+1 << ": " << nx << '\n';
		}
	}
	
	return 0;
}

