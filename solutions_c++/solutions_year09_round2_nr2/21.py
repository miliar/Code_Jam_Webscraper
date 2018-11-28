#include <string>
#include <cstring>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;

#define INF 1000000000
#define PB push_back
 
//////////////////////////////////////////


int main() {
    int N;
    scanf("%d", &N);
    REP(t, N) {
        char buf[1000];
        string res;
        scanf("%s", buf);
        res = buf;
        bool x = next_permutation(res.begin(), res.end());
        if (!x) 
            res = res.substr(0, 1)+"0"+res.substr(1);
        int ile = 0;
        while (res[0]=='0') { ile++; res = res.substr(1); }
        REP(a, ile) { res = res.substr(0, 1)+"0"+res.substr(1); }
        printf("Case #%d: %s\n", t+1, res.c_str());
    }
    
}


