#include<iostream>
using namespace std;

const int N = 27;
const int M = 16;
const int K = 501;
bool tab[M][N];
char zb[10*K][M];
char wz[K];
int n,d,l;

main(){
  scanf("%d %d %d",&l,&d,&n);
  for(int i=0;i<d;i++)
    scanf("%s",zb[i]);
  for(int i=1;i<=n;i++){
    scanf("%s",wz);
    int poz = 0;
    int roz = strlen(wz);
    for(int k=0;k<l;k++) for(int j=0;j<N;j++) tab[k][j] = 0;
    int nr = 0;
    while(poz < roz){
      if(wz[poz] == '('){
        poz++;
        while(isalpha(wz[poz])){
          tab[nr][wz[poz] - 'a'] = 1;
          poz++;
        }
        poz++;
      }
      else
        tab[nr][wz[poz++]-'a'] = 1;
      nr++;
    }
    int ile= 0;
    for(int j=0;j<d;j++){
      bool ok = 1;
      for(int k=0;k<l;k++)
        if(!tab[k][zb[j][k] - 'a']) ok  =0;
      ile += ok;
    }
    printf("Case #%d: %d\n",i,ile);
  }
}
