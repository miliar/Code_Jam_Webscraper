#include <cstdio>
#include <algorithm>
using namespace std;

#define x first
#define y second

const char FILEIN[] = "date.in";				// input file
const char FILEOUT[] = "date.out";				// output file
const int MAX_N = 128;							// max number of trains leaving from one city

int w;											// turnaround time
int n;											// number of trains leaving from A
int m;											// number of trains leaving from B
pair<int, int> v1[MAX_N];						// schedule for trains leaving A
pair<int, int> v2[MAX_N];						// schedule for trains leaving B

void read(int &a) {
	char s[8];
	scanf(" %s ", s);
	a = ((s[0]-'0') * 10 + (s[1]-'0')) * 60 + ((s[3]-'0') * 10 + (s[4]-'0'));
}

int same(pair<int, int> a, pair<int, int> b) {
	return a.y + w <= b.x;
}

void Solve(int case_no) {
	sort(v1, v1+n);
	sort(v2, v2+m);
	bool mark1[MAX_N] = {};
	bool mark2[MAX_N] = {};

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if (same(v1[i], v2[j]) && !mark2[j]) {
				mark2[j] = true;
				break;
			}

	for (int i = 0; i < m; ++i)
		for (int j = 0; j < n; ++j)
			if (same(v2[i], v1[j]) && !mark1[j]) {
				mark1[j] = true;
				break;
			}

	int ta = 0;						// number of trains leaving a
	int tb = 0;						// number of trains leaving b
	for (int i = 0; i < n; ++i)
		ta += !mark1[i];
	for (int i = 0; i < m; ++i)
		tb += !mark2[i];
	printf("Case #%d: %d %d\n", case_no, ta, tb);
}

int main() {
	freopen(FILEIN, "r", stdin);
	freopen(FILEOUT, "w", stdout);

	int t;										// number of test cases
	scanf("%d\n", &t);
	for (int case_no = 1; case_no <= t; ++case_no) {
		scanf("%d\n", &w);
		scanf("%d %d\n", &n, &m);
		for (int i = 0; i < n; ++i) {
			read(v1[i].x);
			read(v1[i].y);
		}
		for (int i = 0; i < m; ++i) {
			read(v2[i].x);
			read(v2[i].y);
		}

		Solve(case_no);
	}
}