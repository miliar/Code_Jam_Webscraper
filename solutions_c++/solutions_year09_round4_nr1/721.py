#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <sstream>
#include <fstream>
#include <set>

using namespace std;

#define FR(i, n) for (int i=0; i<n; i++)
#define FOR(i, a, b) for (int i=a; i<=b; i++)

#define MAXN 100000

typedef long long LL;

int n, ret;
int a[50];

void process() {
     ret = 0;
     FR(i, n) 
     if (a[i]>i)
     {
           int k = 0;
           FOR(j, i+1, n-1)
             if (a[j]<=i) {
               k = j; break;
             }
           
           
           for (int j=k-1;j>=i; j--) {
                 swap(a[j], a[j+1]);
                 ret++;
           }
     }
     
     
}

int main() {
    freopen("a.in", "rt", stdin);
    freopen("a.out", "wt", stdout);
    

    
    
    int ntest;
    cin >> ntest;
    
    string temp, st;
    getline(cin, temp);    
    FR(u, ntest) {      
          cout << "Case #" << u+1<<": ";  
          cin >> n;  getline(cin, temp);
          
          //FR(i, n) cout << i << " "; cout << endl;
          FR(i, n) {
                getline(cin, st);
                a[i] = -1;
                FR(u, st.length())
                  if (st[u]=='1') a[i] = u;
                
                //cout << a[i] << " ";
          }
          //cout << endl;
          
          
          process();
          
          cout << ret <<endl;
    }    
    
    return 0;
}

