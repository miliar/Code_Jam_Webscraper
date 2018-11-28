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
#define dbg(x) cout << #x << " : " << x << "; " << flush;
#define dbge(x) cout << #x << " : " << x << ";" << endl;
#define GI ({int t; scanf("%d", &t); t;})
typedef long long LL;
typedef pair <int, int> II;
typedef vector <int> VI;

bool match(vector <string> & pat, string & str)
{
    int s = str.SZ;
    FORZ(i, s)
	if(pat[i].find(str[i]) == string :: npos)
	    return false;
    return true;
}

int main()
{
    GI;
    int aleanSZ = GI, patSZ = GI;
    vector <string> Alean;
    string tmp;
    
    FORZ(i, aleanSZ)
    {
	cin >> tmp;
	Alean.PB(tmp);
    }

    vector < vector < string > > pattern(patSZ);

    FORZ(i, patSZ)
    {
	string pat;
	cin >> pat;
	int ps = pat.SZ;
	FORZ(p, ps)
	{
	    tmp = "";
	    if(pat[p] == '(')
	    {
		p++;
		while(pat[p] != ')')
		    tmp = tmp + pat[p++];
		pattern[i].PB(tmp);
	    }
	    else {
		tmp = " ";
		tmp[0] = pat[p];
		pattern[i].PB(tmp);
	    }
	}

    }

    int count[patSZ];
    memset(count, 0, sizeof count);

    FORZ(pat, patSZ)
	FORZ(ale, aleanSZ)
	    if( match(pattern[pat], Alean[ale]) )
		count[pat]++;

    FORZ(i, patSZ)
	printf("Case #%d: %d\n", i+1, count[i]);
    return 0;
}


