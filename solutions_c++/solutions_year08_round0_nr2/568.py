#include "iostream"
#include "algorithm"
#include "fstream"
#include "sstream"

#define tmax(a, b) (((a)>(b))?(a):(b))
#define tmin(a, b) (((a)<(b))?(a):(b))
#define FR(i, n) for (int i=0; i<n; i++)
#define FOR(i, a, b) for (int i=a; i<=b; i++)

using namespace std;

int test, ntest, re1, re2, res;
int na, nb, tat, n;

int be[222], en[222];
int tho[222], viec[222], hd[222], truoc[222];
int dau, cuoi;

bool noi(int i, int j) {
    if (i <= na && j <= na) return false;
    if (i > na && j > na) return false;
    return en[i] + tat <= be[j];    
} 

void tangcap(int j) {
     int i, jnext;
     while (j > 0) {
       i = truoc[j];
       jnext = tho[i];
       tho[i] = j;
       viec[j] = i;
       j = jnext;
     }
     res--;
}

void BFS(int iroot) {
     dau = 0, cuoi = 1;
     hd[1] = iroot;
     memset(truoc, 0, sizeof(truoc));
     while (dau != cuoi) {
       int i = hd[++dau];
       FOR(j, 1, n)
         if (truoc[j]==0 && noi(i,j)) {
           truoc[j] = i;
           if (viec[j]==0) {
             tangcap(j);
             return;
           }
           hd[++cuoi] = viec[j];           
         }       
     }
}

void process() {
     cin >> tat;
     cin >> na >> nb;
     n = res = na + nb;
     FOR(i, 1, n) {
       int h1, m1, h2, m2;
       scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
       be[i] = h1 * 60 + m1;
       en[i] = h2 * 60 + m2;
     }          
     
     memset(tho, 0, sizeof(tho));
     memset(viec, 0, sizeof(viec));
     FOR(i, 1, n) BFS(i);     
     re1 = 0;
     FOR(i, 1, na)        
       if (viec[i]==0) re1++;     
}

int main() {
    freopen("bl.in",  "rt", stdin);
    freopen("bl.out", "wt", stdout);
    
    cin >> ntest;
    FOR(test, 1, ntest) {
      process();
      printf("Case #%d: %d %d\n", test, re1, res - re1);
    }    
    
    return 0;
}
