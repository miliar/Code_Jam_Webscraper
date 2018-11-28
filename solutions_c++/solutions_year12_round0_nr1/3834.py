
#include <stdio.h>
#include <string.h>
#include <malloc.h>


main() {

  char tr[1000];
  char transl[1000] = " ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupazoo";
  char crypt[1000] = " ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvyqee";
  
  for (int i = 0; i < strlen(transl); i++) {
    tr[crypt[i]] = transl[i];    
  }
  tr['z'] = 'q';

  int T;

  scanf("%d\n",&T);
  size_t n = 1000;
  char *str = (char *) malloc(n);

  for (int t = 1; t <= T; t++) {
    str[0] = 0;
    getline(&str,&n,stdin);
    int len = strlen(str);
    if ((str[len-1]<'a') && (str[len-1] != ' ' )) {
      str[len-1] = 0;
    }
    for (int p = 0; p < strlen(str); p++) {
      str[p] = tr[str[p]];
    }
    printf("Case #%d: %s\n",t,str);
  }





}
