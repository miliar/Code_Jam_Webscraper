#include <iostream>
#include <algorithm>
#include <vector>

#define FR(i, n) for (int i=0; i<(n); i++)

using namespace std;

int ntest, res;
int c, d, n;
int tr[99][99], op[99][99];
int a[1111];

void process() {
     memset(tr, 0xff, sizeof(tr));
     memset(op, 0, sizeof(op));
     cin >> c;
     string st;
     FR(i, c) {
           cin >> st;
           tr[st[0]-'A'][st[1]-'A'] = tr[st[1]-'A'][st[0]-'A'] = st[2]-'A';           
     }
     cin >> d;
     FR(i, d) {           
           cin >> st;
           op[st[0]-'A'][st[1]-'A'] = op[st[1]-'A'][st[0]-'A'] = 1;           
     }
     int k = 0;
     cin >> n >> st;
     FR(i, n) {
           //st[i]
           int x = st[i]-'A';
           a[k++] = x;
           while (k>=2 && tr[a[k-2]][a[k-1]]>=0) {
                 a[k-2] = tr[a[k-2]][a[k-1]];
                 k--;
           }         
           FR(j, k-1)
                 if (op[a[j]][a[k-1]]) {
                    k = 0;
                    break;
                 }
     }
     
     cout << "[";
     FR(i, k) {
       printf("%c", (a[i]+'A'));
       if (i!=k-1) printf(", ");
     }
     cout << "]" << endl;
}

int main() {
    
    freopen("B-large.in", "rt", stdin);
    freopen("b.out", "wt", stdout);
    
    cin >> ntest;
    for (int i=1; i<=ntest; i++) {
        printf("Case #%ld: ", i);
        process();        
    }    
    
    return 0;
}
