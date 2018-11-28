#include <stdio.h>
#include <string>
#include <map>
#include<set>

using namespace std;

main( )


{

  int T;
  char lista[1000];
  scanf("%d\n",&T);
  char bases[3];
  bases[2] = 0;

  for (int t = 1; t <= T; t++) {

    int C;
    int D;
    int size = 0;
    std::map<string,char> convert;
    
    std::map<char,set<char> > oppose;
    
    scanf("%d",&C);
    for (int c = 0; c < C; c++) {
      char str[5];
      scanf("%s",str);
      char nb = str[2];
      bases[0] = str[0];
      bases[1] = str[1];
      convert[bases] = nb;
      bases[0] = str[1];
      bases[1] = str[0];
      convert[bases] = nb;
    }
    scanf("%d",&D);
    for (int d = 0; d < D; d++) {
      char str[5];
      scanf("%s",str);
      
      oppose[str[0]].insert(str[1]);
      oppose[str[1]].insert(str[0]);
      
    }
    
    int N;
    
    scanf("%d ",&N);
    
    for (int n = 0; n < N; n++) {
      char letter;
      char prev;
      scanf("%c",&letter);
      
      bool changed = true;

      while (changed) {
	changed = false;
	if (size > 0) {
	  prev = lista[size-1];
	  bases[0] = prev;
	  bases[1] = letter;
	  string s = bases;
	  if (convert.find(s) != convert.end()) {
	    letter = convert[s];
	    size--;
	    changed = true;
	  }
	}
      }
      lista[size] = letter;
      size++;
      if (oppose.find(letter) != oppose.end()) {
	set<char> &myset = oppose[letter];
	
	bool found = false;
	for (int p = 0; (!found) && (p < size-1); p++) {
	  if (myset.find(lista[p]) != myset.end()) {
	    found = true;
	  }
	}
	
	if (found) {
	  size = 0;
	}
      }
    }

    
    printf("Case #%d: [",t);
    
    for (int i = 0; i < size-1; i++) {
      printf("%c, ",lista[i]);
    }
    if (size > 0) {
      printf("%c",lista[size-1]);
    }
    printf("]\n");

  }




}
