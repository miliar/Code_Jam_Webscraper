#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

int cmap[256][256];
int dmap[256][256];

bool check(char c, char * buf, int p) {
	for (int i = 0; i < p; ++i)
		if (dmap[c][ buf[i] ])
			return true;
	return false;
}

int main () {

	int T;

	cin >> T;
	for (int t = 1; t <= T; ++t) {
	
		int N;
		char a,b,c;
		int d_chr = 0;
		int d_pos = -1;

		char buf[256];
		int p = 0;

		memset(cmap, 0, sizeof(int)*256*256);
		memset(dmap, 0, sizeof(int)*256*256);

		// create
		cin >> N;
		for (int i = 0; i < N; ++i) {
			cin >> a >> b >> c;
			cmap[a][b] = cmap[b][a] = c;
		}
		// delete
		cin >> N;
		for (int i = 0; i < N; ++i) {
			cin >> a >> b;
			dmap[a][b] = dmap[b][a] = -1;
			dmap[a][0] = dmap[b][0] = 1;
		}

		cin >> N;
		for (int i = 0; i < N; ++i) {
			cin >> c;

			if (p > 0 && cmap[buf[p-1]][c]) {
				c = buf[p-1] = cmap[buf[p-1]][c];
			}
			else if (check(c, buf, p)) {
				p = 0;
			}
			else {
				if (dmap[c][0]) {
					d_chr = c;
					d_pos = p;
				}

				buf[p++] = c;
			}
		
		}

		buf[p] = 0;

		if (p == 0)
			cout << "Case #" << t << ": []" << endl;
		else {
			cout << "Case #" << t << ": [" << buf[0];

			for (int i = 1; i < p; ++i)
				cout << ", " << buf[i];

			cout << "]" << endl;
		}

	}
	
	return 0;
}
