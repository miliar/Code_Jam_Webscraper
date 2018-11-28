#include <cstdio>
#include <string>
#include <iostream>
#include <cassert>
#include <cstring>

using namespace std;

int main() {
  char hash_v[12012];

  memset(hash_v, 0, sizeof(hash_v));
 
  hash_v['y'] = 'a';
  hash_v['e'] = 'o';

  hash_v['q'] = 'z';
  
  hash_v['z'] = 'q';

  string a[3];
  a[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  a[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  a[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string b[3];
  b[0] = "our language is impossible to understand";
  b[1] = "there are twenty six factorial possibilities";
  b[2] = "so it is okay if you want to just give up";
  
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < (int)a[i].size(); j++) {
      hash_v[ (int)a[i][j] ] =  b[i][j];
      //hash_v[ (int)b[i][j] ] =  a[i][j];
    }
  }

  hash_v[' '] = ' ';
  int t;
  scanf("%d",&t);
  getchar();
  int case_n = 1;
  while (t--) {
    string c;
    getline(cin, c);

    printf("Case #%d: ", case_n++);
    for (int i = 0; i < c.size(); i++) {
      printf("%c",hash_v[c[i]]);


 


      
    }
    printf("\n");
  }
  return 0;
}
