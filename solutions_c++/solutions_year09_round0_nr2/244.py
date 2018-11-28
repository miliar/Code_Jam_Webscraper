#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define fr(i, N) for(i = 0; i < (int)N; i++)
#define setContains(i,j) (((1<<j)&i) != 0)
#define MP make_pair
#define F first
#define S second
#define pb push_back
#define Eps 1e-11

int H, W;
int Mat[200][200];
int area[200][200];

void input()
{
	int i, j;
	scanf("%d%d", &H, &W);

	fr (i, H) fr (j, W) area[i][j] = -1, scanf("%d", &Mat[i][j]);
}

bool valid(int h, int w) {
	return 0 <= h && h < H && 0 <= w && w < W;
}

void process()
{
	int i, j, k, l, ant = 0;
	int dh[4] = {-1, 0, 0, 1};
	int dw[4] = {0, -1, 1, 0};
	map<int, char> Data;
	fr (i, H) fr (j, W) if (area[i][j] == -1) {
		vector<pair<int, int> > Que;
		Que.pb(MP(i, j));

		fr (k, Que.size()) {
			int next = -1;
			int h = Que[k].F, w = Que[k].S;
			fr (l, 4) if (valid(h + dh[l], w + dw[l]) && Mat[h + dh[l]][w + dw[l]] < Mat[h][w]) {
				if (next == -1) next = l;
				if (Mat[h+dh[l]][w+dw[l]] < Mat[h+dh[next]][w+dw[next]]) next = l;
			}

			if (next == -1) {	// sink
				fr (k, Que.size()) area[Que[k].F][Que[k].S] = ant;
				ant++;
				break;
			} else if (area[h+dh[next]][w+dw[next]] != -1) {
				fr (k, Que.size()) area[Que[k].F][Que[k].S] = area[h+dh[next]][w+dw[next]];
				break;
			} else {
				Que.pb(MP(h+dh[next], w+dw[next]));
			}
		}
	}

	char next = 'a';
	fr (i, H) fr (j, W) {
		if (Data.find(area[i][j]) == Data.end()) {
			Data[area[i][j]] = next++;
		}

		printf("%c", Data[area[i][j]]);
		if (j == W-1) printf("\n");
		else printf(" ");
	}
}

int main()
{
	int t, T;
	scanf("%d", &T);

	fr(t, T)
	{
		input();
		printf("Case #%d:\n", t+1);
		process();
	}
	return 0;
}

