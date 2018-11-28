#include <iostream>
#include <vector>

using namespace std;

int nc;

int R,k,N;

int main(){
    cin >> nc;
    for (int q= 1; q<=nc; q++){
        cerr << "q = " << q << endl;
        cin >> R >> k >> N;
        long long grupos[N];
        long long profit[N];
        long long nextpos[N];
        memset(profit,0,sizeof(profit));
        memset(nextpos,0,sizeof(nextpos));
        for (int i=0;i<N;i++) cin >> grupos[i];
        for (int i=0;i<N;i++){
            long long curr = 0;
            for (int j=0;j<N && curr <= k;j++){
                if (curr + grupos[(i+j)%N] <= k){
                   profit[i]+=grupos[(i+j)%N];
                   curr+=grupos[(i+j)%N];
                }
                else {
                     nextpos[i] = (i+j)%N;
                     break;
                }
            }
        }
        //for (int i=0;i<N;i++) cout << nextpos[i] << " ";
        //cout << endl;
        long long totprof=0;
        long long index = 0;
        for (int i=0;i<R;i++){
            totprof+=profit[index];
            index = nextpos[index];
        }
        cout << "Case #" << q << ": " << totprof << endl;
    }
    return 0;
}
