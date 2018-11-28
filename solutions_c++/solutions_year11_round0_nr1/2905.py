#include <iostream>
#include <algorithm>

#define MAX 101
#define FOR(i,j) for (int i=0; i<n; i++)

using namespace std;

int n;
char s_col[MAX];
int s_but[MAX];

int main(){
    int T;
    cin >> T;
    
    for (int t=1; t <=T; t++){
        cin >> n;
        FOR(i,n){
            cin >> s_col[i] >> s_but[i];
        }
        
        int sol = 0;
        int last_B, last_O;
        int pos_B, pos_O;
        
        last_B = last_O = 0;
        pos_B = pos_O = 1;
        
        FOR(i,n){
            if ( s_col[i] == 'B' ){
                if ( sol - last_B < abs(pos_B - s_but[i]) ){
                    sol += abs(pos_B - s_but[i]) - (sol - last_B);
                }
                pos_B = s_but[i];
            } else {
                if ( sol - last_O < abs(pos_O - s_but[i]) ){
                    sol += abs(pos_O - s_but[i]) - (sol - last_O);
                }
                pos_O = s_but[i];
            }
            sol++;
            
            if ( s_col[i] == 'B' ){
                last_B = sol;
            } else {
                last_O = sol;
            }
        }
        
        cout << "Case #" << t << ": " << sol << endl;
    }
    
    return 0;
}