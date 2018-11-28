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
#include <ctime>
 
using namespace std;

#define sz(a) (LL)a.size()
#define all(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair<int, int> pii;
#define LL long long
#define INF 1000000

int D, I, M, N;
int cache[105][1600];
int a[105];

int fix(int be, int en)
{
    int dif = abs(en-be);
    if (dif==0) return 0;
    if (M==0) return 1000000;
    int need = (dif-1) / M;
    return need * I;
}

int calc(int v, int lastKeep)
{
    int& res = cache[v][lastKeep+520];
    if (res>=0) return res;
    if (v==N)
    {
        return res=0;
    }
    int i;
    if (lastKeep==1000) //never kept
    {
        res = D + calc(v+1, 1000);
        //res = min(res, calc(v+1, a[v]));
        for (i=-520; i<=520; i++)
            res = min(res, abs(i-a[v]) + calc(v+1, i));
        return res;
    }
    res = D + calc(v+1, lastKeep);
    //res = min(res, fix(lastKeep, a[v]) + calc(v+1, a[v]));
    for (i=-520; i<=520; i++)
        res = min(res, fix(lastKeep, i) + abs(i-a[v]) + calc(v+1, i));
    return res;
}

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "r", stdin);
	
    //freopen("B-small-attempt0.in", "r", stdin);
    //freopen("B-small-attempt0a.out", "w", stdout);

    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);

	//freopen("B-large.in", "r", stdin);
	//freopen("B-large.out", "w", stdout);

	int numtest, test;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        cin >> D >> I >> M >> N;
        for (int i=0; i<N; i++) cin >> a[i];
        memset(cache, -1, sizeof(cache));
        int ans = calc(0, 1000);
		cout << "Case #" << (test) << ": " << ans << endl;
	}
	return 0;
}
