
#include <stdio.h>
#include <string.h>

main() {

  int T;

  scanf("%d",&T);


  for (int t = 1; t <= T; t++) {

    char result[100];
    
    scanf("%s",result);

    int numDigits = strlen(result);
    int mini = -1;
    int minj = 0;
    char min = result[numDigits-1];
    int found = 0;
    for (int j = numDigits - 2; found == 0 && j >= 0; j--) {
      for (int i= j +1; i < numDigits; i++) 
	if ((result[i] != '0') && (result[i] > result[j])) {
	  found = 1;
	  minj = j;
	  if ((mini == -1) || ( result[mini] > result[i]))
	    mini = i;
	}
    }
    

    if (found == 0) {
      result[numDigits] = '0';
      numDigits++;
      result[numDigits] = 0;
      mini = numDigits-1;
      minj = 0;
    }
    
    char tmp = result[mini];
    result[mini] = result[minj];
    result[minj] = tmp;
    

    for (int i = numDigits-1;i > minj; i--) 
      for (int j = i-1; j > minj; j--) {
	if (result[i] < result[j]) {
	  char tmp = result[i];
	  result[i] = result[j];
	  result[j] = tmp;
	}
      }
    if (found == 0) {
      for (int i = 1; (result[0] == '0') && i < numDigits; i++)
	if (result[i] != '0') {
	  result[0] = result[i];
	  result[i] = '0';
	}
    }
	 

    printf("Case #%d: %s\n",t,result);

  }





}
