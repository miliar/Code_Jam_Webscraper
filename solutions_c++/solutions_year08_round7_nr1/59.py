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

map<string, int> mix;
int l[1024];
bool isMix[1024];
int ed[1024][1024], childs[1024];
int nmix;

int put(string& foo)    {
    if (mix.find(foo) == mix.end()) {
        mix[foo] = nmix++;
    }
    return mix[foo];
}

int ans;

void getChilds(int u)   {
    childs[u] = 0;
    FOR (idx, 0, l[u])  {   
        int v = ed[u][idx];
        if (isMix[v])   childs[u]++;
    }
}

void dfs(int u) {
//    int ret = 1;
    
    vector<pair<int, int> > ch;

    FOR (idx, 0, l[u])   {
        int v = ed[u][idx];
        if (isMix[v])   {
            ch.PB(MP(childs[v], v));
        }
    }
    
    SORT(ch);

    int cnt = 0;
    for (int idx = ch.SZ-1; idx >= 0; --idx)    {
        int v = ch[idx].second;
        ans = max(ch[idx].first + cnt + 1, ans);
        cnt++;
    }    

    ans = max(childs[u] + 1, ans);

    /*
    FOR (idx, 0, l[u])   {
        int v = ed[u][idx];
        if (isMix[v])   {
            ret++;
            dfs(v);
        }
    }
    */
    
}


int main(void)	{
	int numTests;
	cin >> numTests;
	FOR (nc, 1, numTests+1)	{
        int N;
		cin >> N;
        nmix = 0;
        mix.clear();
        memset(isMix, 0, sizeof isMix);
        memset(ed, 0, sizeof ed);
        memset(l, 0, sizeof l);
        ans = 0;

        int start = -1;
        FOR (i, 0, N)   {
            string s;
            cin >> s;
            int node = put(s);
            if (i == 0) {
                start = node;
                assert(start == 0);
            }

            int nedges;
            cin >> nedges;
            
            FOR (j, 0, nedges)  {
                cin >> s;
                int idx = put(s);

                if (s[0] >= 'A' && s[0] <= 'Z') {   //mixture
                    isMix[idx] = true;
                }
                ed[node][l[node]++] = idx;
            }
        }
        memset(childs, 0, sizeof childs);
        FOR (i, 0, nmix)    {
            getChilds(i);
        }

        dfs(start);
		cout << "Case #" << nc << ": " << ans << endl;
	}
	
	
}
