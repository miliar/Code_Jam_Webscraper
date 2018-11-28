#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <utility>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef long long ll;
typedef pair<int, int> pii;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))

#define FOR(i,a,b) for (int i=(a); i<(b); ++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(), (a).end()
#define SORT(a) sort(ALL(a))
#define pb push_back


int main(int argc, char** argv)
{
    ifstream in(argv[1]);
    int testnum;
    in >> testnum;
    string eof;
    getline(in, eof);

    for (int h=0; h<testnum; ++h)
    {
        long long ret = 0;
        int p, k, l;
        list<int> alpha;
        in >> p >> k >> l;
        list<int> num(k, 1);
        
        REP(i, l)
        {
            int temp;
            in >> temp;
            alpha.pb(temp);
        }

        //list<int>::iterator ppp;
        //for (ppp = alpha.begin(); ppp != alpha.end(); ++ppp)
        //    cout << *ppp << endl;

        REP(i, l)
        {
            list<int>::iterator pos = max_element(ALL(alpha));
            int current = *pos;
            list<int>::iterator pos2 = min_element(ALL(num));
            int here = *pos2;
            ret += here * current;
            ++(*pos2);
            if (here == p)
                num.erase(pos2);
            alpha.erase(pos);
        }


        cout << "Case #" << h+1 << ": " << ret; 

        cout << endl;
    }    
}
