#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#define FOR(i,a,b) for(int i = a ; i < b ; i++)

#define FORI(i,b,a) for(int i = b - 1 ; i >= a ; i--)

#define LL long long
#define ULL unsigned long long
#define UI unsigned int

#define VI vector<int>
#define VS vector<string>

#define pb push_back

int main() {
    int tc,T;
    int r,c;
    int arr[51][51];
    char a[51][51];
    
    cin>>tc;
    FOR(T,1,tc+1) {
        printf("Case #%d:\n",T);
        char ch;
        cin>>r>>c;
        FOR(i,0,r) {
            FOR(j,0,c) {
                cin>>ch;
                if(ch == '.') arr[i][j] = 0;
                if(ch == '#') arr[i][j] = -1;
                a[i][j] = ch;
            }
        }
        
        FOR(i,0,r-1) {
            FOR(j,0,c-1) {
                if(arr[i][j] == -1 && arr[i+1][j] == -1 && arr[i][j+1] == -1 && arr[i+1][j+1] == -1) {
                    arr[i][j] = arr[i+1][j] = arr[i][j+1] = arr[i+1][j+1] = 1;
                }
            }
        }
        
        bool b = false;
        
        FOR(i,0,r) {
            FOR(j,0,c) {
                if(arr[i][j] == -1) {
                    cout << "Impossible" << endl;
                    b = true;
                    break;
                }
            }
            if(b) break;
        }
        
        FOR(i,0,r-1) {
            FOR(j,0,c-1) {
                if(arr[i][j] == 1 && arr[i+1][j] == 1 && arr[i][j+1] == 1 && arr[i+1][j+1] == 1) {
                    arr[i][j] = arr[i+1][j] = arr[i][j+1] = arr[i+1][j+1] = 0;
                    a[i][j] = a[i+1][j+1] = '/';
                    a[i+1][j] = a[i][j+1] = '\\';
                }
            }
        }
        
        if(b) continue;
        else {
             FOR(i,0,r) {
                 FOR(j,0,c) {
                     cout << a[i][j];
                 }
                 cout << endl;
             }
        }
        
    }
    return (0);
}
