#include<vector>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<set>
#include<string.h>
#include<map>
#include<algorithm>
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<queue>
#include<stack>
#include<ctype.h>
#include<cmath>
#include<fstream>

using namespace std;

#define sz size()
#define st stringstream
#define len length()
#define f(i,p,n) for(int i=p;i<n;i++)
#define sort(v) sort(v.begin(),v.end())
#define pb push_back

int main () {
    
    freopen("A-large.in","r",stdin);
    freopen("tiles.out","w",stdout);
    
    int t, r, c;
    char a[50][50], ch;
    cin >> t;
    f(k,0,t) {
             
        cin >> r >> c;
        f(i,0,r) {
            f(j,0,c) {
                
                cin >> ch;
                a[i][j] = ch;
            }
        }
        
        f(i,0,r) {
            f(j,0,c) {
                
                if (a[i][j] == '.') continue;
                if (a[i][j] == '#') {
                    
                    if (j+1 < c && a[i][j+1] == '#' && i+1 < r && a[i+1][j] == '#' && a[i+1][j+1] == '#') {
                            
                        a[i][j] = a[i+1][j+1] = '/';
                        a[i+1][j] = a[i][j+1] = '\\';
                    }
                }
            }
        }
        bool boo = true;
        f(i,0,r) {
            f(j,0,c) {
                
                if (a[i][j] == '#') {
                
                    boo = false;
                    break;
                }
            }    
            if (!boo) break;
        }    
        
        cout << "Case #" << k+1 << ":" << endl;
        if (!boo) cout << "Impossible" << endl;
        else {
             f(i,0,r) {
                 f(j,0,c) {
                     
                     cout << a[i][j];
                 }
                 cout << endl;
             }
        }
    }
    return 0;
    system("pause");
}                 
