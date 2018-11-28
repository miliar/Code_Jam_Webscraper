#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-8; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-8; }

int maxc, cli[1000], adj[500][500];

int clique(int vec[], int s, int size) {
  if (! s) {
    if (size > maxc) {
      maxc = size;
      return 1;
    }   
    return 0;
  }
  while (s) {
    if (size + s <= maxc) return 0;
    int i = vec[s - 1]; 
    if (size + cli[i] <= maxc)  return 0;
    s--;
    int tmp[50], k = 0;
    for (int j = 0; j < s; j++)
      if (adj[i][vec[j]]) tmp[k++] = vec[j];
    if (clique(tmp, k, size + 1)) return 1;
  }
}

bool f(int a,int b,int c,int d){
  if (a==c)return false;
  if (b==d)return false;
  if (a>c && b<d)return false;
  if (a<c && b>d)return false;
  return true;
}

int main(){
  int tt; scanf("%d",&tt);
  for (int ti=1;ti<=tt;ti++){
    int n,K;
    scanf("%d%d",&n,&K);
    int a[n][K];
    int label[n];
    for (int i=0;i<n;i++){
      for (int j=0;j<K;j++){
        scanf("%d",&a[i][j]);
      }
    }

    for (int i=0;i<n;i++){
      for (int j=i+1;j<n;j++){
        bool valid=true;
        for (int k=0;k<K-1 &&valid;k++){
          valid = f(a[i][k],a[i][k+1],a[j][k],a[j][k+1]);
        }
        adj[i][j] = adj[j][i] = !valid;
      }
    }
  
    /*
    for (int i=0;i<n;i++){
      for (int j=0;j<n;j++)printf("%d ",adj[i][j]); puts("");
    }
    */

    /* main */
    maxc = 0;
    for (int i = n - 1; i >= 0; i--) {
      int vec[1000], s = 0;
      for (int j = n - 1; j >= i; j--)
        if (adj[i][j])  vec[s++] = j;
      clique(vec, s, 1); 
      cli[i] = maxc;
    }
    printf("Case #%d: %d\n", ti, cli[0]);

    //printf("Case #%d: %d\n",ti,ln);
  }

  return 0;
}
