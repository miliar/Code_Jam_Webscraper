#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
//#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
//#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <string>

using namespace std;

#define MP make_pair
#define FF first
#define SS second
#define SZ size()
#define PB push_back
#define all(x) (x).begin(), (x).end()
#define FORZ(i, n) for(typeof(n) i = 0 ; i !=n ; i++)
#define tr(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define dbg(x) //cout << #x << " : " << x << "; " << flush;
#define dbge(x) //cout << #x << " : " << x << ";" << endl;
#define GI ({int t; scanf("%d", &t); t;})
typedef long long LL;
typedef pair <int, int> II;
typedef vector <int> VI;

string line;
string pat = "welcome to code jam";
int MOD = 10000;
int dp[501][20];
int ps, ls;

int cal(int lid, int pid)
{
    if(pid == ps)
	return 1;
    if(lid == ls)
	return 0;
    int & ret = dp[lid][pid];
    if(ret != -1)
	return ret;
    ret = 0;
    for(int i = lid; i < ls ; i++)
	if(line[i] == pat[pid])
	    ret = (ret + cal(i+1, pid + 1)) % MOD;
    return ret;
}

int main()
{
    int T;
    scanf("%d\n", &T);
    ps = pat.SZ;
    FORZ(test, T)
    {
	getline(cin, line);
	ls = line.SZ;
	FORZ(i, 500)
	    FORZ(j, 20)
	    	dp[i][j] = -1;
	printf("Case #%d: %04d\n", test+1, cal(0, 0));
    }
    return 0;
}
