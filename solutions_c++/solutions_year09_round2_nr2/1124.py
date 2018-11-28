#include <stdio.h>
#include <algorithm>
#include <functional>

using namespace std;

int main(){
	int T;
  scanf("%d", &T);
  char ch;
  scanf("%c", &ch);

  char s[25],_s[25];
  int i;
  for(i = 0; i < T; i++){
    gets(s);
    strcpy(_s,s);
    int len = strlen(s);
    next_permutation(s,s+len);
    if(strcmp(s, _s) > 0 )
      printf("Case #%d: %s\n", i+1, s);
    else{      
      bool flg = 1;
      for(int k = 1 ; k < len; k++){
        if(_s[k] != '0'){
          flg = 0;
          break;
        }
      }
      if(flg){
        printf("Case #%d: %s%c\n", i+1, _s,'0');
      }else{
        int zeCnt = 0;
        int j ;
        for( j = len-1; j>=0; j--){
            if(_s[j] == '0')
              zeCnt++;
            else
              break;
        }
        printf("Case #%d: %c%c", i+1, _s[j],'0');
        for(int t = 0; t < zeCnt; t++)
          printf("0");
        for(--j;j >=0; j--){
          printf("%c", _s[j]);
        }
        printf("\n");
      }
    }
  }
	return 1;
}
