#include<cstdio>
int T,e,s,tt;
char b[10][10];
int checkrow(int row,char c1,char c2){
    for (int i=0; i<4; i++){
        if (b[row][i]!=c1&&b[row][i]!=c2) return 0;    
    }
    return 1;
}
int checkcol(int col,char c1,char c2){
    for (int i=0; i<4; i++){
        if (b[i][col]!=c1&&b[i][col]!=c2) return 0;
    }
    return 1;
}
int checkdiag1(char c1,char c2){
    for (int i=0; i<4; i++){
        if (b[i][i]!=c1&&b[i][i]!=c2) return 0;
    }
    return 1;
}
int checkdiag2(char c1,char c2){
    for (int i=0; i<4; i++){
        if (b[i][3-i]!=c1&&b[i][3-i]!=c2) return 0;
    }
    return 1;    
}
int main(){
    scanf("%d",&T);
    tt=0;
    while (T--){
          for (int i=0; i<4; i++)
              scanf("%s",b[i]);
          e=0; s=2;
          for (int i=0; i<4; i++)
              for (int j=0; j<4; j++)
                  if (b[i][j]=='.') e=1;
          
          for (int i=0; i<4; i++){
              if (checkrow(i,'X','T')||checkcol(i,'X','T')) s=0;
          }
          if (checkdiag1('X','T')||checkdiag2('X','T')) s=0;

          for (int i=0; i<4; i++){
              if (checkrow(i,'O','T')||checkcol(i,'O','T')) s=1;
          }
          if (checkdiag1('O','T')||checkdiag2('O','T')) s=1;
          
          ++tt;
          printf("Case #%d: ",tt);
          if (s==0) printf("X won\n");
          else if (s==1) printf("O won\n");
          else if (e==0) printf("Draw\n");
          else printf("Game has not completed\n");
          
    }
    return 0;    
}
