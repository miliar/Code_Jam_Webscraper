#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>
#include <iostream>

using namespace std;

#define TAM 1024

int tempo[TAM];

int gcd(int a,int b){
  if(b == 0) return a;
  else return gcd(b,a%b);
}

int main(){
  int nt;
  scanf("%d",&nt);
  for(int t = 1 ; t <= nt; t++){
    int n;

    scanf("%d",&n);
    for(int i = 0;i < n;i++) scanf("%d",&tempo[i]);

    sort(tempo,tempo+n);
    
    int T = tempo[1] - tempo[0];
    
    for(int j = 1;j < n;j++) T = gcd(T,tempo[j] - tempo[0]);

    int k = 0;
    while(T*k - tempo[0] < 0) k++;
    printf("Case #%d: %d\n",t,T*k - tempo[0]);

  }
  return 0;
}
