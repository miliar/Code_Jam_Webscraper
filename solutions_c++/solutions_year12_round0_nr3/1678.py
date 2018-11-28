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
int A, B;

void solve(int caseNum){
    //solve problem here
    int res = 0;
    for(int n = A; n <= B; ++n){
        int d = 10;
        set<int> st;
        for(; n / d > 0; d *= 10) ;
        for(int d1 = 10; d1 < d; d1 *= 10){
            int d2 = d / d1;
            int a = n / d1, b = n % d1;
            int m = b * d2 + a;
            if(b * 10 / d1 == 0) continue;
            if(n >= m || m < A || B < m) continue;
            if(st.find(m) != st.end()) continue;
            st.insert(m);
            ++res;
        }
    }
    cout << "Case #" << caseNum << ": " << res << endl;
}

int main(){
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        //input test case here
        cin >> A >> B;

        solve(t);
    }
    return 0;
}
