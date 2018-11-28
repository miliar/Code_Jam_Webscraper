/* 
look at my code
my code is amazing
give it a lick
mmm - it tastes just like raisins

have a stroke of its mane
it turns into a plane
and then it turns back again
when you tug on its winkie

eww that's dirty
do you think so?
Well I better not show you where
the lemonade is made

sweet lemonade
mmm - sweet lemonade
sweet lemonade
yeah sweet lemonade

get on my code
I'll take you around the universe
and all the other places too

I think you'll find that the universe
pretty much covers everything

Shut up woman get on my code! 
*/

//another_fine_solution by Askar

// input/output
#include <cstdio>
#include <iostream>
// structures
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <tr1/unordered_set>
#include <tr1/unordered_map>
// other stuff
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <utility>

using namespace std;
using namespace std::tr1;

#ifdef EBUG
    #define dbg if(1)
    #define NOFORK 
#else
    #define dbg if(0)
#endif

// vlastny assert
#define assert(x) if(!(x)) ERR(x)
#ifdef NOFORK
    #define ERR(x) cerr << "F: " << __FUNCTION__ << "(), L: " << __LINE__ << ", (" << #x << ") isn\'t true\n";
#else
    #define ERR(x) fork()
#endif

#define MINIM(x, y) x = min(x, (y))
#define MAXIM(x, y) x = max(x, (y))
#define db(x) dbg cerr << #x << "\t: " << (x) << endl;
#define iter(x) typeof((x).begin())
#define FOR(i,n) for(int i = 0; i < (n); i++)
#define FOR1(i, n) for(int i = 1; i <= (n); i++)
#define Foreach(it, str) for(typeof((str).begin()) it = (str).begin(); it != (str).end(); it++)
#define ULTIM(i, N, a) dbg{ cerr << #a << endl; FOR(i, N) cerr << a << " "; cerr << endl << endl;}
#define mp make_pair
#define PASS
typedef long long ll;
const long long INF = 2000000000;
const double EPS = 1e-9;

const int MAXN = 10047;

int N, D;

int vd[MAXN];
int vl[MAXN];
int maxl[MAXN];

void vypis(bool da_sa, int t){
    cout << "Case #" << t << ": ";
    if(da_sa)  cout << "YES\n";
    else cout << "NO\n";
}

void zrataj(int t){
    if(vl[0] < vd[0]){
        vypis(false, t);
        return;
    }
    maxl[0] = vd[0];

    queue<int> qu;
    qu.push(0);

    while(!qu.empty()){
        int x = qu.front(); qu.pop();

        int pp = x+1;
        while(pp < N && abs(vd[x] - vd[pp]) <= maxl[x]){
            if(maxl[pp] == -1 || maxl[pp] < min(vl[pp], abs(vd[x] - vd[pp]))){
                maxl[pp] = min(vl[pp], abs(vd[x] - vd[pp]));
                qu.push(pp);
            }
            pp++;
        }
    }
    
    FOR(i, N){
        if(vd[i] == D && vl[i] == 0){
            if(maxl[i] == 0){ 
                vypis(true, t);
                return;
            }
            else{
                vypis(false, t);
                return;
            }
        }
    }


}

int main(){
    int T;
    cin >> T;
    FOR1(t, T){
        ///////////////////
        cin >> N;
        vector<pair<int, int> > tried;
        FOR(i, N){
            int d;
            int l;
            cin >> d >> l;
            tried.push_back(mp(d,l));
            maxl[i] = -1;
        }
        cin >> D;
        maxl[N] = -1; 
        tried.push_back(mp(D, 0));
        N++;
        sort(tried.begin(), tried.end());

        FOR(i, N){
            vd[i] = tried[i].first;
            vl[i] = tried[i].second;
        }
         
        zrataj(t);

        //////////////////
    }
}
