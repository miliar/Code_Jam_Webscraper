#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <math.h>
#include <algorithm>
#define fori(n) for (int i = 0; i < n; i++)
#define forj(n) for (int j = 0; j < n; j++)
#define fork(n) for (int k = 0; k < n; k++)
#define MAXLEN 501

using namespace std;

string needle = "welcome to code jam";
string hay;
string trash;
int counter = 0;

int dyn[MAXLEN][20];

int dfs(int hay_pos, int needle_pos) {
	if (dyn[hay_pos][needle_pos] != -1) {
		return dyn[hay_pos][needle_pos];
	}

	int haylen = hay.length();
	int nedlen = needle.length();

	int counter = 0;
	if (needle_pos == nedlen) {
		counter = 1;
	} else {
		for (int i = hay_pos; i < haylen; i++) {
			if (hay[i] == needle[needle_pos]) {
				counter += dfs(i+1,needle_pos+1);
			}
		}
	}
	counter %= 10000;
	dyn[hay_pos][needle_pos] = counter;
	return counter;
}

int main() {
	ifstream in("welcome.in");
	FILE* out = fopen("welcome.out","w");
	int N;
	in >> N;
	getline(in,trash);
	for (int n = 0; n < N; n++) {
		for (int i = 0; i < MAXLEN; i++) {
			for (int j = 0; j < 20; j++) {
				dyn[i][j] = -1;
			}
		}

		getline(in,hay);
		cout << hay << endl;
		int ans = dfs(0,0);
		printf("Case #%d: %04d\n",n+1,ans);
		fprintf(out,"Case #%d: %04d\n",n+1,ans);
	}
	return 0;
}
