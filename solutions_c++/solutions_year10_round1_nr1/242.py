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

int ret[3];
int n, k;
string a[111], b[111];
int c[111][111];

int dx[] = {0, 0, 1, -1, 1, 1, -1, -1};
int dy[] = {1, -1, 0, 0, -1, 1, -1, 1};

bool inside(int i, int j) {
     return (i>=0 && i<n && j>=0 && j<n); 
}

void check(int i, int j, int u, int v) {
    if (ret[v]>=k) return;
    int dem = 1;
    while (1) {
          int ii=i+dx[u];
          int jj=j+dy[u];
          if (!inside(ii,jj)) break;
          if (c[ii][jj]!=v) break;
          dem++;
          i=ii;j=jj;
    }
    ret[v]>?=dem;
}

void process() {
     ret[0]=ret[1]=ret[2]=0;
     FR(i, n) FR(j, n) {
           b[j][n-1-i] = a[i][j];
     }
     
     FR(i,n) FR(j,n) {
             c[i][j]=0;
             if (b[i][j]=='R') c[i][j]=1;
             if (b[i][j]=='B') c[i][j]=2;
     }
     //FR(i,n) { FR(j,n) cout << c[i][j]; cout << endl; } cout << endl;
     FR(j, n) {
           int x = n-1;
           for (int i=n-1; i>=0; i--) {
               if (c[i][j]!=0) {
                 int t = c[i][j];
                 c[i][j] = 0;
                 c[x][j] = t;
                 x--;
               }
           }
     }
     //FR(i,n) { FR(j,n) cout << c[i][j]; cout << endl; }
     
     FR(i,n) FR(j,n) if (c[i][j]>0) {
             FR(u,8) check(i,j,u,c[i][j]);
     }
}

int main() {
    freopen("Ax.in", "rt", stdin);
    freopen("Ax.out", "wt", stdout);
    

    
    
    int ntest;
    cin >> ntest;
    
    string temp, st;
    getline(cin, temp);    
    FR(u, ntest) {      
          cout << "Case #" << u+1<<": ";  
          
          cin >> n >> k;
          getline(cin, temp);
          
          FR(i, n) {
                cin >> a[i];
                b[i] = a[i];
                //cout << a[i]<<endl;
          }
          
          //cout << endl;

          
          
          process();
          
          //cout << ret[1] << " " << ret[2] << endl;
          
          if (ret[1]<k && ret[2]<k) cout << "Neither";
          else
          if (ret[1]>=k && ret[2]>=k) cout << "Both";
          else
          if (ret[1]>=k) cout << "Red";
          else cout << "Blue";
          cout << endl;
    }    
    
    return 0;
}

