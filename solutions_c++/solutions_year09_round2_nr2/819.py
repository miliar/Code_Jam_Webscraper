#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstring>
using namespace std;

int main(){
  int C;
  scanf("%d\n", &C);
  char number[50];
  char result[50];
  for(int c = 1; c <= C; ++c){
    gets(number);
    if(!next_permutation(number, &number[strlen(number)])) {
      char *iter_number = number;
      int zero_count = 0;
      while((*iter_number) == '0') {
        ++zero_count;
        ++iter_number;
      }
      result[0] = *iter_number;
      for(int i = 1; i <= zero_count + 1; ++i)
        result[i] = '0';
      strcpy(&result[zero_count + 2], &number[zero_count + 1]);
    } else {
      strcpy(result, number);
    }
    
//     printf("%s\n", number);
    printf("Case #%d: %s\n", c, result);
  }
  return 0;
}