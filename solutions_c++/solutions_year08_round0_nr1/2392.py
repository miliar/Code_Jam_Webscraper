#include <cstdio>
#include <string>
#define inf 99999999

using namespace std;

int n, m, nr;
int best[1100][200];
string name[1000], query[1000];

string getLine(){
       char lin[9999];
       fgets(lin, sizeof(lin), stdin);
       return lin;
}

void solve(){
     nr++;
     scanf("%d\n", &n);
     for (int i=0; i<n; i++)
         name[i] = getLine();
     scanf("%d\n", &m);
     for (int i=0; i<m; i++)
         query[i] = getLine();
     memset(best, 0x3f, sizeof(best));         
     for (int i=0; i<n; i++)
         if (name[i] != query[0])
            best[0][i] = 0;
     for (int i=1; i<m; i++){
         int sw = inf;
         for (int j=0; j<n; j++)
             if (best[i-1][j] < sw)
                sw = best[i-1][j];
         for (int j=0; j<n; j++)
             if (name[j] != query[i]){
                best[i][j] = best[i-1][j];
                if (sw+1 < best[i][j])
                   best[i][j] = sw+1;
             }
     }
     int min = inf;
     for (int i=0; i<n; i++)
         if (best[m-1][i] < min) min = best[m-1][i];
     if (m==0) min=0;
     printf("Case #%d: %d\n", nr, min);
}

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int tst;
    scanf("%d", &tst);
    while (tst--)
          solve();
}
