#include <cstdio>
#include <vector>
#include <algorithm>
#define MaxN 10000

using namespace std;

int nrT, N, M, n, sol;
vector<int> vec[MaxN];
int leg[2*MaxN], c[2*MaxN], t[2*MaxN];
char ok[2*MaxN];
char a[200][200];

bool firstP(int k){
     return ((k%M)%2) == 0;
}

void leaga(int v){
     for (unsigned i=0; i<vec[v].size(); i++)
         if (leg[vec[v][i]] < 0){
            leg[v] = vec[v][i];
            leg[vec[v][i]] = v;
            sol++;
            return;
         }
}

void urca(int v){
     int k=t[v];
     while (t[k]>=0) k=t[t[k]];
     if (leg[k]>0) return;
     sol++; k=v;
     while (k>=0){
           leg[k]=t[k];
           leg[t[k]]=k;
           k=t[t[k]];
     }
}

int  augment(){
     unsigned i, j=0, nr=0; 
     memset(ok, 0, n);
     for (i=0; (int)i<n; i++)
         if (firstP(i))
            if (leg[i]<0) c[nr++]=i, ok[i]=1, t[i]=-1;
     int old=sol;
     while (j<nr){
           int k=c[j++];
           if (firstP(k))
              for (i=0; i<vec[k].size(); i++){
                  int V=vec[k][i];
                  if (V==leg[k]) continue;
                  if (!ok[V])
                     ok[V]=1, c[nr++]=V, t[V]=k;
              }
           if (!firstP(k) && !ok[leg[k]])
              ok[leg[k]]=1, c[nr++]=leg[k], t[leg[k]]=k;
     }
     for (i=0; i<nr; i++)
         if (!firstP(c[i]) && leg[c[i]]<0) urca(c[i]);
     return (old<sol);
}   

bool broken(int x, int y){
     if (x<0 || x>=N || y<0 || y>=M) return true;
     return (a[x][y]=='x');
}

void link(int x, int y){
     if (broken(x, y)) return;
     int V = x*M+y;
     if (!broken(x, y-1)) vec[V].push_back(V-1);
     if (!broken(x, y+1)) vec[V].push_back(V+1);
     if (!broken(x-1, y-1)) vec[V].push_back(V-M-1);
     if (!broken(x-1, y+1)) vec[V].push_back(V-M+1);
     if (!broken(x+1, y-1)) vec[V].push_back(V+M-1);
     if (!broken(x+1, y+1)) vec[V].push_back(V+M+1);     
}

void solve(){   
     sol = 0;
     for (int i=0; i<n; i++)
         vec[i].resize(0);
     scanf("%d %d\n", &N, &M);
     n = N*M;
     for (int i=0; i<N; i++)
         scanf("%s\n", a[i]);
     for (int i=0; i<N; i++)
         for (int j=0; j<M; j+=2)
             link(i, j);
     memset(leg, -1, sizeof(leg));
     sol=0;
     for (int i=0; i<N; i++)
         for (int j=0; j<M; j+=2)
             leaga(i*M+j);
     while (augment());
     sol = -sol;
     for (int i=0; i<N; i++)
         for (int j=0; j<M; j++)
             if (a[i][j] == '.') sol++;    
     nrT++;    
     printf("Case #%d: ", nrT);
     printf("%d\n", sol);
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
