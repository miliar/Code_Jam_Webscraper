#include <iostream>

#define MAX 20

using namespace std;

int seq[MAX];
int c[MAX];
int n;
int sol;

int suma(int a, int b){
    int s = 0;
    for (int i=0; i<15; i++){
        if ( (a & (1 << i)) != (b & (1 << i)) ){
            s |= (1 << i);
        }
    }
    return s;
}

void f(int i){
    if ( i == n ){
        
        int s0 = 0;
        int ss0 = 0;
        for (int k=0; k<n; k++){
            if ( seq[k] == 0 ){
                s0 = suma(s0, c[k]);
                ss0 += c[k];
            }
        }
        
        int s1 = 0;
        int ss1 = 0;
        for (int k=0; k<n; k++){
            if ( seq[k] == 1 ){
                s1 = suma(s1, c[k]);
                ss1 += c[k];
            }
        }
        if ( ss0 == 0 || ss1 == 0 ){
            return;
        }
        
        if ( s0 == s1){
            sol = max(sol, max(ss0, ss1));
        }
        
    } else {
        seq[i] = 0;
        f(i+1);
        seq[i] = 1;
        f(i+1);
    }
}

int main(){
    int T;
    cin >> T;
    for (int t=1; t<=T; t++){
        cin >> n;
        for (int i=0; i<n; i++){
            cin >> c[i];
        }
        sol = -1;
        f(0);
        cout << "Case #" << t << ": ";
        if ( sol == -1 ){
            cout << "NO" << endl;
        } else {
            cout << sol << endl;
        }
    }
    return 0;
}