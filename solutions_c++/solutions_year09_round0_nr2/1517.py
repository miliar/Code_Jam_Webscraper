#include <cstdio>
#include <vector>
using namespace std;


struct SET {
	SET *up;
	int lvl;

	void init() {
		up = this;
		lvl = 0;
	}
	SET *find() {
		SET *top = up;
		while(top->up != top)
			top = top->up;
		SET *w = this;
		while(w->up != w) {
			SET *x = w->up;
			w->up = top;
			w = x;
		}
		return top;
	}
	static void link(SET &a, SET &b) {
		SET *A = a.find();
		SET *B = b.find();
		if(A->lvl > B->lvl) {
			B->up = A;
		} else if(A->lvl < B->lvl) {
			A->up = B;
		} else if(A != B) {
			B->up = A;
			A->lvl++;
		}
	}
	bool operator==(SET &o) {
		return find() == o.find();
	}
	bool operator!=(SET &o) {
		return find() != o.find();
	}
};

static const int delta[4][2] = { /* [delta][x,y] */
	{0,-1}, /* NORTH */
	{-1,0}, /* WEST */
	{ 1,0}, /* EAST */
	{0, 1}  /* SOUTH */
};

void solve_map() {
	int W, H;
	static int map[200][200];

	/* wczytaj mapkę */
	scanf("%d%d", &H, &W);
	for(int y=0; y<H; y++)
	for(int x=0; x<W; x++)
		scanf("%d", &map[y][x]);

	/* sprawdź co gdzie płynie */
	static SET set[200][200];
	for(int y=0; y<H; y++)
	for(int x=0; x<W; x++)
		set[y][x].init();

	/* łącz */
	for(int sy=0; sy<H; sy++)
	for(int sx=0; sx<W; sx++) {
		int nx = sx, ny = sy;
		int lastalt = map[sy][sx];
		for(int d=0; d<4; d++) {
			int cx = sx+delta[d][0], cy = sy+delta[d][1];
			if(cx<0 || cy<0 || cx>=W || cy>=H)
				continue;
			if(map[cy][cx] >= lastalt)
				continue;
			lastalt = map[cy][cx];
			nx = cx, ny = cy;
		}
		SET::link(set[sy][sx], set[ny][nx]);
	}

	/* przypisz etykietki */
	static char label[200][200];
	for(int sy=0; sy<H; sy++)
	for(int sx=0; sx<W; sx++) {
		label[sy][sx] = 0;
	}
	for(char letter='a'; letter<='z'; letter++) {
		SET *spc = NULL;
		for(int y=0; y<H; y++)
		for(int x=0; x<W; x++) {
			if(label[y][x])
				continue;
			if(!spc)
				spc = &set[y][x];
			if(*spc != set[y][x])
				continue;
			label[y][x] = letter;
		}
	}

	/* wypisz */
	for(int y=0; y<H; y++) {
		for(int x=0; x<W; x++) {
			printf("%c ", label[y][x]);
		}
		printf("\n");
	}
}

int main() {
	int T; scanf("%d", &T);
	for(int t=0; t<T; t++) {
		printf("Case #%d:\n", t+1);
		solve_map();
	}
	return 0;
}

