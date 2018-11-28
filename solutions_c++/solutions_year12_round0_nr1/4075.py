#include<stdio.h>
#include<stdlib.h>

int main(){
  char line[256], cline[256];
  char dict[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u',
		   'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w',
		   'j', 'p', 'f', 'm', 'a', 'q'};
  int nlines;
  int i, j;
  gets(line);
  nlines = atoi(line);
  for(i = 0; i < nlines; i++){
    gets(line);
    //printf("%s\n", line);
    j = 0;
    for(j = 0; j < 256; j++){
      if(line[j] == '\0'){
	cline[j] = line[j];
	printf("Case #%d: %s\n", i + 1, cline);
	break;
      }
      else if(line[j] == ' '){
	cline[j] = line[j];
      }
      else{
	cline[j] = dict[int(line[j]) - 97];
      }
    }
  }
  return 0;
}
