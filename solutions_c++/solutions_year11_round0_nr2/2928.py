#define MAXC 37
#define MAXD 29
#define MAXN 101

#include<stdio.h>

char combine1[2*MAXC],combine2[2*MAXC],combineto[2*MAXC],opposed1[2*MAXD],opposed2[2*MAXD],string[MAXN];
int instring[26];


int length;

bool combined(char c1, char c2, int C){
  for (int i=0; i<2*C; i++){
    if ((combine1[i] == c1) && (combine2[i] == c2)){
      instring[string[length-1]-'A']--;
      string[length-1] = combineto[i];
      return true;
    }
  }  
  return false;
}

bool opposed(char cnew, char c2,int D){
  for (int i=0; i<2*D; i++){
    if ((opposed1[i] == cnew) && (instring[opposed2[i]-'A'] > 0)){
      length = 0;
      for (int j=0; j<26; j++) instring[j] = 0;
      return true;
    }
  }
  return false;
}

int main(){
  int T;
  scanf("%d\n",&T);
  for (int tt=0; tt<T; tt++){
    int C,D,N;
    scanf("%d ",&C);
    for (int i=0; i<2*C; i+=2){
      scanf("%c%c%c ",&combine1[i],&combine2[i],&combineto[i]);
      combine1[i+1] = combine2[i];
      combine2[i+1] = combine1[i];
      combineto[i+1] = combineto[i];
    }
    scanf("%d ",&D);
    for (int i=0; i<2*D; i+=2){
      scanf("%c%c ",&opposed1[i],&opposed2[i]);
      opposed1[i+1] = opposed2[i];
      opposed2[i+1] = opposed1[i];
    }
    for (int j=0; j<26; j++) instring[j] = 0;
    scanf("%d ",&N);
    length = 0;
    char cc;
    for (int i=0; i<N; i++){
      scanf("%c",&cc);
      if (!combined(cc,string[length-1],C)){
        if (!opposed(cc,string[length-1],D)){
          string[length] = cc;
          length++;
          instring[cc-'A']++;
        }
      }
    }
    printf("Case #%d: [",tt+1);
    for (int i=0; i<length-1; i++){
      printf("%c, ",string[i]);
    }
    printf("%c]\n",string[length-1]);    
  }
  return 0;
} 
