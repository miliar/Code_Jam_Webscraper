#include <iostream>
#include <cmath>
#include <stack>
#include <set>
using namespace std;
#define MAX 60

int r, c;
char b[MAX][MAX];

int init() {
    for(int i = 0; i < MAX; ++i) {
        for(int j = 0; j < MAX; ++j) {
            b[i][j] = 0;
        }
    }
}

int main() {
    int test;
    cin >> test;
    
    for(int task = 1; task <= test; ++task) {
        cin >> r >> c;
        
        int result = 0;
        for(int i = 0; i < r; ++i) {
            for(int j = 0; j < c; ++j) {
                cin >> b[i][j];
            }
        }
        
        int rc = 0, cc = 0;
        
        for(int i = 0; i < r; ++i) {
            for(int j = 0; j < c; ++j) {
                if(b[i][j] == '#') {
                    if((cc == 0 && rc == 0) || (cc == 1 && rc == 1)) {
                        b[i][j] = '/';
                    }
                    else {
                        b[i][j] = '\\';
                    }
                    
                    if(rc) {
                        if(b[i][j-1] != '#') {
                            break;
                        }
                    }
                    rc = 1-rc;
                    
                    if(cc) {
                        if(b[i-1][j] != '#') {
                            break;
                        }
                    }
                    cc = 1-cc;
                }
                
                cout << "XXX" << rc << " " << cc << endl;
            } 
            if(rc != 0 || cc != 0) {
                result = -1;
                break;
            }    
            
        }
        
        if(result < 0) {
            cout << "Case #" << task << ":\n";
            cout << "Impossible" << endl;
        }
        else {
            cout << "Case #" << task << ":\n";
            for(int i = 0; i < r; ++i) {
                for(int j = 0; j < c; ++j) {
                    cout << b[i][j];
                }
                cout << endl;   
            }
        }
    }
}
