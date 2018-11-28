#include <cstdio>
#include <cstdlib>

int nt0,nt;
char map['z'-'a'+1];
char line[128];

char strings[6][128] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                        "our language is impossible to understand",
                        "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                        "there are twenty six factorial possibilities",
                        "de kr kd eoya kw aej tysr re ujdr lkgc jv",
                        "so it is okay if you want to just give up"};

void create_map() {
  map['y'-'a'] = 'a';
  map['e'-'a'] = 'o';
  map['q'-'a'] = 'z';
  for(int i=0 ; i<6 ; i+=2)
    for(char *t1 = strings[i], *t2 = strings[i+1] ; *t1 != '\0' ; ++t1, ++t2)
      map[*t1-'a'] = *t2;
  map['z'-'a'] = 'q';
}

int main() {
  create_map();

  scanf(" %d", &nt0);
  for(nt=1 ; nt<=nt0 ; ++nt) {
    scanf(" %[^\r\n]", line);
    printf("Case #%d: ", nt);
    for(char *t = line ; *t != '\0' ; ++t)
      if(*t == ' ') putchar(*t);
      else putchar(map[*t-'a']);
    putchar('\n');
  }

  return 0;
}
