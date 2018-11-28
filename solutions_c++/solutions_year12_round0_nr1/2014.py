#include <iostream>
#include <cstring>

char ref1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
char ref2[] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char ref3[] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

char ans1[] = "our language is impossible to understand";
char ans2[] = "there are twenty six factorial possibilities";
char ans3[] = "so it is okay if you want to just give up";

char G[1000];

int main() {
  char t[256];
  memset(t, 0, sizeof(t));
  
  for (int i = 0; ref1[i] != '\0'; i++) {
    t[ref1[i]] = ans1[i];
  }
  for (int i = 0; ref2[i] != '\0'; i++) {
    t[ref2[i]] = ans2[i];
  }
  for (int i = 0; ref3[i] != '\0'; i++) {
    t[ref3[i]] = ans3[i];
  }
  
  for (int i = 'a'; i <= 'z'; i++) {
   // printf("i  = %c , t = %c\n", i, t[i]);
  }
  t['q'] = 'z';
  t['z'] = 'q';
  
  int nrTest;
  scanf("%d\n", &nrTest);
  for (int testcase = 1; testcase <= nrTest; testcase++) {
    gets(G);
    printf("Case #%d: ", testcase);
    for (int i = 0; i < strlen(G); i++) {
      G[i] = t[G[i]];
      putchar(G[i]);
    }
    printf("\n");
    
  }
 
  return 0; 
}
