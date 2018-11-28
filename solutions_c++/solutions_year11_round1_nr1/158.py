#include <iostream>
#include <algorithm>
#include <vector>

#define FR(i, n) for (int i=0; i<(n); i++)
#define FOR(i, a, b) for (int i=(a); i<=(b); i++)

using namespace std;

int ntest;
int res;
long long n, p1, p2;
int a[111];

void process() {
     cin >> n >> p1 >> p2;
     res = 0;
     if ((p1<100 && p2==100) || (p1>0 && p2==0)) {
        res = 0;
        return;
     }
     memset(a, 0, sizeof(a));
     int x = 0;
     int cnt = 0;
     while (1) {
           cnt++;
           if (cnt>n) return;
           x = (x + p1) % 100;
           if (x==0) { res=1; return; }
           if (a[x]>0) return;
           a[x]=1;
     }
}

int main() {
    
    freopen("A-large.in", "rt", stdin);
    freopen("a.out", "wt", stdout);
    
    cin >> ntest;
    for (int i=1; i<=ntest; i++) {
        process();           
        printf("Case #%ld: ", i);
        if (res>0) printf("Possible\n");
        else  printf("Broken\n");
    }    
    
    return 0;
}
