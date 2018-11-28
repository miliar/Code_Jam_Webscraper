#include<stdio.h>
#include<string.h>
#include <ctype.h>
#define tL 20
#define tD 5123
#define tN 512
#define tAlfab 30

int mascaraDeUmGrupo(char pat[],int *pos){
  int res=0;
  (*pos) ++;
  while(pat[*pos] != ')'){
    res += 1<< (pat[*pos]-'a');
    (*pos) ++;
  }
  return res;
}

void toMask(int mask[],char pat[],int L){
  for(int i=0;i<L;i++) mask[i] = 0;
  int pos,ind;
  pos=ind=0;
  while(pat[pos] != '\0'){
    if(islower(pat[pos])){
      mask[ind++] = 1 << (pat[pos]-'a');
    }else if (pat[pos] == '('){
      mask[ind++] = mascaraDeUmGrupo(pat,&pos);
    }
    pos++;
  }
}
int match(int v1[],int v2[],int D){
  for(int i=0;i<D;i++){
    if ((v1[i] & v2[i]) == 0){
      return 0;
    }
  }
  return 1;
}
int main(){
  int L,D,N;
  char alienWords[tD][tL];
  int alienMask[tD][tL];
  char pattern[(tAlfab+2)*tL+123];
  scanf(" %d %d %d ",&L,&D,&N);
  for(int lin=0;lin<D;lin++){
    scanf(" %s ",alienWords[lin]);
    toMask(alienMask[lin],alienWords[lin],L);
  }
  for(int cas=1;cas<=N;cas++){
    int sol=0;
    int mask[tL];
    scanf(" %s ",pattern);
    toMask(mask,pattern,L);
    for(int i=0;i<D;i++){
      if(match(mask,alienMask[i],L)){
	sol++;
      }
    }
    printf("Case #%d: %d\n",cas,sol);
  }
  return 0;
}
