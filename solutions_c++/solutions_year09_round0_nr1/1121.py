#include<iostream>
using namespace std;

char posb[15][26];
char words[5000][20];
char input[512];

int L, D, N;

int main() {

	freopen("d:/input.in", "r", stdin);
	freopen("d:/output.out","w", stdout);
	scanf("%d %d %d", &L, &D, &N);
	for (int i=0; i<D; ++i)
		scanf("%s", words[i]);
	for (int i=0; i<N; ++i) {
		memset(posb, 0, sizeof posb);
		scanf("%s", input);
		int cur = 0;
		for (int j=0; j<L; ++j) {
			if (input[cur]=='(') {
				++cur;
				while(input[cur] != ')') {
					posb[j][input[cur]-'a'] = 1;
					++cur;
				}
			}
			else
				posb[j][input[cur]-'a'] = 1;
			++cur;
		}
		int count = 0;
		for (int j=0; j<D; ++j) {
			bool suc = true;
			for (int k=0; k<L; ++k) {
				if (posb[k][words[j][k]-'a'] == 0) {
					suc = false;
					break;
				}
			}
			if (suc)
				++count;
		}
		printf("Case #%d: %d\n", i+1, count);
	}
	return 0;
}