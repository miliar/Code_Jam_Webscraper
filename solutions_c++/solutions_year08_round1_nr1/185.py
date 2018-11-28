#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <string>
#include <cstring>
#include <cassert>

using namespace std;

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define present(c,x) ((c).find(x) != (c).end()) 
#define sqr(x) ((x) * (x))
#define dist(x1, y1, x2, y2) (sqrt(sqr((x1) - (x2)) + sqr((y1) - (y2))))
#define pow2(x) (1 << (x))

const int dir[8][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}};

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;

const int inf = 0x7f7f7f7f;
const double eps = 1e-9;


const int maxn = 1000;
long long a[maxn], b[maxn];
int n;

void init()
{
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
	scanf("%lld", &a[i]);
    }
    for (int i = 0; i < n; ++i) {
	scanf("%lld", &b[i]);
    }
}

void run()
{
    sort(a, a + n);
    sort(b, b + n, greater<long long>());
    long long res = 0;
    for (int i = 0; i < n; ++i) {
	res += a[i] * b[i];
    }
    printf("%lld\n", res);
}

int main(void)
{
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
	printf("Case #%d: ", i);
	init();
	run();
    }
    return 0;
}

