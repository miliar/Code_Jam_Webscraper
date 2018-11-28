#include <stdio.h>
#include <string.h>

int main(){
  freopen("1.in","r",stdin);
  int t = 6;
  int map [300] = {0};
  map['z'] = 'q';
  map['q'] = 'z';
  map[' '] = ' ';
  int j=0;
  char s[31][110];
  while(t--){
    gets(s[j]);
    if(j%2){
      for(int i=0;i<strlen(s[j-1]);i++){
        map[s[j][i]] = s[j-1][i];
      }
    }
    j++;
  }
  fclose(stdin);
  freopen("A-small-attempt0.in","r",stdin);
  freopen("smallA.out","w",stdout);
  int test;
  int i=0;
  scanf("%d\n",&test);
  char str[100][200];
  while(test--){
    gets(str[i]);
    printf("Case #%d: ",i+1);
    for(int j=0;j<strlen(str[i]);j++){
      printf("%c",map[str[i][j]]);
    }
    printf("\n");
    i++;
  }
  
  return 0;
}
