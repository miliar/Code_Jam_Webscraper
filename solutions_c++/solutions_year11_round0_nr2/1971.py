#include <iostream>
#include <map>
#include <set>
using namespace std;
#define MAX 256

char  s[MAX];
int opp[MAX][MAX], inv[MAX][MAX];
int init() {
    for(int i = 0; i < MAX; ++i) {
        s[i] = -1;
        for(int j = 0; j < MAX; ++j) {
            opp[i][j] = -1;
            inv[i][j] = -1;
        }
    }
}

int main() {
    int test;
    cin >> test;
    
    for(int cases = 1; cases <= test; ++cases) {
        int N, D, C;
        init();
        cin >> C;
        char a, b, c;
        for(int i = 0; i < C; ++i) {
            cin >> a >> b >> c;
            inv[a][b] = int(c);
            inv[b][a] = int(c);
            //cout << inv[a][b] << endl;
            //cout << a << b << c << endl;
        }
        
        cin >> D;
        for(int i = 0; i < D; ++i) {
            cin >> a >> b;
            opp[a][b] = 1;
            opp[b][a] = 1;
        }
        
        cin >> N;
        for(int i = 0; i < N; ++i) {
            cin >> a;
            s[i] = a;
        }
        
        int lastValid = 0;
        for(int i = 1; i < N; ++i) {
            //cout << i << " " << s[i] << " " << s[lastValid] << endl;
            //cout << "inv " << inv[s[i]][s[lastValid]] << " " << inv['Q']['F'] << " " << (s[i]-'Q' + s[lastValid] -'F' ) << endl;
            if(s[lastValid] > 0 && inv[s[i]][s[lastValid]] > 0) {
                //cout << "Hello " << s[i] << " " << s[lastValid] << endl;
                s[i] = char(inv[s[i]][s[lastValid]]);
                s[i-1] = -1;
                lastValid = i;
            
            }
            else {
                int temp = lastValid;
                for(int j = lastValid; j >= 0; --j) {
                    if(s[i] > 0 && s[j] > 0 && opp[s[i]][s[j]] > 0) {
                        for(int k = 0; k <= i; ++k) {
                            s[k] = -1;
                        }
                        
                        lastValid = -1;
                        break;
                    }
                }
                
                if(lastValid == temp) {
                    lastValid = i;
                }
            }
            //cout << "Valid " << lastValid << endl;
            
        }
        
        cout << "Case #" << cases << ": [";
        char temp[MAX];
        int count = 0;
        for(int i = 0; i < N; ++i) {
            if(s[i] >= 0) {
                temp[count++] = s[i];
            }
        }
        
        for(int i = 0; i < count-1; ++i) {
            cout << temp[i] << ", ";
        }
        if(count > 0) {
            cout << temp[count-1];
        }
        cout << "]" << endl;;
    }
}
