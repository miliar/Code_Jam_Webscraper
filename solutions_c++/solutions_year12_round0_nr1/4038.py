#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N;
  char tr[] = "yhesocvxduiglbkrztnwjpfmaq";
	
  scanf("%d\n", &N);
	
	for (int n=1; n<=N; n++) { 
  	int i;
	  char str[101];
	  char tstr[101];
    gets(str);
    
    for(i=0; i<strlen(str); i++) 
      if (str[i]==' ') tstr[i] = ' ';
      else tstr[i] = tr[str[i] - 'a'];
    tstr[i] = '\0';
    
	  cout << "Case #" << n << ": " << tstr << endl;
	}
	
  return 0;
}
