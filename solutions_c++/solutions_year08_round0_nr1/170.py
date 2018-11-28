#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int nt, it;
	
	cin >> nt;
	for (it = 1; it <= nt; it++) {
		int ns, nq, i, q, j, m;
		string t;
		map<string, int> ms;
		
		cin >> ns;
		getline(cin, t);
		for (i = 0; i < ns; i++) {
			getline(cin, t);
			ms[t] = i;
		}
		
		cin >> nq;
		
		vector<vector<int> > v(nq + 1, ns); // mazākais pārslēgšanos skaits[laika moments][tajā izvēlētais meklis]
		
		getline(cin, t);
		for (i = 0; i < nq; i++) {
			getline(cin, t);
			q = ms[t];
			m = nq + 1;
			for (j = 0; j < ns; j++) if (j != q) m = min(m, v[i + 1][j] = v[i][j]);
			v[i + 1][q] = m + 1; //min(m + 1, v[i][q] + 2);
		}
		
		cout << "Case #" << it << ": " << *min_element(v[i].begin(), v[i].end()) << '\n';
	}
	
	return 0;
}
