#include <algorithm>
#include <cstdlib>
#include <climits>
#include <iostream>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <iomanip>

using namespace std;

typedef unsigned char byte;
typedef unsigned int uint;

vector<int> d, l;

int N, D;

bool can_reach(int k, int pos){
    int dist = d[k] - pos;
    if(pos + 2*dist >= D) return true;
    int i=k+1;
    while(i < N && d[i] <= d[k]+dist){
        if(l[i] >= d[i]-d[k]){
            if(can_reach(i, d[k])) return true;
        }
        else{
            if(can_reach(i, d[i] - l[i])) return true;
        }
        i++;
    }
    return false;
}

void solve(){
    cin >> N;
    d.resize(N);
    l.resize(N);
    for(int i=0; i<N; i++){
        cin >> d[i] >> l[i];
    }
    cin >> D;
    if(d[0] > l[0]){
        cout << "NO";
        return ;
    }
    if(can_reach(0, 0)) cout << "YES";
    else cout << "NO";
}

int main(){
    // cout << fixed << setprecision(6);
    int T;
    cin >> T;
    for(int t=1; t<=T; t++){
        cout << "Case #" << t << ": ";
        solve();
        cout << '\n';
    }
    return 0;
}
