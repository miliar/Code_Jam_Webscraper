#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <list>

using namespace std;

#define LEN 1000

int T,C,D,N;
char str[LEN];
char combines[26][26];
bool opposed[26][26];
int plof[26];
list<char> letters;

void init() {
	for (int i = 0; i < 26; i++) {
		for (int j = 0; j < 26; j++) {
			combines[i][j] = '\0';
			opposed[i][j] = '\0';
		}
		plof[i] = 0;
	}
	letters.clear();
}

void combine(char * tmp) {
	int a = tmp[0] - 'A';
	int b = tmp[1] - 'A';
	char c = tmp[2];
	combines[a][b] = c;
	combines[b][a] = c;
}

void opponent(char * tmp) {
	int a = tmp[0] - 'A';
	int b = tmp[1] - 'A';
	opposed[a][b] = true;
	opposed[b][a] = true;
}

bool checkplof(char c) {
	for (int i = 0; i < 26; i++) {
		if (plof[i] > 0 && opposed[i][c - 'A'])
			return true;
	}
	return false;
}

void process(char c) {
	if (letters.empty()) {
		letters.push_back(c);
		plof[c - 'A']++;
		return;
	}
	char b = letters.back();
	char d = combines[b - 'A'][c - 'A'];
	if (d != '\0') {
		letters.pop_back();
		plof[b - 'A']--;
		plof[d - 'A']++;
		letters.push_back(d);
	}
	else {
		if (checkplof(c)) {
			letters.clear();
			for (int i = 0; i < 26; i++)
				plof[i] = 0;
			return;
		}
		letters.push_back(c);
		plof[c - 'A']++;
	}
}

int main() {
	fgets(str,LEN - 2,stdin);
	sscanf(str,"%d",&T);
	for (int i = 0; i < T; i++) {
		init();
		fgets(str,LEN - 2,stdin);
		char* tmp = strtok(str," ");
		sscanf(tmp, "%d", &C);
		for (int j = 0; j < C; j++) {
			tmp = strtok(NULL," ");
			combine(tmp);
		}
		tmp = strtok(NULL," ");
		sscanf(tmp, "%d", &D);
		for (int j = 0; j < D; j++) {
			tmp = strtok(NULL," ");
			opponent(tmp);
		}
		tmp = strtok(NULL," ");
		sscanf(tmp, "%d", &N);
		tmp = strtok(NULL," ");
		for (int j = 0; j < N; j++)
			process(tmp[j]);
		list<char>::iterator it;
		bool eerste = true;
		printf("Case #%d: [", i + 1);
		for (it = letters.begin(); it != letters.end(); it++) {
			if (!eerste)
				printf(", ");
			printf("%c", *it);
			eerste = false;
		}
		printf("]\n");
	}
	return 0;
}
