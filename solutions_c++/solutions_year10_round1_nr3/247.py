#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <sstream>
#include <fstream>
#include <set>
#include <map>

using namespace std;

#define FR(i, n) for (int i=0; i<n; i++)
#define FOR(i, a, b) for (int i=a; i<=b; i++)

#define MAXN 100000

typedef long long LL;
typedef pair<int,int> II;

int n;
LL ret;
int a1,a2,b1,b2;
int f[1100100];

inline int tmin(int x, int y) {
       if (x<y) return x;
       return y;
}

inline int tmax(int x, int y) {
       if (x>y) return x;
       return y;
}

int go(int a, int b) {
    if (a<b) return go(b, a);
    if (a==b) return 0;
    // a > b
    if (a%b==0) {
      return 1;
    }
    int k=a/b;
    int tmp=go(b,a-k*b);    
    if (tmp==1 && k==1) return 0;
    else return 1;
}

int find(int u) {
    int L = 1, R = u;
    int res=0;
    while (L<=R) {
          int mid = (L+R)/2;
          if (go(u,mid)) {
            res=mid;
            L = mid+1;
          } else
          R=mid-1;
    }    
    return res;
}

void init() {
     ret = 0;
     f[1]=0;
     f[2]=1;
     f[3]=1;
     int aa=0;
     FOR(i,4,1000000) {
       f[i] = find(i);      
       //cout << f[i] << endl; 
     }
}

void process() {
     ret=0;
     FOR(a,a1,a2) {
       int x = f[a];
       //b1->b2
       //1->x       
       int u=tmax(b1,1);
       int v=tmin(b2,x);
       if (v>=u) ret += (v-u+1);
     }
     
     FOR(b,b1,b2) {
       int x = f[b];
       //b1->b2
       //1->x       
       int u=tmax(a1,1);
       int v=tmin(a2,x);
       if (v>=u) ret += (v-u+1);
     }
}

int main() {
    freopen("Cx.in", "rt", stdin);
    freopen("Cx.out", "wt", stdout);
    
    int ntest;
    cin >> ntest;
    
    string temp, st;
    getline(cin, temp);  
    init();
    FR(u, ntest) {      
          cout << "Case #" << u+1<<": ";                      
          cin >> a1 >> a2 >> b1 >> b2;          
          process();          
          cout << ret <<endl;
    }    
    
    return 0;
}

