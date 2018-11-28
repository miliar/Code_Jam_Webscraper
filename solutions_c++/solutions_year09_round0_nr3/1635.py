
#include <stdio.h>
#include <string.h>


char target[20] = "welcome to code jam";



int count(char * line) {


  int len = strlen(line);
  
  int c[20][50];

  for (int letter = 0; letter < strlen(target); letter++) {
    
    for (int i = 0; i < 50; i++)
      c[letter][i] = 0;    
  }
  
  // c[l][p] = number of times substrings of target up to letter l 
  //             appear before character p of the line - and finish at pos p;


  for (int i = 0; i < strlen(line); i++)
    if (line[i] == target[0]) {
      c[0][i] = 1;
    }
  
    

  for (int letter = 1; letter < strlen(target); letter++) {
    
    for (int i = 0; i < strlen(line); i++)

      if (line[i] == target[letter]) {
	
	c[letter][i] = 0;
	for (int j = 0; j < i; j++) {
	  c[letter][i] += c[letter-1][j];	  
	}
	
      }
      else {
	c[letter][i] = 0;    	
      }
  }
  
  int total = 0;
  int nletters = strlen(target);
  for (int i = 0; i < strlen(line); i++)
    {
      total += c[nletters-1][i];
      
    }


  return total;
}


main() {

  int N;

  char line[50];


  scanf("%d\n",&N);
  
  
  for (int i = 1; i <= N; i++) {
    
    scanf("%[^\n]\n",line);

    
    
    printf("Case #%d: %04d\n",i,count(line)%10000);
    
  }


}
