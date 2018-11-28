#include <string> 
#include <algorithm> 
#include <cfloat> 
#include <climits> 
#include <cmath> 
#include <complex> 
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <functional> 
#include <iostream> 
#include <map> 
#include <memory> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <vector> 

#define EACH(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define ALL(x) (x).begin(),(x).end() 
using namespace std;
const double eps = 1e-10;

//input data
int N, T, S, p, t[100];

int check(int t, int p){
    int res = 3;
    for(int i = 0; i <= 10 && i <= t; ++i){
        for(int j = i; j <= 10 && i + j <= t; ++j){
            int k = t - (i + j);
            int mx = max(i, max(j, k)), mn = min(i, min(j, k));
            if(mx >= p)
                res = min(res, mx - mn);
        }
    }
    return res;
}
void solve(int caseNum){
    //solve problem here
    int res = 0;
    sort(t, t + N, greater<int>());
    for(int i = 0; i < N; ++i){
        int c = check(t[i], p);
        if(c <= 1){
            ++res;
        }
        else if(c <= 2 && S > 0){
            ++res;
            --S;
        }
    }
    cout << "Case #" << caseNum << ": " << res << endl;
}

int main(){
    int T;
    cin >> T;

    for(int a=1; a<=T; ++a){
        //input test case here
        cin >> N >> S >> p;
        for(int i = 0; i < N; ++i){
            cin >> t[i];
        }
        solve(a);
    }
    return 0;
}
