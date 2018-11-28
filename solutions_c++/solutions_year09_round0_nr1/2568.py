#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
#include <boost/regex.hpp> 

using namespace std;

#define NWORD 5010
#define WSIZE 20

int L, D, N;

char dic[NWORD][WSIZE];
char query[10000];
char filter[50][50];

int indic(char *s) {
	for(int i = 0; i < D; ++i) {
		if(strcmp(s, dic[i]) == 0) {
			return 1;
		}
	}
	return 0;
}

void bt(int qpos, int spos)
{
	int clos = qpos;
	while(query[qpos] != '(') {
		if(query[qpos] == '\0') {
			return;
		}
		filter[0][spos++] = query[qpos];
		qpos++;
	}
	while(query[clos] !=')') {
		if(query[clos] == '\0') {
			return;
		}
		clos++;
	}
	int ans = 0;
	for(int i = qpos+1; i < clos; ++i) {
		filter[i-qpos-1][spos] = query[i];
	}
	bt(clos+1, spos+1);
}

void printfilter()
{
	for(int i = 0; i < 26; ++i) {
		for(int j = 0; j < L; ++j) {
			printf("%c", filter[i][j]);
		}
		printf("\n");
	}
}

int match(char * s)
{
	for(int i = 0; s[i] != '\0'; ++i) {
		int j;
		for(j = 0; filter[j][i] != 0; ++j) {
			if(filter[j][i] == s[i]) break;
		}
		if(filter[j][i] == 0) return 0;
	}
	return 1;
}

int main() {

	scanf(" %d %d %d", &L, &D, &N);

	for(int i = 0; i < D; ++i) {
		scanf(" %s", dic[i]);
		//printf("%s\n", dic[i]);
	}

	for(int i = 0; i < N; ++i) {
		memset(filter, 0, sizeof(filter));
		int ans = 0;
		scanf(" %s", query);
		//printf("%s\n", query);
		bt(0, 0);
		//printf("Filter:\n");
		//printfilter();
		for(int j = 0; j < D; ++j) {
			if(match(dic[j])) ans++;
		}
		printf("Case #%d: %d\n", i+1, ans);
	}

	return 0;
}
