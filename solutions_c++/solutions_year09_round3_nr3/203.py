#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int F[200];
int P,Q,tmp;
int TAB[500][500];
int MASKA[11000];
long long function(int a, int b){
  if(a>=b)
    return 0;
  if(TAB[ MASKA[a] ][ MASKA[b] ]>=0)
    return TAB[ MASKA[a] ][ MASKA[b] ];
  //printf("przedzial od %d do %d\n", a, b);
  long long min=2000000000;
  for(int i=0; i<Q; i++){
    if(F[i]>=a && F[i]<=b){
      long long tmp=0;
      tmp+=F[i]-a;//lewy przedzial koszt
      tmp+=b-F[i];//prawy przedzial koszt
      tmp+=function(a, F[i]-1);
      tmp+=function(F[i]+1, b);
      //printf("%lld", tmp);
      if(tmp<min){
	min=tmp;
      }
    }
  }
  if(min!=2000000000){
    TAB[ MASKA[a] ][ MASKA[b] ]=min;
    return min;
  }else{
    TAB[ MASKA[a] ][ MASKA[b] ]=0;
    return 0;
  }
}
int main(){
  int T;
  scanf("%d", &T);
  for(int i=1; i<=T; i++){
    scanf("%d%d", &P, &Q);
    for(int j=0; j<Q; j++){
      scanf("%d", &tmp);
      F[j]=tmp;
    }
    for(int a=0; a<500; a++)
      for(int b=0; b<500; b++)
	TAB[a][b]=-1;
    for(int a=0; a<11000; a++)
      MASKA[a]=0;
    MASKA[1]=1;
    int r=2;
    for(int j=0; j<Q; j++){
      MASKA[ F[j]-1 ]=r++;
      MASKA[ F[j] ]=r++;
      MASKA[ F[j]+1 ]=r++;
    }
    MASKA[P]=r++;
    long long wynik;
    wynik=function(1, P);
    printf("Case #%d: %lld\n", i, wynik);
  }
  return 0;
}
