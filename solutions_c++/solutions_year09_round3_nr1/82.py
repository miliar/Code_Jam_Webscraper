
#include <stdio.h>

#include<string>
#include<map>

using namespace std;



main() {

  
  int T;

  char line[100];
  
  scanf("%d",&T);
  
  
  
  for (int t = 1; t <= T; t++) {

    scanf("%s",line);

    unsigned long long int result;
    
    unsigned long long int base = 0;

    int len = strlen(line);
    map<char,int> value;
    int numchars = 0;

    for (int p = 0; p < len; p++) {
      if (value.find(line[p]) == value.end()) {
	numchars++;
	if (numchars == 1) {
	  value[line[p]] = 1;
	}
	else {
	  if (numchars == 2) {
	    value[line[p]] = 0;
	  }
	  else {
	    value[line[p]] = numchars - 1;
	  }
	}
      }
      
    }

    if (numchars <= 1) {
      base = 2;
    }
    else 
      base = numchars;
    
    // now compute num;

    result = 0;
    
    for (int p = 0; p < len; p++) {
      result *= base;
      result += value[line[p]];
    }
    
    printf("Case #%d: %llu\n",t,result);
    
  }





}
