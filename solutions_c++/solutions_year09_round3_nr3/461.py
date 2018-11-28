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

#define MAXT 1111000000

typedef long long LL;

int len, n;
int a[111];
int f[111][111];
int p[111], kill[111];

int left(int i) {
    if (i==0) return 0;
    return a[i-1];
}

int right(int i) {
    if (i==n-1) return len+1;
    return a[i+1];
}

int go(int i, int j) {
    int& ret = f[i][j];
    if (ret!=-1) return ret;
    if (i==j) {
      ret = right(j)-left(i)-2;
      return ret;
    }    
    
    int temp1 = right(j)-left(i)-2 + go(i+1, j);
    int temp2 = right(j)-left(i)-2 + go(i, j-1);
    
    ret = min(temp1, temp2);
    
    return ret;
}

void process() {
     sort(a, a+n);
     
     memset(f, 0xff, sizeof(f));     
     int ret = go(0, n-1);
     
     cout << ret << endl;
}




int run() {      
    int ret = 0;
    FR(u, n) {
          int i = p[u];
          
          int L = 0;
          for (int j=i-1; j>=0; j--)
            if (kill[j]) {
              L = a[j];
              break;
            }          
          
          int R = len+1;
          for (int j=i+1; j<n; j++)
            if (kill[j]) {
              R = a[j];
              break;
            }
          
          kill[i] = 1;
          ret += R - L - 2;
    }    
    
    return ret;
}

void process1() {
     sort(a, a+n);     
     FR(i, n) p[i] = i;     
     
     int ret = MAXT;     
     while (1) {
           memset(kill, 0, sizeof(kill));
           int temp = run();          
           ret = min(ret, temp);
           if (!next_permutation(p, p+n)) break;
     }
     cout << ret << endl;
}

int main() {
    freopen("c.in", "rt", stdin);
    freopen("c.out", "wt", stdout);
    
    int ntest;
    cin >> ntest;
    
    string temp;
    getline(cin, temp);    
    FR(u, ntest) {
          cin >> len >> n;
          FR(i, n) cin >> a[i];
          cout << "Case #" << u+1<<": ";
          process1();
    }    
    
    return 0;
}

