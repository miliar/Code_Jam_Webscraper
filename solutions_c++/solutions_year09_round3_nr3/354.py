#include <iostream>
using namespace std;
#include <climits>

int main(void){
    int cases;
    cin >> cases;
    for(int c=0;c<cases; ++c){
        int p,q;
        int qs[128];
        int dp[128][128];
        cin >> p >> q;
        qs[0]=0;
        for(int i=1;i<=q;++i)
            cin >> qs[i];
        qs[q+1]=p+1;
        for(int i=0;i<=q;++i)
            dp[0][i] = qs[i+1]-qs[i]-1;
        for(int i=1;i<=q;++i){
            for(int j=0;j<=q-i;++j){
                int min = INT_MAX;
                for(int k=0;k<i;++k){
                    if(dp[k][j]+dp[i-k-1][j+k+1]<min)
                        min = dp[k][j]+dp[i-k-1][j+k+1];
                }
                dp[i][j] = min+qs[i+j+1]-qs[j]-1;
            }
        }
        /*for(int i=0;i<=q+1;++i)
            cout << qs[i] << " ";
        cout << endl;
        for(int i=0;i<=q;++i){
            for(int j=0;j<=q-i;++j)
                cout << dp[i][j] << " ";
            cout << endl;
        }
        cout << endl;*/
        cout << "Case #" << c+1 << ": " << dp[q][0]-p << endl;
    }
    return 0;
}
