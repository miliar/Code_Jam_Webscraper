#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
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
#define FORE(i, a, b) for(typeof(a) i = a ; i <= b ; i++)
#define tr(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define dbg(x) cout << #x << " : " << x << "; " << flush;
#define dbge(x) cout << #x << " : " << x << ";" << endl;
#define GI ({int t; scanf("%d", &t); t;})
typedef long long LL;
typedef pair <int, int> II;
typedef vector <int> VI;

string toStr(LL no)
{
    string ret = "";
    while(no)
    {
	int d = no % 10;
	no /= 10;
	ret += d + '0';
    }
    reverse(all(ret));
    return ret;
}
int main()
{
    int t = GI;
    FORZ(test, t)
    {
	string no;
	cin >> no;
	no = "0" + no;
	next_permutation(all(no));
	if(no[0] == '0')
	    no = no.substr(1);
	printf("Case #%d: %s\n", test+1, no.c_str());
    }
    return 0;
}
