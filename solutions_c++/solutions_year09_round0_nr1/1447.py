#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<string> V;
int has[256][20];
char buf[10000];

int main() {
	int L, D, N;
	int _42=0;
	scanf(" %d %d %d", &L, &D, &N);

	for (int i=0; i < D; i++) {
		scanf(" %s", buf);
		V.push_back(buf);
	}

	for (int i=0; i < N; i++) {
		int cnt=0;
		scanf(" %s", buf);

		memset(has, 0, sizeof(has));
		int p=0;
		bool group=false;
		for (int j=0; j < strlen(buf); j++) {
			if (buf[j] == '(') group = true;
			else if (buf[j] == ')') group = false;
			else has[ buf[j] ][p] = 1;

			if (!group) p++;
		}

		for (int j=0; j < (int)V.size(); j++) {
			bool match = true;
			for (int k=0; k < V[j].size(); k++) {
				if (!has[ V[j][k] ][k]) {
					match = false;
					break;
				}
			}
			if (match) cnt++;
		}
		printf("Case #%d: %d\n", ++_42, cnt);
	}

	return 0;
}


