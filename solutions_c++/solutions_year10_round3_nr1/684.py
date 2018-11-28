#include <iostream>
#include <vector>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<_b; i++)
#define REP(i,n) FOR(i,0,n)

typedef long long ll;
typedef std::vector<ll> VL;

using namespace std;

static void solve_case(int i);

int main(void){
    int N;
    cin >> N;
    for(int i = 0; i < N; i++){
        solve_case(i+1);
    }
    return 0;
}

void solve_case(int cn){
    VL A,B;
    int N;
    cin >> N;
    REP(i,N) {
        int a,b;
        cin >> a >> b;
        A.push_back(a);
        B.push_back(b);
    }

    int result = 0;
    REP(i,N) FOR(j,i+1,N){

        result += (A[i] > A[j]) * (B[j] > B[i]);
        result += (A[i] < A[j]) * (B[j] < B[i]);

    }
    cout << "Case #" << cn << ": " << result << endl;
}
