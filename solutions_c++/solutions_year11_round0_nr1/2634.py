#include <cstdio>
#include <algorithm>

#define TRACE(x) 
#define PRINT(x...) TRACE(printf(x))

using namespace std;

int T, N;
char robot[100];
int bo[110];
int bb[110];
pair<char, int> seq[110];

int main()
{
	scanf(" %d", &T);
	for(int _42 = 1; _42 <= T; ++_42) {
		int nbo = 0;
		int nbb = 0;
		int po = 1;
		int pb = 1;

		scanf(" %d", &N);
		for(int i = 0; i < N; ++i) {
			int button;
			scanf(" %s %d", robot, &button);
			if(*robot == 'O') {
				bo[nbo++] = button;
			} else {
				bb[nbb++] = button;
			}
			seq[i] = make_pair(*robot, button);
		}

		int t;
		int ibo, ibb;
		int i;
		for(t = 0, ibo = 0, ibb = 0, i = 0; i < N; ++t) {
			int pushd = 0;
			PRINT("Time %d\n", t);
			if(ibo < nbo) {
				if(po < bo[ibo]) {
					po++;
					PRINT("\tOrange: Move to button %d\n", po);
				} else if (po > bo[ibo]) {
					po--;
					PRINT("\tOrange: Move to button %d\n", po);
				} else {
					if(seq[i].first == 'O') {
						pushd = 1;
						ibo++;
						PRINT("\tOrange: Push button %d\n", po);
					} else {
						PRINT("\tOrange: Stay at button %d\n", po);
					}
				}
			}

			if(ibb < nbb) {
				if(pb < bb[ibb]) {
					pb++;
					PRINT("\tBlue: Move to button %d\n", pb);
				} else if (pb > bb[ibb]) {
					pb--;
					PRINT("\tBlue: Move to button %d\n", pb);
				} else {
					if(seq[i].first == 'B') {
						pushd = 1;
						ibb++;
						PRINT("\tBlue: Push button %d\n", pb);
					} else {
						PRINT("\tBlue: Stay at button %d\n", pb);
					}
				}
			}

			if(pushd) i++;
		}

		printf("Case #%d: %d\n", _42, t);
	}
	return 0;
}
