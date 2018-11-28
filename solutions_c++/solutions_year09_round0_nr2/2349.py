#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <vector>

#define INT_MAX    2147483647

using namespace std;

enum {
    NORTH,
    WEST,
    EAST,
    SOUTH,
    DIR_MAX
};

typedef vector<vector<int> > Cells;

static void init(Cells &c, int h, int w, int v) {
    c.clear();
    c.resize(h);
    for (int i = 0; i < c.size(); i++) {
	c[i].resize(w, v);
    }
}

static void dumpA(const Cells &A) {
    for (int h = 0; h < A.size(); h++) {
	for (int w = 0; w < A[h].size(); w++) {
	    printf("%d ", A[h][w]);
	}
	printf("\n");
    }
    printf("\n");
}

static void dumpL(const Cells &L) {
    for (int h = 0; h < L.size(); h++) {
	for (int w = 0; w < L[h].size(); w++) {
	    printf("%c ", L[h][w]);
	}
	printf("\n");
    }
}

static void display(int i, const Cells &L) {
    printf("Case #%d:\n", i + 1);
    dumpL(L);
}

static char solve(const Cells &A, Cells &L, int h, int w, char &zcLabel) {
    assert(A.size() != 0);
    int H = A.size();
    int W = A[0].size();

    //printf("Solving A[%d][%d] = %d...\n", h, w, A[h][w]);
    if (L[h][w] == '-') {
	int dir[DIR_MAX] = {
	    h - 1 >= 0 ? A[h - 1][w] : INT_MAX,
	    w - 1 >= 0 ? A[h][w - 1] : INT_MAX,
	    w + 1 < W  ? A[h][w + 1] : INT_MAX,
	    h + 1 < H  ? A[h + 1][w] : INT_MAX
	};
	
	// Find the direction with min value
	int min = INT_MAX;
	int which = -1;
	for (int i = 0; i < DIR_MAX; i++) {
	    if (dir[i] < min) {
		min = dir[i];
		which = i;
	    }
	}
	
	if (A[h][w] <= min) {
	    if (L[h][w] == '-') {
		L[h][w] = zcLabel++;
	    }
	} else {
	    switch (which) {
	    case NORTH:
		L[h][w] = solve(A, L, h - 1, w, zcLabel);
		break;
	    case WEST:
		L[h][w] = solve(A, L, h, w - 1, zcLabel);
		break;
	    case EAST:
		L[h][w] = solve(A, L, h, w + 1, zcLabel);
		break;
	    case SOUTH:
		L[h][w] = solve(A, L, h + 1, w, zcLabel);
		break;
	    default:
		break;
	    }
	}
    }

    //printf("\tL[%d][%d] = %c\n", h, w, L[h][w]);
    return (L[h][w]);
}

static void solve(const Cells &A, Cells &L) {
    char zcLabel = 'a';
    int H = A.size();
    int W = A[0].size();

    //L[0][0] = zcLabel;
    for (int h = 0; h < A.size(); h++) {
	for (int w = 0; w < A[h].size(); w++) {
	    solve(A, L, h, w, zcLabel);
	}
    }
}

int main(void) {
    Cells A;  // A is the Altitude array
    Cells L;  // L is the label array

    // Read the spec
    int T;
    // Read 1st line
    if (fscanf(stdin, "%d", &T) != 1) {
	fprintf(stderr, "Parse error!\n");
	exit(-1);
    }
    //printf("%d\n", T);
    
    for (int i = 0; i < T; i++) {
	int H, W;
	if (fscanf(stdin, "%d %d", &H, &W) != 2) {
	    fprintf(stderr, "Parse error!\n");
	    exit(-1);
	}
	//printf("%d %d\n", H, W);
	init(A, H, W, -1);

	for (int h = 0; h < H; h++) {
	    for (int w = 0; w < W; w++) {
		int c;
		if (fscanf(stdin, "%d", &c) != 1) {
		    fprintf(stderr, "Parse error!\n");
		    exit(-1);
		} else {
		    A[h][w] = c;
		}
	    }
	}

	//dumpA(A);
	init(L, H, W, '-');
	solve(A, L);
	//dumpL(L);
	display(i, L);
	L.clear();
    }
    
    return (0);
}
