/// Written by G_Crabe

#include <cstdio>
#include <cmath>

#include <assert.h>
#include <memory.h>

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(v) v.begin(), v.end()
#define sz(v) (int)v.size()

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

template<typename Type>
inline Type sqr(Type num) {
    return num * num;
}

const int INF = (int)1e9;
const float EPS = 1e-9;
const double PI = 3.141592653589793;

typedef long long int64;
typedef long double ld;

#define MAXN 100

// For global date

inline char solve(char x) {

	if (x == ' ') return ' ';
	if (x == 'z') return 'q';
	if (x == 'n') return 'b';
	if (x == 'f') return 'c';
	if (x == 'i') return 'd';
	if (x == 'c') return 'e';
	if (x == 'w') return 'f';
	if (x == 'l') return 'g';
	if (x == 'b') return 'h';
	if (x == 'k') return 'i';
	if (x == 'u') return 'j';
	if (x == 'o') return 'k';
	if (x == 'm') return 'l';
	if (x == 'x') return 'm';
	if (x == 's') return 'n';
	if (x == 'e') return 'o';
	if (x == 'v') return 'p';
	if (x == 'y') return 'a';
	if (x == 'p') return 'r';
	if (x == 'd') return 's';
	if (x == 'r') return 't';
	if (x == 'j') return 'u';
	if (x == 'g') return 'v';
	if (x == 't') return 'w';
	if (x == 'h') return 'x';
	if (x == 'a') return 'y';
	if (x == 'q') return 'z';
}

int main() {
	freopen(CIN_FILE, "rt", stdin);
	freopen(COUT_FILE, "wt", stdout);
    ios_base::sync_with_stdio(false);

    int n;
    scanf("%d\n", &n);

    for (int test = 0; test < n; ++test) {
    		char str[MAXN];
    		gets(str);

		printf("Case #%d: ", test + 1);

    		for (int i = 0; i < strlen(str); ++i)
    			printf("%c", solve(str[i]));
    
    		printf("\n");
    }

    return 0;
}
