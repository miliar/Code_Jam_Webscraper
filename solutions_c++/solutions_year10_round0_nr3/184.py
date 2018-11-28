#include <iostream>
using namespace std;
int main()
{
    int R , k , N, G[2000];
    int  t0;
    cin >> t0; for (int tt = 1; tt<= t0; tt++) {
        cin >> R >> k >> N;
        for (int i = 0 ; i < N ; i++) cin >> G[i];
        for (int i = 0 ; i< N; i++) G[N+i] = G[i];
        int next[ 2000];
        long long  add [ 2000];
        for (int i = 0  ; i <N; i++) {
            long long  tmp  = 0 ;
            for (int j  = 0 ; j <=N; j++) {
                tmp += G[i+j];
                next[i] = i+j;
                if (tmp > k ) break;
            }
            add[i] = 0 ;
            for (int j = i; j<next[i]; j++)  add[i]+=G[j];
            if (next[i]>=N) next[i]-=N;
        }
    /*    for (int i  = 0 ; i  < N; i++) cout << G[i]<<' ' ;
        cout << endl;
        for (int i  = 0 ; i  < N; i++) cout << next[i]<<' ' ;
        cout << endl;
        for (int i  = 0 ; i  < N; i++) cout << add[i]<<' ' ;
        cout << endl;        
    */
        long long  ans  =  0; 
        int p = 0 ;
        for (int i =  0 ; i < R ; i++) {
            ans += add[p];
            p= next[p];
          }
        cout <<"Case #"<<tt<<": "<< ans << endl;
    }
}
