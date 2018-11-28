#include <cstdio>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)


#define MAX 55


char picture[MAX][MAX];

int main(){
  int T,t,R,C,i,j;
  scanf("%d\n",&T);
  REP(t,T){
    scanf("%d %d\n",&R,&C);
    REP(i,R){
      REP(j,C){
        scanf("%c",&picture[i][j]);
      }
      scanf("\n");
    }
    bool possible = true;
    REP(i,R-1){
      // fuer jede Zeile
      REP(j,C-1){
        if (picture[i][j] == '#'){
          if ((picture[i][j+1] == '#') && (picture[i+1][j] == '#') && (picture[i+1][j+1] == '#')){
            picture[i][j] = '/';
            picture[i+1][j+1] = '/';
            picture[i][j+1] = 92;
            picture[i+1][j] = 92;
          }else possible = false;
        }
      }
    }  
    REP(i,R){
      if (picture[i][C-1] == '#') possible = false;
    }
    REP(j,C){
      if (picture[R-1][j] == '#') possible = false;
    }
    printf("Case #%d:\n",t+1);
    if (possible){
      REP(i,R){
        REP(j,C){
          printf("%c",picture[i][j]);
        }
        printf("\n");
      }
    }else{
      printf("Impossible\n");
    }  
  }
  return 0;
}
 
