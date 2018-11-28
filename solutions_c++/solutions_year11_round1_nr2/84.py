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

vector<string> words;
string ord;
int listpos[26];
int best, bestw;
int ans[128];

vector<pair<int, vector<int> > > split(vector<pair<int, int> >& v)   {
    vector<pair<int, vector<int> > > vv;
    int i = 0;
    while (i < v.SZ)    {
        int j = i;
        int crit = v[i].first;
        while (j < v.SZ && v[j].first == v[i].first)    j++;
        vector<int> tmp(j - i);
        int k = 0;
        while (i < j)   {
            tmp[k] = v[i].second;
            k++;
            i++;
        }
        vv.PB(MP(crit, tmp));
    }
    return vv;
}


void go(vector<int>& widx, vector<int>& spots, int cur)   {
    if (spots.SZ == 0)  {
        if (best < cur || (best == cur && bestw > widx[0])) {
            best = cur;
            bestw = widx[0];
        }
        return;
    }
    
    int pos = 26;
    FOR (i, 0, widx.SZ) {
        FOR (j, 0, spots.SZ) {
            char ch = words[widx[i]][spots[j]];
            pos = min(pos, listpos[ch-'a']);
        }
    }
    
    vector<pair<int, int> > v;  
    FOR (i, 0, widx.SZ) {
        int msk = 0;
        FOR (j, 0, spots.SZ) {
            char ch = words[widx[i]][spots[j]];
            if (ch == ord[pos]) {
                msk |= (1<<spots[j]);
            }
        }
        v.PB(MP(msk, widx[i]));
    }
    
    SORT(v);
    vector<pair<int, vector<int> > > splits = split(v);
    FOR (i, 0, splits.SZ)   {
        int msk = splits[i].first;
        vector<int> nextspots;
        FOR (j, 0, spots.SZ)   {
            if ((msk & (1<<spots[j])) == 0) {
                nextspots.PB(spots[j]);
            }
        }
        go(splits[i].second, nextspots, cur + (msk == 0 ? 1 : 0));
    }
}


void lengo(vector<int>& widx)   {
    vector<pair<int, int> > v;
    
    FOR (i, 0, widx.SZ) {
        v.PB(MP(words[widx[i]].SZ, widx[i]));
    }
    
    SORT(v);
    vector<pair<int, vector<int> > > splits = split(v);
    FOR (i, 0, splits.SZ)   {
        vector<int> empty;
        FOR (j, 0, splits[i].first) {
            empty.PB(j);
        }
        go(splits[i].second, empty, 0);
    }
}


int main(void)	{
	int T, N, M;
	cin >> T;
	FOR (nc, 1, T+1)	{
        cin >> N >> M;
        
        words.clear();
        words.resize(N);
        FOR (i, 0, N)   {
            cin >> words[i];
        }
        
        vector<int> widx(N);
        FOR (i, 0, N)   {
            widx[i] = i;
        }
        
        FOR (i, 0, M)   {
            cin >> ord;
            assert(ord.SZ == 26);
            FOR (j, 0, 26)    {
                assert('a' <= ord[j] && ord[j] <= 'z');
                listpos[ord[j]-'a'] = j;
            }
            best = -1, bestw = -1;

            lengo(widx);
            assert(bestw != -1);
            
            ans[i] = bestw;
        }
		
		cout << "Case #" << nc << ":";
        FOR (i, 0, M)   {
            cout << " " << words[ans[i]];
        }
        cout << endl;
	}
	
	
}
