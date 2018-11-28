#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <climits>
#include <cfloat>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <numeric>
#include <complex>
#include <utility>
#include <memory>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <sstream>
#include <assert.h>
using namespace std;

const double EPS = 1e-9;
const int INF = 100000000;
const int MOD = 1000000007;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vst;
typedef pair<int,int> pint;
typedef long long ll;

template<class T1, class T2> ostream& operator<<(ostream &s, pair<T1,T2> P){return s<<'<'<<P.first<<", "<<P.second<<'>';}
template<class T> ostream& operator<<(ostream &s, vector<T> P) {s<<"{ ";for(int i=0;i<P.size();++i){if(i>0)s<<", ";s<<P[i];}return s<<" }"<<endl;}
template<class T> ostream& operator<<(ostream &s, vector<vector<T> > P) {for(int i=0;i<P.size();++i){s<<i<<" : "<<P[i];}return s;}




int main() {    
    freopen( "/Users/macuser/Downloads/B-large.in", "r", stdin );
	freopen( "/Users/macuser/Downloads/output.txt", "w", stdout );
    
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i) {
        int N,S,P;        vint pok;
        vint aok;
        
        cin >> N >> S >> P;
        
        int smin = max(P, P*3-4);
        int nmin = max(smin, P*3-2); 
        
        for (int j = 0; j < N; ++j) {
            int temp;
            cin >> temp;
            
            if (temp > 30) continue;
            if (temp >= nmin) aok.push_back(temp);
            else if (temp >= smin) pok.push_back(temp);
        }
        //cout << pok << aok;
        
        int res = min(S, (int)pok.size()) + (int)aok.size();
        
        printf("Case #%d: %d\n", i+1, res);

    }
    
	return 0;
}













