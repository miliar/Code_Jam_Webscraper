#include <iostream>

using namespace std;

int T[55];
int R[55];
char buf[55];


int testcase(){
    int n; scanf("%d", &n);
    
    for (int i=1; i<=n; ++i){
        T[i] = 0;
        scanf("%s", buf+1);
        
        for (int j=1; j<=n; ++j){    
            if ( buf[j] == '1' ) T[i] = j;
        }
        
        
    }
    
    //for (int i=1; i<=n; ++i) cout << "." << T[i];
    //cout << endl;
    
    for (int i=1; i<=n; ++i) R[i] = 0;
    
    int moves = 0;
    
    int cur = 1;
    
    for (int i=1; i<=n; ++i){
        for (int j=1; j<=n; ++j){
            if ( R[j] != 1 && T[j] <= i ) {
                R[j] = 1;
                T[j] = cur;
                ++cur;
                break;
            }
        }
    }
    
    
    //for (int i=1; i<=n; ++i) cout << "." << T[i];
    //cout << endl;
    
    
    for (int i=n; i>0; --i){
        for ( int j=n; j>0; --j){
            if ( T[j] == i ) {
                T[j] = -1;
                break;
            } else if ( T[j] >= 0 ) moves++;
        }
    }

return moves;
}

int main(){
int t; scanf("%d", &t);
for(int i=1; i<=t; ++i) printf("Case #%d: %d\n", i, testcase());
return 0;
}

