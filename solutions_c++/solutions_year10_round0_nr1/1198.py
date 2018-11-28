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
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////


int main() {
    int TT, N, K;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d", &N, &K);
        printf("Case #%d: %s\n", tt+1, (K+1)%(1<<N) ? "OFF" : "ON");
    }
}


