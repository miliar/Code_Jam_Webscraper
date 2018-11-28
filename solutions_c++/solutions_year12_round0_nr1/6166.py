#pragma comment(linker, "/STACK:16777216")
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#define eps 1.0e-6
#define inf 2000000000
#define forn(i, n) for(int i = 0; i < (int)n; ++i)

using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<bool> vb;
typedef pair<int, int> ii;
typedef long long ll;

char s[100500];
char rep[] = "yhesocvxduiglbkrztnwjpfmaq";

void solve(int test) {
gets(s);
int l = strlen(s);
forn(i, l) if(s[i] >= 'a' && s[i] <= 'z'){
s[i] = rep[s[i] - 'a'];
}
printf("Case #%d: %s\n", test, s);
}

int main(int argc, char **argv) {
freopen("input.txt", "r", stdin);
freopen("output.txt", "w+", stdout);
int tt;
scanf("%d\n", &tt);
forn(i, tt) {
solve(i + 1);
}
return 0;
}
