#include <cstdio>
#include <algorithm>
#include <bitset>
#define MaxN 2000000
#define buc 1024
#define bucket(i) ((i)/buc)

using namespace std;

int nrt;
int n, nr, poz[500];
int full[MaxN/buc], first[MaxN/buc];
bool isFree[MaxN];
int a[MaxN], next[MaxN], prev[MaxN];

int bucketSize(int b){
    return buc - full[b];
}

int advance(int poz, int K){
    if (K==0) return poz;
/*    
    int b = bucket(poz);
    if (poz + buc < n && poz == first[b] &&  K >= bucketSize(b))
       return advance(first[b+1], K-bucketSize(b));
//*/
    return advance(next[poz], K-1);
}

void mark(int poz, int val){
     isFree[poz] = false;
     full[bucket(poz)]++;
     a[poz] = val;
     int Next = next[poz];
     int Prev = prev[poz];
     if (poz == first[bucket(poz)]){
        int b = bucket(poz);
        first[b] = Next;
     }
     next[Prev] = Next;
     prev[Next] = Prev;
}

void solve(){
     scanf("%d %d", &n, &nr);
     for (int i=0; i<nr; i++)
         scanf("%d", poz+i), poz[i]--;
     memset(full, 0, sizeof(full));
     memset(a, 0, sizeof(a));
     memset(isFree, true, sizeof(isFree));
     for (int i=0; i<n; i++){
         next[i] = (i+1)%n;
         prev[i] = (n+i-1)%n;
     }
     int Poz = 1;
     for (int i=0; i<=n/buc; i++)
         first[i] = buc*i;
     int remain = n;
     mark(0, 1);     
     for (int i=2; i<=n; i++){
         remain--;              
         Poz = advance(Poz, i-1);
         mark(Poz, i);
         Poz = next[Poz];
     }
     nrt++;
     printf("Case #%d: ", nrt);
     for (int i=0; i<nr; i++)
         printf("%d ", a[poz[i]]);
     printf("\n");
     
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.out", "w",stdout);
    int tst;
    scanf("%d", &tst);
    while (tst--)
          solve();
    return 0;
}
