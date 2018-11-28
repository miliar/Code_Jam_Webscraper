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

vi pow10(12, 1);
vvi rec(2000001, vi());
vi nrec(2000001, 0);

typedef map<int, vector<bool> > mapivb;

int solve(int a, int b)
{
    int l = b - a + 1;
    map<int, set<int> > d;

    int t = 0;
    forz(i, a, b+1) {
        if(nrec[i]) {
            forx(j, sz(rec[i])) {
                int cand = rec[i][j];
                //cout << i << " -> " << cand << endl;
                if(cand >= a && cand <= b && cand != i)
                    if(!exists(d[i], cand)) {
                        t++;
                        d[i].insert(cand);
                        d[cand].insert(i);
                    }
            }
        }
    }

    return t;
}

int main() 
{
    // init pow10
    forz(i, 1, 12) pow10[i] = pow10[i-1] * 10;
    // init recycled table
    forx(i, 7) {
        int a = pow10[i];
        int b = i == 6 ? 2000000 : pow10[i + 1] - 1;
        forz(j, a, b+1) {
            // here i+1 equal to number of digits in j
            for(int k = 1; k < i + 1; k++) {
                int p = (j % pow10[k] ) * pow10[i + 1 - k] + j / pow10[k];
                if(a <= p && p <= b && p != j) {
                    rec[j].push_back(p);
                    nrec[j]++;
                }
            }
        }
    }

    string line;
    getline(cin, line);
    int T = strtol(line.c_str(), 0, 10);

    for(int t=1; t <= T; t++)
    {
        getline(cin, line);
        istringstream is(line);
        int a; int b; is >> a; is >> b;

        cout << "Case #" << t << ": " << solve(a, b) << endl;
    }   
    
    return 0;
}
    
