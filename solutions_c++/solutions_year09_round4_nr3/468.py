#include <iostream>
#include <string>
#include <set>
using namespace std;

int n, m;
int b[110][30];
int c[110][110];
set<int> a[2];

int lessx(int x, int y) {
    for (int i = 0; i < m; ++i) {
        if (b[x][i]< b[y][i]) return 1;
        if (b[x][i]> b[y][i]) return 0;
        }
        return 0;
}
int lessxxx(int x, int y) {
    for (int i = 0; i < m; ++i) {
        if (b[x][i]>= b[y][i]) return 0;
        }
        return 1;
}
void done() {
     for (int i = 0; i < n; ++i) {
         for (int j = i + 1; j< n; ++j) {
             if (lessx(j, i)) {
                 int tt;
                 for (int k = 0;k < m;++k) tt=b[i][k],b[i][k]=b[j][k],b[j][k]=tt;
             }
         }
     }
     memset(c, 0, sizeof(c));
     for (int i = 0; i < n; ++i) {
         for (int j = 0; j < n; ++j) {
             if (lessxxx(i,j)) c[i][j] = 1;
         }
     }
     /*
     for (int i = 0; i < n; ++i) {
         for (int j = 0; j < n; ++j) {
             cout << c[i][j]<< " ";
         }cout << endl;
     }*/
     a[0].clear();
     a[0].insert(1);
     int ap = 0;
     for (int i = 1; i< n; ++i) {
    //     for (set<int>::iterator it = a[ap].begin(); it != a[ap].end(); ++it) {   cout << *it << " ";} cout << endl;
         
         a[1-ap].clear();
         for (set<int>::iterator it = a[ap].begin(); it != a[ap].end(); ++it) {
             int x = *it;
             for (int j = 0; j < i; ++j) {
                 if ((x & (1<<j)) && c[j][i]) {
                      int y = (x|(1<<i));
                      y = (y^(1<<j) );
                      a[1-ap].insert(y);
                 }
             }
             a[1-ap].insert(x|(1<<i));
         }
         ap = 1-ap;
     }
   //      for (set<int>::iterator it = a[ap].begin(); it != a[ap].end(); ++it) {   cout << *it << " ";} cout << endl;

     int ret = n;
     for (set<int>::iterator it = a[ap].begin(); it != a[ap].end(); ++it) {
         int x = *it;
         int r = 0;
         for (int i = 0; i < n; ++i) {
             if (x &(1<<i)) r++;
         }
             if(ret >r) ret = r;
     }
     cout << ret << endl;
}
int main() {
    int as;
    cin >> as;
    for (int kk=0; kk < as; ++kk) {
        cout << "Case #" << kk+1 << ": ";
        cin >> n>> m;
        for (int i = 0; i < n; ++i) for (int j = 0; j  < m; ++j) cin >> b[i][j];
        done();
    }
    return 0;
}
