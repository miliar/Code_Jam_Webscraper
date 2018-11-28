#include <stdio.h>
#include <string.h>
#include <sstream>
#include <algorithm>
using namespace std;

const int N = 105;

struct Node {
	int from, to;
	Node() {}
	Node(int ff, int tt) {
		from = ff;
		to = tt;
	}
};

int turn, n[2];
Node A[2][N];

void read_time(int& x) {
	char tm[10];
	scanf("%s", tm);
	int i, n = strlen(tm);
	for(i = 0; i < n; ++i) if(tm[i] == ':') tm[i] = ' ';
	istringstream is(tm);
	int a, b, c;
	is >> a;
	is >> b;
	c = a * 60 + b;
	x = c;
}

void read(int x, int y) {
	read_time(A[x][y].from);
	read_time(A[x][y].to);
	A[x][y].to += turn;
}

bool cmp1(const Node& a, const Node& b) {
	return a.from < b.from;
}

bool cmp2(const Node& a, const Node& b) {
	return a.to < b.to;
}

int solve(int x, int y) {
	sort(A[x], A[x] + n[x], cmp1);
	sort(A[y], A[y] + n[y], cmp2);
	int i = 0, j = 0, cnt = 0;
	while(i < n[x] && j < n[y]) {
		if(A[y][j].to <= A[x][i].from) cnt++, i++, j++;
		else i++;
	}
	return n[x]-cnt;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("res.txt", "w", stdout);
	
	int ntc, i, j, tc = 0;
	scanf("%d", &ntc);
	while(ntc--) {
		scanf("%d %d %d", &turn, &n[0], &n[1]);
		for(i = 0; i < n[0]; ++i) read(0, i);
		for(i = 0; i < n[1]; ++i) read(1, i); 

		printf("Case #%d: %d %d\n", ++tc, solve(0, 1), solve(1,0) );
	}
	return 0;
}