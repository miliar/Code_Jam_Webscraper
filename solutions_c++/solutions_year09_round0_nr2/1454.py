using namespace std;
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <list>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>

class cell {
public:
	int h;
	int w;
	int alt;
	char lab;
	cell* dir[4];
	cell* flow;
};

typedef vector<cell> cellmap;

#define FOR(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define FORD(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define GETS(s) getline(cin, s);
#define GETDS(s, d) getline(cin, s, d);
#define GETI(i) { string _s; getline(cin, _s); i = atoi(_s.c_str()); }
#define GETDI(i, d) { string _s; getline(cin, _s, d); i = atoi(_s.c_str()); }

//----------------------------------------------------------------------------
int main() {
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int result;
	int T, H, W;
	int hi, wi, di;
	int altmin;
	char l, sl;
	cell *c;
	cellmap M;

	GETI(T);
	FOR(TestCase, 1, T) {
		result = 0;
		GETDI(H,' ');
		GETI(W);
		for (hi = 0; hi < H; hi++) {
			for (wi = 0; wi < W; wi++) {
				c = new cell();
				c->h = hi;
				c->w = wi;
				c->flow = NULL;
				c->lab = '*';
				if (wi == W - 1)
					GETI(c->alt)
				else
				GETDI(c->alt,' ');
				M.push_back(*c);
			}
		}
		// direction
		for (hi = 0; hi < H; hi++)
			for (wi = 0; wi < W; wi++) {
				//N
				if (hi > 0)
					M[hi * W + wi].dir[0] = &M[(hi - 1) * W + wi];
				else
					M[hi * W + wi].dir[0] = &M[hi * W + wi];
				//W
				if (wi > 0)
					M[hi * W + wi].dir[1] = &M[hi * W + wi - 1];
				else
					M[hi * W + wi].dir[1] = &M[hi * W + wi];
				//E
				if (wi < W - 1)
					M[hi * W + wi].dir[2] = &M[hi * W + wi + 1];
				else
					M[hi * W + wi].dir[2] = &M[hi * W + wi];
				//S
				if (hi < H - 1)
					M[hi * W + wi].dir[3] = &M[(hi + 1) * W + wi];
				else
					M[hi * W + wi].dir[3] = &M[hi * W + wi];
			};
		// flow
		for (hi = 0; hi < H; hi++)
			for (wi = 0; wi < W; wi++) {
				altmin = M[hi * W + wi].dir[0]->alt;
				for (di = 1; di < 4; di++)
					if (M[hi * W + wi].dir[di]->alt < altmin)
						altmin = M[hi * W + wi].dir[di]->alt;
				if (altmin < M[hi * W + wi].alt) {
					//flowdown
					for (di = 0; di < 4; di++)
						if (M[hi * W + wi].dir[di]->alt == altmin) {
							M[hi * W + wi].flow = M[hi * W + wi].dir[di];
							break;
						};

				};
			};
		// label
		l = 'a';
		for (hi = 0; hi < H; hi++)
			for (wi = 0; wi < W; wi++) {
				if (M[hi * W + wi].lab == '*') {
					c = M[hi * W + wi].flow;
					sl = '*';
					while (c != NULL) {
						sl = c->lab;
						c = c->flow;
					};
					if (sl == '*') {
						c = &M[hi * W + wi];
						while (c != NULL) {
							c->lab = l;
							c = c->flow;
						};
						l++;
					} else {
						c = &M[hi * W + wi];
						while (c != NULL) {
							c->lab = sl;
							c = c->flow;
						};
					};
				};
			};
		printf("Case #%d:\n", TestCase);
		//printf("H=%d W=%d \n", H, W);
		for (hi = 0; hi < H; hi++) {
			for (wi = 0; wi < W; wi++) {
				printf("%c ", M[hi * W + wi].lab);
				//printf("%d%c", M[hi * W + wi].alt, M[hi * W + wi].lab);
				//if (M[hi * W + wi].flow == NULL)
				//	printf("->NULL ");
				//else
				//	printf("->%d,%d ", M[hi * W + wi].flow->h,
				//			M[hi * W + wi].flow->w);
			}
			printf("\n");

		}
		for (hi = 0; hi < H; hi++)
			for (wi = 0; wi < W; wi++)
				M[hi * W + wi].~cell();
		M.clear();

	}
	return EXIT_SUCCESS;
}
