#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;

typedef vector<int> vi; 
typedef pair<int,int> ii;
 
#define sz(a) int((a).size()) 
#define pb push_back 
#define present(c,x) ((c).find(x) != (c).end()) 

char dic[5010][20];
char s[1000];
bool present[1000][26];
int D, L;
int N;

void init()
{
    scanf("%d%d%d", &L, &D, &N);
    for (int i = 0; i < D; ++i) {
	scanf("%s", dic[i]);
    }
}

bool go(char *t)
{
    for (int i = 0; i < L; ++i) {
	if (!present[i][t[i] - 'a'])
	    return false;
    }
    return true;
}

void run()
{
    scanf("%s", s);
    int n = strlen(s);
    for (int i = 0; i < n; ++i) {
	for (int j = 0; j < 26; ++j) {
	    present[i][j] = 0;
	}
    }

    int k = 0;
    int i = 0;
    while (i < n) {
	if (s[i] == '(') {
	    ++i;
	    while (s[i] != ')') {
		present[k][s[i] - 'a'] = true;
		++i;
	    }
	}
	else {
	    present[k][s[i] - 'a'] = true;
	}
	++i;
	++k;
    }

    int ans = 0;
    for (int i = 0; i < D; ++i) {
	if (go(dic[i])) {
	    ++ans;
	}
    }
    printf("%d\n", ans);
}

int main(void)
{
    init();
    for (int i = 1; i <= N; ++i) {
	printf("Case #%d: ", i);
	run();
    }
    return 0;
}


