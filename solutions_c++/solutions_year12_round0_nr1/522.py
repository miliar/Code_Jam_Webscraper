#include<cstdio>
char t[256], 
     from[] = "zy qeeejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv\n",
       to[] = "qa zooour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up\n";
main() {
  int i, T, C = 1;
  for (i = 0; from[i]; ++i)
    t[from[i]] = to[i];
  scanf("%d%*c", &T);
  while (T--) {
    printf("Case #%d: ", C++);
    i = 0; 
    while (i != '\n') {
      i = getchar();
      putchar(t[i]);
    }
  }
}
