#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#define dbg(x)// cout << #x << " : " << x << "; " << flush;
#define dbge(x) //cout << #x << " : " << x << ";" << endl;
#define GI ({int t; scanf("%d", &t); t;})
typedef long long LL;
typedef pair <int, int> II;
typedef vector <int> VI;

//FILE *fp = freopen("input", "r", stdin);
//FILE *f = freopen("output", "w", stdout);
map <int , int> vis;

int toBase(int val, int b)
{
    if(b == 10)
	return val;
    string ans = "";
    while(val)
    {
	ans += val%b + '0';
	val /= b;
    }
    reverse(all(ans));
    stringstream ss(ans);
    int ret;
    ss >> ret;
    return ret;
}

bool happy (int bno, int base)
{
    int sd = 0;
    if(vis[bno])
	return false;
    if(bno == 1)
	return true;
    vis[bno]++;
dbg(bno);dbg(base);    
    while(bno)
    {
	int dig = bno % 10;
	sd += dig * dig;
	bno /= 10;
    }
    dbge(sd);
    return happy(toBase(sd, base), base);
}

int main()
{
    int t = GI;
    getchar();
    FORZ(test, t)
    {
	string line;
	getline(cin, line);
	stringstream ss(line);
	VI bases;
	int val;
	int N = 0;
	while(ss >> val)
	{
	    bases.PB(val);
	    N++;
	}
/*	FORZ(i, N)
	cout << bases[i] << " ";
	cout << endl;
*/
	val = 2;
	while(true)
	{
        dbge(val);
	    VI bNos(N);
	    FORZ(i, N)
		bNos[i] = toBase(val, bases[i]);
/*		FORZ(i, N)
            cout << bNos[i] << " ";
	    cout << endl;
     GI;*/
	    bool ok = true;
	    FORZ(i, N)
	    {
		vis.clear();
		if(!happy(bNos[i], bases[i]))
		{
		    ok = false;
		    break;
		}
	    }
	    if(ok)
	    {
		printf("Case #%d: %d\n", test+1, val);
		break;
	    }
	    val++;
	}
    }
    return 0;
}
