#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;

typedef vector<int> vi; 
typedef pair<int,int> ii;
 
#define sz(a) int((a).size()) 
#define pb push_back 
#define present(c,x) ((c).find(x) != (c).end()) 

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

const int maxn = 200;
int a[maxn][maxn];
int x[maxn][maxn];
int y[maxn][maxn];
int num[maxn][maxn];
int m, n;

void init()
{
    scanf("%d%d", &m, &n);
    for (int i = 0; i < m; ++i) {
	for (int j = 0; j < n; ++j) {
	    scanf("%d", &a[i][j]);
	}
    }
}

void go(int i, int j)
{
    int best = a[i][j];
    int bi = -1, bj = -1;
    for (int k = 0; k < 4; ++k) {
	int ii = i + dx[k];
	int jj = j + dy[k];
	if (ii >= 0 && ii < m && jj >= 0 && jj < n && a[ii][jj] < best) {
	    best = a[ii][jj];
	    bi = ii;
	    bj = jj;
	}
    }
    if (bi >= 0 && bj >= 0) {
	if (x[bi][bj] < 0 && y[bi][bj] < 0) {
	    go(bi, bj);
	}
	x[i][j] = x[bi][bj];
	y[i][j] = y[bi][bj];
    }
    else {
	x[i][j] = i;
	y[i][j] = j;
    }
}
    

void run()
{
    memset(x, -1, sizeof(x));
    memset(y, -1, sizeof(y));
    for (int i = 0; i < m; ++i) {
	for (int j = 0; j < n; ++j) {
	    if (x[i][j] < 0 && y[i][j] < 0) {
		go(i, j);
	    }
	}
    }

    memset(num, -1, sizeof(num));
    int k = 0;
    for (int i = 0; i < m; ++i) {
	for (int j = 0; j < n; ++j) {
	    if (num[x[i][j]][y[i][j]] < 0) {
		num[x[i][j]][y[i][j]] = k;
		++k;
	    }
	}
    }
    for (int i = 0; i < m; ++i) {
	for (int j = 0; j < n; ++j) {
	    if (j)
		putchar(' ');
	    putchar(num[x[i][j]][y[i][j]] + 'a');
	}
	putchar('\n');
    }
}

int main(void)
{
    int c;
    scanf("%d", &c);
    for (int i = 1; i <= c; ++i) {
	printf("Case #%d:\n", i);
	init();
	run();
    }
    return 0;
}

