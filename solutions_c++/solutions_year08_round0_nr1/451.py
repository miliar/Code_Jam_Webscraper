#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void main() {
	ifstream inp("a.in");
	ofstream out("a.out");
	int n;
	inp >> n;
	for (int id = 1; id <= n; id++) {
		int s, q;
		string temp;
		inp >> s;
		vector<string> site(s);
		getline(inp, temp);
		for (int i=0; i<s; i++) getline(inp, site[i]);
		inp >> q;
		getline(inp, temp);
		vector<string> query(q);
		for (int i=0; i<q; i++) getline(inp, query[i]);
		vector<int> cg(s);
		for (int i=q-1; i>=0; i--) {
			vector<int> cg0 = cg;
			for (int j=0; j<s; j++) {
				int min = q;
				if (site[j] != query[i])
				{
					for (int k=0; k<s; k++) {
						int v = cg0[k] + (j != k);
						if (v < min) min = v;
					}
				}
				cg[j] = min;
			}
		}
		int min = cg[0];
		for (int i=0; i<s; i++) if (cg[i]<min) min=cg[i];
		out << "Case #" << id << ": " << min << endl;
	}
}
