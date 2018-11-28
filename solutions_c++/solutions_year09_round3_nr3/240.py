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

vector<int> a;
int hash[110];
int n, p;

void init()
{
    scanf("%d%d", &n, &p);
    a.clear();
    for (int i = 0; i < p; ++i) {
	int x;
	scanf("%d", &x);
	a.pb(x - 1);
    }
}

int go()
{
    memset(hash, 0, sizeof(hash));
    int tot = 0;
    for (int i = 0; i < a.size(); ++i) {
	hash[a[i]] = true;
	for (int j = a[i] - 1; j >= 0 && !hash[j]; --j) {
	    ++tot;
	}
	for (int j = a[i] + 1; j < n && !hash[j]; ++j) {
	    ++tot;
	}
    }
    return tot;
}

void run()
{
    sort(a.begin(), a.end());
    int ans = 1000000000;
    do {
	ans = min(ans, go());
    } while (next_permutation(a.begin(), a.end()));
    printf("%d\n", ans);
}

int main(void)
{
    int c;
    scanf("%d", &c);
    for (int i = 1; i <= c; ++i) {
	init();
	printf("Case #%d: ", i);
	run();
    }
    return 0;
}

