/*
	Author: TangQiao @ Netease Youdao.
	2011.5.7
*/
#include <stdio.h>
#include <string>
#include <vector>
#include <math.h>
using namespace std;

char combine[256][256];
char oppose[256][256];
char seq[110], len;
vector<char> ans;
bool debug = false;

void init() {
	// reset values
	memset(combine, 0, sizeof(combine));
	memset(oppose, 0, sizeof(oppose));
	memset(seq, 0, sizeof(seq));
	ans.clear();

	// read data
	int n, i;
	char tmp[10];
	scanf("%d", &n);
	for (i = 0; i < n; ++i) {
		scanf("%s", tmp);
		combine[tmp[0]][tmp[1]] = tmp[2];
		combine[tmp[1]][tmp[0]] = tmp[2];
	}
	scanf("%d", &n);
	for (i = 0; i < n; ++i) {
		scanf("%s", tmp);
		oppose[tmp[0]][tmp[1]] = 1; 
		oppose[tmp[1]][tmp[0]] = 1;
	}
	scanf("%d", &len);
	scanf("%s", seq);
}


void output() {
	int i;
	printf("[");
	if (ans.size() > 0) {
		printf("%c", ans[0]);
	}
	for (i = 1; i < ans.size(); ++i) 
		printf(", %c", ans[i]);
	printf("]\n");

}

void judgeCombine() {
	bool res = true;
	while (res) {
		res = false;
		if (ans.size() >= 2) {
			char c = ans[ans.size() - 1];
			char b = ans[ans.size() - 2];
			if (combine[b][c] != 0) {
				ans.pop_back();
				ans.pop_back();
				ans.push_back(combine[b][c]);
				res = true;
			}
		}
	}
}

void judgeOppose() {
	if (ans.size() >= 2) {
		char c = ans[ans.size() - 1];
		for (int i = 0; i < ans.size() -1; ++i) {
			if (oppose[ans[i]][c]) {
				// ans.erase(ans.begin() + i, ans.end());
				ans.clear();
				break;
			}
		}
	}
}

void deal() {
	for (int i = 0; i < len; ++i) {
		char c = seq[i];
		ans.push_back(c);
		// combine:
		judgeCombine();
		// oppose
		judgeOppose();
		
		if (debug) {
			output();
		}
	}
}


int main() {
    int N;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    scanf("%d", &N);
    for (int i = 0; i < N; ++i) {
        init();
        deal();
        printf("Case #%d: ", i+1);
		output();
    }
    return 0;
}

/*
Sample Test Case:
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW

Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []

My Test Case:
10
1 ERQ 1 QW 3 REW
0 0 1 A

*/