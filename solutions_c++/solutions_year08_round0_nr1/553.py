#include <iostream>
#include <sstream>
#include <fstream>
#include <map>
#include <vector>
#include <string>

using namespace std;

const string FIN = "A-big.in";
const string FOUT = "A-big.out";

int N, S, Q;
int main () {

	ifstream fin;
	ofstream fout;
	int n;
	fin.open (FIN.c_str());
	fout.open (FOUT.c_str());
	
	string s;
	getline (fin,s);
	istringstream ins(s);
	ins >> n;
	//cout << n << endl;
	for (int xxx = 1; xxx <= n; ++xxx) {
		getline (fin, s);
		ins.clear();
		ins.str(s);
		ins >> S;
		map<string, int> se;
		for (int i = 0; i < S; ++i) {
			getline (fin, s);
			int sz = se.size ();
			se [s] = sz;
		}
		getline (fin, s);
		ins.clear();
		ins.str(s);
		ins >> Q;
		vector<string> q;
		for (int i = 0; i < Q; ++i) {
			getline (fin, s);
			q.push_back (s);
		}
		int D [2][200];
		memset (D, 0, sizeof (D));
		int b;
		for (int i = 0; i < Q; ++i) {
			b = (i & 1);
			memset (D [b], 0x7f, sizeof (D[b]));
			if (se.find (q [i]) == se.end ()) {
				memcpy (D [b], D [1 - b], sizeof (D [0]));
				continue;
			}
			int idx = se [q [i]];
			for (int j = 0; j < S; ++j)
				if (j != idx) {
					D [b][j] = min(D [1 - b][j], D[1-b][idx] + 1);
				}
		}
		
		int res = Q + 1;
		for (int j = 0; j < S; ++j)
			res <?= D [b][j];
			
		fout << "Case #" << xxx << ": " << res << endl;
	}
	fout.close ();
	fin.close ();
}
