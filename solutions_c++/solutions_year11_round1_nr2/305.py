#include <cstdio>
#include <cstdlib>
#include <list>

using namespace std;

int limit; int wordInd;
char wordout[10000][11];
short words[10000][27];

void trial(list<short> &wordList, int guess, char* alph) {
	list<short> buckets[1024];
	int count = 0;
	bool possible = false;
	//if (guess > 0) return;
	for (list<short>::iterator i = wordList.begin(); i != wordList.end(); i++) {
		short mask = words[*i][*alph - 'a'];
		if (mask) possible = true;
		buckets[mask].push_front(*i);
		count++;
	}
	//printf("%d\n", count);
	if (count == 1) {
		int word = *(wordList.begin());
		//printf("%d %s %d\n", guess, wordout[word], word);
		if (guess > limit) {
			limit = guess;
			wordInd = word;
		} else if (guess == limit) {
			if (word < wordInd) wordInd = word;
		}
		return;
	}
	if (possible) {
		for (int i = 0; i < 1024; i++) {
			if (buckets[i].empty()) continue;
			trial(buckets[i], (i == 0)?guess+1:guess, alph+1);
		}
	} else {
		trial(wordList, guess, alph+1);
	}
}

int trialmain(int t) {
	printf("Case #%d:", t);
	int N; int M;
	list<short> wordList;
	scanf("%d%d", &N, &M);
	for (int j = 0; j < N; j++) {
		for (int k = 0; k < 26; k++)
			words[j][k] = 0;
		scanf("\n%s", wordout[j]);
		int len = strlen(wordout[j]);
		wordList.push_front(j);
		words[j][26] = len;
		for (int k = 0; k < len; k++) {
			words[j][wordout[j][k]-'a'] |= 1 << k;
		}
	}
	for (int j = 0; j < M; j++) {
		limit = 0;
		char alph[28];
		alph[0] = 'a' + 26;
		scanf("\n%s", alph+1);
		trial(wordList, 0, alph);
		printf(" %s", wordout[wordInd]);
	}
	printf("\n");
}

int main(int argc, char* argv[]) {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		trialmain(i);
	}

    return 0;
}
