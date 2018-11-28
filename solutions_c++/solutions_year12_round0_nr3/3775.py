#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int count_digits(int n) {

    int digits = 0;
    while(n > 0) {
      n = n/10;
      digits++;
    }
    return digits;
}

int POW(int x, int y){
  int result = 1;
  for(int i = 0; i < y; i++){
    result *= x;
  }
  return result;
}

int main(){

  int start = 2000, end = 2222;

  int n;
  scanf("%d", &n);
  for(int iteration = 0; iteration < n; iteration++){
   int count = 0;
   scanf("%d %d", &start, &end);
   int digits = count_digits(start);
   for(int i = start; i <= end; i++) {
      int tmp = i;
      do{
        int last = tmp % 10;
        tmp = tmp/10;
        tmp = tmp + last * POW(10, digits-1);
        if (tmp > i && tmp <= end) {count++;}
      }while( tmp != i );
    }
    printf("Case #%d: %d\n",iteration+1,count);
  }
}
