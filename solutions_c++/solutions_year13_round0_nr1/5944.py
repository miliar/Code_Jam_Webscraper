#include <stdio.h>
int main()
{
  freopen("A-small-attempt0.in","rt",stdin);
  freopen("A-small-attempt0.out","wt",stdout);
  int t,ntest,countr,countd,countx1,countx2;
  bool noAns,hasAns;
  char b[5][5],ans;
  scanf("%d",&ntest);
  for(t=1;t<=ntest;t++){
    for(int i=0;i<4;i++){
      scanf("%s",b[i]);
    }
    hasAns = noAns = false;
    for(int i=0;i<4;i++){
      countd = countr = countx1 = countx2 = 0;
      for(int j=0;j<4;j++){
        if(b[i][j] != '.'){
          if(b[i][j] == b[i][0] || b[i][j] == 'T')
            countr++;
        }else{
          noAns = true;
        }
        if(b[j][i] != '.'){
          if(b[j][i] == b[0][i] || b[j][i] == 'T')
            countd++;
        }else{
          noAns = true;
        }
      }
      if(countr==4){
        hasAns = true;
        ans = b[i][0];
        if(ans == 'T')
          ans = b[i][1];
        break;
      }
      if(countd==4){
        hasAns = true;
        ans = b[0][i];
        if(ans == 'T')
          ans = b[1][i];
        break;
      }
    }
    if(hasAns){
      printf("Case #%d: %c won",t,ans);
    }else{
      for(int i =0;i<4;i++){
        if(b[i][i]!='.')
        if(b[0][0] == b[i][i] || b[i][i] == 'T')
          countx1++;
        if(b[i][3-i] !='.')
        if(b[0][3] == b[i][3-i] || b[i][3-i] == 'T')
          countx2++;
      }
      if(countx1==4){
        hasAns = true;
        ans = b[0][0];
        if(ans == 'T')
          ans = b[1][1];

      }
      if(countx2==4){
        hasAns = true;
        ans = b[0][3];
        if(ans == 'T')
          ans = b[1][2];

      }
      if(hasAns){
        printf("Case #%d: %c won",t,ans);
      }else if(noAns){
        printf("Case #%d: Game has not completed",t);
      }else{
        printf("Case #%d: Draw",t);
      }
    }
    printf("\n");
  }
  return 0;
}
