#include <cstdio>
#include <algorithm>
#include <vector>

#define MAX_LEN 40*40
#define MAX_WORDS 5500

using namespace std;

char words[MAX_WORDS][MAX_LEN];

int main() {
	int wordlen, nWords, nCases;
	scanf("%d%d%d ",&wordlen,&nWords,&nCases);
	for (int i = 0; i < nWords; i++) {
		scanf("%s ",words[i]);
	}
	for (int i = 0; i < nCases; i++) {
		char test[MAX_LEN]; scanf("%s ",test);
		vector<int> possible = vector<int>(nWords,1);
		int j = 0, index=0;
		while (j < wordlen) {
			vector<int> nextp = vector<int>(nWords,0);
			if (test[index] == '(') {
				index++;
				while (test[index] != ')') {
					for (int k = 0; k < nWords; k++) {
						nextp[k] = nextp[k] || (possible[k] && words[k][j] == test[index]);
					}
					index++;
				}
				index++;
			} else {
				for (int k = 0; k < nWords; k++) {
					nextp[k] = possible[k] && words[k][j] == test[index];
				}
				index++;
			}
			possible=nextp;
			j++;
		}
		int out=0;
		for (int k=0; k < nWords; k++) {
			out+=possible[k];
		}printf("Case #%d: %d\n",i+1,out);
	}
}