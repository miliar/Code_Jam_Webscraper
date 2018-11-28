#include <iostream>
#include <algorithm>

using namespace std;

enum {
	BOTO = 0,
	BOTB
};

int main() {
	int n;
	int t[2][101] = {0};
	int p[2][101] = {0};
	cin >> n;

	for (int cs = 1; cs <= n; cs++) {
		int nn;
		
		t[BOTO][0] = t[BOTB][0] = 0;
		p[BOTO][0] = p[BOTB][0] = 1;


		cin >> nn;

		for (int i = 1; i <= nn; i++) {
			char bot;
			int pos, d;

			cin >> bot >> pos;
			switch (bot) {
				case 'O': bot = BOTO;break;
				case 'B': bot = BOTB;break;
			}

			d = p[bot][i-1] - pos;
			d = (d<0)?-d:d;

			t[bot][i] = max(t[bot][i-1] + d, t[1-bot][i-1]) + 1;
			p[bot][i] = pos;

			t[1-bot][i] = t[1-bot][i-1];
			p[1-bot][i] = p[1-bot][i-1];

		}
		
		int T = max(t[BOTO][nn], t[BOTB][nn]);
			
		cout << "Case #" << cs << ": " << T << endl;
	}

	return 0;
}
