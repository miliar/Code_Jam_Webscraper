#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>

using namespace std;

struct Line {
	int l, r;
};

Line lines[10000];

int main(int argc, char * argv[])
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;

		for (int i = 0; i < N; i++) {
			cin >> lines[i].l >> lines[i].r;
		}

		int intersections = 0;
		for (int l = 0; l < N-1; l++) {
			for (int r = l+1; r < N; r++) {
				if (l == r) continue;
				if ((lines[l].l > lines[r].l && lines[l].r < lines[r].r)
					|| (lines[l].l < lines[r].l && lines[l].r > lines[r].r)) intersections++;
			}
		}

		cout << "Case #" << t << ": ";
		cout << intersections;
		cout << "\n";
	}

	return 0;
}

