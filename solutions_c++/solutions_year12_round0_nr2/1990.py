#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<vvi> vvvi;
typedef vector<vvvi> vvvvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef vector<string> vs;
typedef vector< vector<string> > vvs;
#define all(c) (c).begin(), (c).end() 
#define rall(c) (c).rbegin(), (c).rend() 
#define sz(a) int((a).size()) 
#define forx(i,l) for(int i = 0; i < l; i++) 
#define forz(i,a,l) for(int i = (a); i < l; i++) 
#define forp(p,c) for(typeof((c).begin()) p = (c).begin(); p != (c).end(); p++) 
#define exists(c,x) ((c).find(x) != (c).end()) 
#define dumpvv(vv) forp(p,vv) { forp(q,*p) cout << *q << " "; cout << endl; }

// total points -> best unsurprizing score
vi bu(31, -1);
// total points -> best suprizing score
vi bs(31, -1);

void calc_triplets()
{
    forx(a, 11) forx(b, 11) forx(c, 11) {
        if(abs(a-b) <= 2  && abs(a-c) <= 2 && abs(b-c) <= 2)  {
            int best = max(a, max(b, c));
            int sum = a + b + c;
            if(abs(a-b) == 2 || abs(a-c) == 2 || abs(b-c) == 2)
                bs[sum] = max(best, bs[sum]);
            else
                bu[sum] = max(best, bu[sum]);
        }
    }
}

int solve(vvi& mem, int s, int p, vi& dd, int pos)
{
    if(mem[s][pos] != -1)
        return mem[s][pos];

    int sum = dd[pos - 1];
    int ret_s = bs[sum] >= p;
    int ret_u = bu[sum] >= p;

    int ret = 0;

    // last position
    if(pos == 1) 
        ret = s ? ret_s : ret_u; 
    // other position
    else {  
        if(s == 0)
            ret = ret_u + solve(mem, s, p, dd, pos-1);
        else if(s >= pos)
            ret = ret_s + solve(mem, s-1, p, dd, pos-1);
        else 
            ret = max(ret_s + solve(mem, s-1, p, dd, pos-1),
                       ret_u + solve(mem, s, p, dd, pos-1));
    }

    /*
    cout << "sum: " << sum << " best * for sum: " << ret_s;
    cout << " best _ for sum: " << ret_u;
    cout << " return: " << ret << endl;
    */
    return mem[s][pos] = ret;
}

int main() 
{
    calc_triplets();

    string line;
    getline(cin, line);
    int T = strtol(line.c_str(), 0, 10);

    for(int t=1; t <= T; t++)
    {

        getline(cin, line);
        istringstream is(line);
        int N; int s; int p;
        is >> N; is >> s; is >> p;

        vector<int> dd;
        int d;
        for(int j = 0; j < N; j++)
        {
            is >> d;
            dd.push_back(d);
        }
        vvi mem(s+2, vi(sz(dd)+2, -1));
        cout << "Case #" << t << ": " << solve(mem, s, p, dd, sz(dd)) << endl;
    }   
    
    return 0;
}
    
