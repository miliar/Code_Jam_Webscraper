#include <iostream>
using namespace std;


int T[1<<13][11];
int P, N;
int M[1<<12];


static const int TOO_MUCH = 1000000000;

int main() {
    int TT; cin>>TT;
    for (int t=1; t<=TT; t++) {
        cin>>P;
        N = (1<<P);
        for (int i=N+N-1; i>=N; i--) {
            int m; cin>>m;
            for (int j=0; j<=P; j++)
                T[i][j] = (j<=m) ? 0 : TOO_MUCH;
        }
        
        for (int i=N-1; i>=1; i--) {
            int leftIx = 2*i;
            int rightIx = 2*i+1;
            int c; cin>>c;
            for (int j=0; j<=P; j++) {
                int notAttend;
                if (j<P)
                    notAttend = T[leftIx][j+1] + T[rightIx][j+1];
                else
                    notAttend = TOO_MUCH;
                int attend = T[leftIx][j] + T[rightIx][j] + c;
                
                T[i][j] = min(TOO_MUCH, min(attend, notAttend));
            }
        }
        
        cout<<"Case #"<<t<<": "<<T[1][0]<<endl;
    }
    
    return 0;
}
