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

vs split(const string& s, const string& delim = " ") { vector<string> res; string t; for ( unsigned int i = 0 ; i != s.size() ; i++ ) { if ( delim.find( s[i] ) != string::npos ) { if ( !t.empty() ) { res.push_back( t ); t = ""; } } else { t += s[i]; } } if ( !t.empty() ) { res.push_back(t); } return res; }

int N, M;
set<vs> ss;

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "r", stdin);
	
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);

    //freopen("A-small-attempt1.in", "r", stdin);
    //freopen("A-small-attempt1.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int numtest, test, i, j, ans;
    string str;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        cin >> N >> M;
        ss.clear();
        for (i=0; i<N; i++)
        {
            cin >> str;
            vs w = split(str, "/");
            if (sz(w) > 0)
            {
                vs ww;
                for (j=0; j<sz(w); j++)
                {
                    ww.pb(w[j]);
                    ss.insert(ww);
                }
            }
        }
        ans = 0;
        for (i=0; i<M; i++)
        {
            cin >> str;
            vs w = split(str, "/");
            if (sz(w) > 0)
            {
                vs ww;
                for (j=0; j<sz(w); j++)
                {
                    ww.pb(w[j]);
                    if (!ss.count(ww))
                    {
                        ans++;
                        ss.insert(ww);
                    }
                }
            }
        }
        cout << "Case #" << (test) << ": " << ans << endl;
	}
	return 0;
}
