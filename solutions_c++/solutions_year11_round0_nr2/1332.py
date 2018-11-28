#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>

using namespace std;

#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;

int main(void)	{
	int cases;
	cin >> cases;
	FOR (nc, 1, cases+1)	{
        int C;
        cin >> C;

        char a[128];
        map<pair<char, char>, char> combine;
        set<pair<char, char> > oppose;

        FOR (i, 0, C)   {
            cin >> a;
            combine[MP(a[0], a[1])] = a[2];
            combine[MP(a[1], a[0])] = a[2];
        }
        cin >> C;
        FOR (i, 0, C)   {
            cin >> a;
            oppose.insert(MP(a[0], a[1]));
            oppose.insert(MP(a[1], a[0]));
        }
        cin >> C;
        cin >> a;
        assert(strlen(a) == C);
        
        vector<char> q;
        FOR (i, 0, C)   {
            q.PB(a[i]);
            
            while (q.SZ >= 2)  {
                pair<char, char> pr = MP(q[q.SZ - 1], q[q.SZ - 2]);
                if (combine.count(pr) != 0)   {
                    q.pop_back();
                    q.pop_back();
                    q.PB(combine[pr]);
                }
                else    {
                    break;
                }
            }
            FOR (i, 0, q.SZ - 1)    {
                if (oppose.find(MP(q[i], q[q.SZ - 1])) != oppose.end()) {
                    q.clear();
                    break;
                }
            }
        }
		cout << "Case #" << nc << ": [";
		FOR (i, 0, q.SZ)    {
            cout << q[i];
            if (i < q.SZ - 1)   cout << ", ";
		}
        cout << "]" << endl;
		
	}
	
	
}
