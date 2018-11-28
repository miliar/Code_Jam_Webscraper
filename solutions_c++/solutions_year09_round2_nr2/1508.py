/*
 * Question: Find words matching the pattern
 * Author: Divye Kapoor
 * Date: 3 Sep 2009
 * 
 */
#include <iostream>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <cassert>
#include <sstream>

using namespace std;

#define FOR(i, l, u) for(int i =(int)(l); i < (int)(u); ++i)
#define REP(i, u) FOR(i, 0, u)
#define LET(x, a) __typeof(a) x(a)
#define IFOR(it, b, e) for(LET(it,b); it != e; ++it)
#define SHIFTL(i, n) ((i) << (n))
#define SHIFTR(i, n) ((i) >> (n))
#define POW2(n) (1 << (n))

typedef vector<int> v_i;
typedef vector<string> v_s;
typedef set<int> set_i;
typedef set<string> set_s;
typedef map<string,int> map_si;
typedef pair<int,int> p_i;

int T;
char N[21];
int main() {
    scanf("%d", &T);
    REP(i, T) {
        scanf("%s", N);
        vector<int> v(strlen(N));
        REP(x, v.size()){
            v[x] = N[x] - '0';
        }
        int t = atoi(N);
        bool c = true;
        vector<int> vc(v);
        copy(v.begin(), v.end(), ostream_iterator<int>(cerr, " "));
        cerr << '\n';
        if(next_permutation(vc.begin(), vc.end())) {
            int r = 0;
            REP(k, vc.size()) {
                r = r*10 + v[k];
            }
            if(r < t) c = true;
            else c = false;
        }
        
        if(!c) {
            v = vc;
        }
        
        copy(v.begin(), v.end(), ostream_iterator<int>(cerr, " "));
        cerr << '\n';
        if(c) {
            vector<int>::iterator m, min = v.end();
            for(m = v.begin(); m != v.end(); ++m) {
                if(min == v.end() && *m != 0) min = m;
                
                if (min != v.end() && *m < *min && *m != 0) {
                    min = m;
                }
            }
            copy(v.begin(), v.end(), ostream_iterator<int>(cerr, " "));
            cerr << '\n';
            cerr << "min = " << *min << endl;
            iter_swap(v.begin(), min);
            copy(v.begin(), v.end(), ostream_iterator<int>(cerr, " "));
            cerr << '\n';
            v.push_back(0);
            sort(v.begin()+1, v.end());
            copy(v.begin(), v.end(), ostream_iterator<int>(cerr, " "));
            cerr << '\n';
        }
        int r = 0;
        REP(k, v.size()) {
            r = r*10 + v[k];
        }
        printf("Case #%d: %d\n", i+1, r);
    }
	return 0;
}
