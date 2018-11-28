#include <stdio.h>


int main() {
  int N;
  int result;
  char t[4][4];
  scanf(" %d",&N);
  
  for(int c=0; c<N; c++) {
      for(int j=0; j<4; j++){
        scanf(" %s", t[j]);
      }
      result = 0;
      char last = 0;
      
      for(int i=0; i<4; i++) {
        last = 0;
        for(int j=0; j<4; j++) {
          if (t[i][j] == '.' || (t[i][j] != 'T' && t[i][j] != last && last != 0)) {
            break;
          }
          if (t[i][j] != 'T') {
            last = t[i][j];
          }
          if (j==3) {
            result = 1;
            goto end;
          }
        }
        
        last = 0;
        for(int j=0; j<4; j++) {
          if (t[j][i] == '.' || (t[j][i] != 'T' && t[j][i] != last && last != 0)) {
            break;
          }
          if (t[j][i] != 'T') {
            last = t[j][i];
          }
          if (j==3) {
            result = 1;
            goto end;
          }
        }
      }
      
      last = 0;
      for(int i=0; i<4; i++) {
        if (t[i][i] == '.' || (t[i][i] != 'T' && t[i][i] != last && last != 0)) {
          break;
        }
        if (t[i][i] != 'T') {
          last = t[i][i];
        }
        if (i==3) {
          result = 1;
          goto end;
        }
      }
      
      last = 0;
      for(int i=0; i<4; i++) {
        if (t[i][3-i] == '.' || (t[i][3-i] != 'T' && t[i][3-i] != last && last != 0)) {
          break;
        }
        if (t[i][3-i] != 'T') {
          last = t[i][3-i];
        }
        if (i==3) {
          result = 1;
          goto end;
        }
      }
      
      if (result == 0) {
        for(int i=0; i<4; i++) {
          for(int j=0; j<4; j++) {
            if(t[i][j] == '.') {
              goto end;
            }
          }
        }
        result = 2;
      }

end:
      printf("Case #%d: ", c+1);
      if (result == 0) {
        printf("Game has not completed\n");
      }
      if (result == 1) {
        printf("%c won\n", last);
      } 
      if (result == 2) {
        printf("Draw\n");
      }
    }
}
