#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

typedef vector<int> vct;
typedef vector<char> vot;
typedef vector<vct> vvt;

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cc;
	cin >> cc;
	for (int cs = 1; cs <= cc; ++cs) {
		int a;
		vvt act(2, vct(1, 1));
		vot ord;
		cin >> a;
		for (int b = 0; b < a; ++b) {
			char bot;
			int button;
			cin >> bot >> button;
			act[(bot != 'O')].push_back(button);
			ord.push_back(bot);
		}

		vct& bo = act[0];
		vct& bb = act[1];

		vct::iterator vo = bo.begin() + 1, vb = bb.begin() + 1, vbe = bb.end(), voe = bo.end();
		vot::iterator next = ord.begin();
		int step = 0;
		for (; (vo != voe || vb != vbe);) {
			++step;
			bool pushed = false;
			if (vo != voe) {
				if (bo[0] != *vo) {
					bo[0] < *vo ? ++bo[0] : --bo[0];
				} else if (*next == 'O') {
					++vo;
					pushed = true;
				}
			}
			if (vb != vbe) {
				if (bb[0] != *vb) {
					bb[0] < *vb ? ++bb[0] : --bb[0];
				} else if (*next == 'B') {
					++vb;
					pushed = true;
				}
			}
			if (pushed)
				++next;
		}
		cout << "Case #" << cs << ": " << step << endl;
	}
	return 0;
}
