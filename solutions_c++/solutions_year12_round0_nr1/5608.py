#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cassert>
#include <ctime>

using namespace std;

#ifdef WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef pair<int, int> pii;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<ll> vll;
typedef vector<vll> vvll;

ll rdtsc() {
    ll tmp;
    asm("rdtsc" : "=A"(tmp));
    return tmp;
}

#define TASKNAME "text"
#define pb push_back
#define mp make_pair
#define EPS (1e-9)
#define INF ((int)1e9)
#define sqr(x) ((x) * (x))         
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

char from[3][100] = {
"ejp mysljylc kd kxveddknmc re jsicpdrysiqz",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};

char to[3][100] = {
"our language is impossible to understandzq",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"
};

char s[101];
int mmap[26];

int main() {
	srand(rdtsc());
	freopen(TASKNAME".in", "r", stdin);
	freopen(TASKNAME".out", "w", stdout);

	memset(mmap, -1, sizeof(mmap));
	for (int it = 0; it < 3; it++) {
		int n = strlen(from[it]);
		assert(n == (int)strlen(to[it]));
		for (int i = 0; i < n; i++)
			mmap[from[it][i] - 'a'] = to[it][i] - 'a';
	}

	int n;
	while (scanf("%d", &n) >= 1) {
		gets(s);
		for (int i = 0; i < n; i++) {
			printf("Case #%d: ", i + 1);
			gets(s);
			for (int j = 0; s[j]; j++)
				if (isspace(s[j]))
					printf("%c", s[j]);
				else
					printf("%c", mmap[s[j] - 'a'] + 'a');
			printf("\n");
		}
		//break;
	}   
	return 0;
}
