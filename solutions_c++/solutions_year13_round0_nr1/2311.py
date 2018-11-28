#include <stdio.h>
#include <vector>

int main() {

  std::vector< std::vector<int> > arr;
  int N;
   int I =0;
  char buf[10];
  scanf("%d", &N);
  while(N-- > 0) {
    bool full = true;
    arr.resize(4);
    arr.clear();
    for (int i = 0; i < 4; i++) {
      arr[i].resize(4);
      arr[i].clear();
      scanf("%s", buf);
      for (int j = 0; j < 4; j++) {
	char c = buf[j];;
  
	//printf("przeczytalem '%c' \n", c);
	if (c == '.') {
	  full = false;
	  arr[i][j] = 0;
	}
	if (c == 'X')
	  arr[i][j] = 1;
	if (c == 'O')
	  arr[i][j] = 2;
	if (c == 'T')
	  arr[i][j] = 3;
      }
    }
    
    // 1 - X won
    // 2 - O won
    // 3 - nobody
    int res = -1;
   
   for (int i = 0; i < 4; i++) {
     //checking X
     bool won = true;
     for (int j = 0; j < 4; j++) {
       // printf("arr[%d][%d] = %d\n", i ,j ,arr[i][j]);
       if (arr[i][j] == 2 || arr[i][j] == 0) {
	 won = false;
	  break;
       }
     }
     if (won) {
       res = 1;
       break;
     }

    won = true;
     for (int j = 0; j < 4; j++) {
       if (arr[j][i] == 2 || arr[j][i] == 0) {
	 won = false;
	 break;
       }
     }
     if (won) {
       res = 1;
       break;
     }

     // checking O
     won = true;
     for (int j = 0; j < 4; j++) {
       if (arr[i][j] == 1 || arr[i][j] == 0) {
	 won = false;
	 break;
       }
     }
     if (won) {
       res = 2;
       break;
     }

     won = true;
     for (int j = 0; j < 4; j++) {
       if (arr[j][i] == 1 || arr[j][i] == 0) {
	 won = false;
	 break;
       }
     }
     if (won) {
       res = 2;
       break;
     }

     res = 3;
   }


   bool won = true;
   for (int j = 0; j < 4; j++) {
     if (arr[j][j] == 1 || arr[j][j] == 0) {
       won = false;
       break;
     }
   }
   if (won) {
     res = 2;
   }
   
   won = true;
   for (int j = 0; j < 4; j++) {
     if (arr[j][3-j] == 1 || arr[j][3-j] == 0) {
       won = false;
       break;
     }
   }
   if (won) {
     res = 2;
   }


   won = true;
   for (int j = 0; j < 4; j++) {
     if (arr[j][j] == 2 || arr[j][j] == 0) {
       won = false;
       break;
     }
   }
   if (won) {
     res = 1;
   }

   won = true;
   for (int j = 0; j < 4; j++) {
     if (arr[j][3-j] == 2 || arr[j][3-j] == 0) {
       won = false;
       break;
     }
   }
   if (won) {
     res = 1;
   }




    printf("Case #%d: ", I+1);

    if (res == 3) {
      if (full) {
	printf("Draw\n");
      } else {
	printf("Game has not completed\n");
      }
    } else {
      printf("%c won\n", res==2?'O':'X');
    }
    

    I++;
  }


}
