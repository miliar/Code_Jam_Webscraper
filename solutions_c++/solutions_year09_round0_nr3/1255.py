#include <cstdio>
using namespace std;
char Line[1000];
int Well[30];
// W  E  L  C  O  M  E  _  T  O  _  C  O  D  E  _  J  A  M  *
// 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
inline void f(int n){
  Well[n]+=Well[n+1];
  Well[n]%=10000;
  return;
}
int main(){
  int n;
  scanf("%d", &n);
  getchar();
  for(int i=0; i<n; i++){
    for(int j=0; j<1000; j++)
      Line[j]=0;
    int t = getchar();
    int j = 0;
    while(t!=10){
      Line[j]=t;
      t=getchar();
      j++;
    }
    for(int j=0; j<30; j++)
      Well[j]=0;
    Well[19]=1;
    for(int j=999; j>=0; j--){
      if(Line[j]=='w'){ f(0); }
      else if(Line[j]=='e'){ f(1); f(6); f(14); } 
      else if(Line[j]=='l'){ f(2); }
      else if(Line[j]=='c'){ f(3); f(11); }
      else if(Line[j]=='o'){ f(4); f(9); f(12); }
      else if(Line[j]=='m'){ f(5); f(18); }
      else if(Line[j]==' '){ f(7); f(10); f(15); }
      else if(Line[j]=='t'){ f(8); }
      else if(Line[j]=='d'){ f(13); }
      else if(Line[j]=='j'){ f(16); }
      else if(Line[j]=='a'){ f(17); }
    }
    Well[0]%=10000;
    printf("Case #%d: ", i+1);
    if(Well[0]==0)
      printf("0000\n");
    else if(Well[0]<10)
      printf("000%d\n", Well[0]);
    else if(Well[0]<100)
      printf("00%d\n", Well[0]);
    else if(Well[0]<1000)
      printf("0%d\n", Well[0]);
    else
      printf("%d\n", Well[0]);
  }
  return 0;
}
