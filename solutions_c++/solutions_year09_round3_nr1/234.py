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

const int maxn = 100;
char s[maxn];
int num[128];
int n;
int base;

void run()
{
    scanf("%s", s);
    n = strlen(s);
    memset(num, -1, sizeof(num));
    num[s[0]] = 1;
    base = 0;
    for (int i = 1; i < n; ++i) {
	if (num[s[i]] < 0) {
	    num[s[i]] = base;
	    if (base == 0)
		base = 2;
	    else
		++base;
	}
    }
    if (base == 0)
	base = 2;
    long long ans = 0;
    for (int i = 0; i < n; ++i) {
	ans = base * ans + num[s[i]];
    }
    printf("%lld\n", ans);
}

int main(void)
{
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
	printf("Case #%i: ", i);
	run();
    }
    return 0;
}


