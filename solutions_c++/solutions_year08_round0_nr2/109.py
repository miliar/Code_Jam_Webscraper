#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

vector <pair <int, int> > event;

// 0 : from A to B, when arrive (B)
// 1 : from B to A, when arrive (A)
// 2 : from A to B, when departure (A)
// 3 : from B to A, when departure (B)

bool go(int a, int b) {
	int aa = a, bb = b;
	for (int i = 0; i < event.size(); ++i) {
		switch(event[i].second) {
			case 0:
				bb++;
				break;
			case 1:
				aa++;
				break;
			case 2:
				aa--;
				if (aa < 0) return false;
				break;
			case 3:
				bb--;
				if (bb < 0) return false;
				break;
		}
	}
	return true;
}

int main() {
	int Q, T, NA, NB;
	scanf("%d", &Q);
	for (int cn = 1; cn <= Q; ++cn) {
		scanf("%d", &T);
		event.clear();

		scanf("%d %d", &NA, &NB);
		for (int i = 0; i < NA; ++i) {
			int dh, dm, ah, am;
			scanf(" %d:%d %d:%d", &dh, &dm, &ah, &am);
			event.push_back(make_pair(dh * 60 + dm, 2));
			event.push_back(make_pair(ah * 60 + am + T, 0));
		}
		for (int i = 0; i < NB; ++i) {
			int dh, dm, ah, am;
			scanf(" %d:%d %d:%d", &dh, &dm, &ah, &am);
			event.push_back(make_pair(dh * 60 + dm, 3));
			event.push_back(make_pair(ah * 60 + am + T, 1));
		}
		sort(event.begin(), event.end());
		bool found = false;
		for (int i = 0; i <= NA; ++i) {
			for (int j = 0; j <= NB; ++j) {
				if (!found) {
					if (go(i, j)) {
						printf("Case #%d: %d %d\n", cn, i, j);
						found = true;
					}
				}
			}
		}
	}
}

