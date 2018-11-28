#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
#include <cmath>

using namespace std;

typedef long long ll;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

#define x first
#define y second
#define c first

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
            cout << "Case #" << t << ": ";
            int N,K,B,T;
            cin >> N >> K >> B >> T;
            vector<int> x(N),v(N);
            for(int i=0;i<N;i++) cin >> x[i];
            for(int i=0;i<N;i++) cin >> v[i];
            
            int no = 0;
            int swaps = 0;
            int k = 0;
            for(int i=N-1;i>=0;i--){
                    if(v[i] * T + x[i] >= B){ swaps += no; k++; }
                    else no++;
                    if(k == K) break;
            }
            if( k != K) cout << "IMPOSSIBLE" << endl;
            else cout << swaps << endl;
    }
}
