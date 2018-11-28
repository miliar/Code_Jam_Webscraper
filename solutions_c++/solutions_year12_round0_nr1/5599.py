#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <assert.h>

char* instrs[4] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                   "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                   "de kr kd eoya kw aej tysr re ujdr lkgc jv",
                   0};

char* outstrs[4] = {"our language is impossible to understand",
                   "there are twenty six factorial possibilities",
                   "so it is okay if you want to just give up",
                   0};

int main(int argc, int* argv)
{
  char map[26];

  memset(map, 0, sizeof(map));
  for(int i = 0; i < 3; ++i) {
    char* is = instrs[i];
    char* os = outstrs[i];
    while(*is) {
      if(*is>='a' && *is<='z') {
        map[(*is)-'a']= *os;
      }
      ++is;
      ++os;
    }
  }

/* 
  for(int i=0;  i < 26; ++i) {
    //printf("%d ", map[i]);
    if(map[i]=='\0') {
      printf("%c", i+'a');
    }
    //printf("\n");
  }
  printf("\n");
  
  return 0;
  
  for(int i=0;  i < 26; ++i) {
    //printf("%d ", map[i]);
    if(map[i]=='\0') {
      //assert(0);
      for(int j = i+1; j < 26; ++j) {
        if(map[j]=='\0') {
          map[i] = j + 'a';
          map[j] = i + 'a';
        }
      }
      break;
    }
    //printf("\n");
  }

*/
  map['q'-'a'] = 'z';
  map['z'-'a'] = 'q';

  for(int i=0;  i < 26; ++i) {
    //printf("%d ", map[i]);
    if(map[i]=='\0') {
      assert(0);
    }
    //printf("\n");
  }
  
  int t=0;
  char buf[1000];
  char result[1000];  
  gets(buf);
  t=atoi(buf);
  for(int i = 1; i <= t; ++i) {
    gets(buf);
    char* is = buf;
    char* os = result;
    while(*is) {
      if(*is>='a' && *is<='z') {
        *os = map[(*is)-'a'];
      }
      else {
        *os = *is;
      }
      ++is;
      ++os;
    }
    *os='\0';

    printf("Case #%d: %s\n", i, result);
    //printf("%s\n", result);
  }

  return 0;
}

