#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;


char cmb[256][256];
bool opp[256][256];


void Load()
{
	memset(cmb, 0, sizeof(cmb));
	memset(opp, 0, sizeof(opp));
	int c, d, i;
	char q, w, r;
	cin >> c;
	for (i = 0; i < c; i++) {
		cin >> q >> w >> r;
		cmb[q][w] = cmb[w][q] = r;
	}
	cin >> d;
	for (i = 0; i < d; i++) {
		cin >> q >> w;
		opp[q][w] = opp[w][q] = true;
	}
}

void Solve()
{
	int n, i, j;
	string s, list;
	cin >> n;
	cin >> s;
	const char chs[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
	char c, h;
	int hm[256];
	memset(hm, 0, sizeof(hm));
	bool cleared;
	for (i = 0; i < n; i++) {
		c = s[i];
		if (list.size() > 0 && cmb[list[list.size()-1]][c] != 0) { // combine?
			h = list[list.size()-1];
			list.resize(list.size()-1);
			list.push_back(cmb[h][c]);
			hm[h]--;
			hm[cmb[h][c]]++;

		} else { // clear?
			cleared = false;
			for (j = 0; j < 8; j++) {
				h = chs[j];
				if (opp[h][c] && hm[h] > 0) {
					list.clear();
					memset(hm, 0, sizeof(hm));
					cleared = true;
					break;
				}
			}
			if (!cleared) {
				list.push_back(c);
				hm[c]++;
			}
		}
	}
	cout << "[";
	for (i = 0; i < list.size(); i++){
		if (i > 0) cout << ", ";
		cout << list[i];
	}
	cout << "]\n";
}

int main()
{
	int nt, tt;
	cin >> nt;
	for (tt = 1; tt <= nt; tt++)
	{
		Load();
		cout << "Case #" << tt << ": ";
		Solve();
	}
	return 0;
}
