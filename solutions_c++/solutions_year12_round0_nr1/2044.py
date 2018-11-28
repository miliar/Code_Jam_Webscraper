#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char mapping[26];
char mapping_back[26];
void map(const char *from, const char *to) {
  int len = strlen(from);
  for (int i = 0; i < len; ++i) {
	if (from[i] >= 'a' && from[i] <= 'z') {
	  mapping[from[i]-'a'] = to[i];
	  mapping_back[to[i]-'a'] = from[i];
	}
  }
}

void init_mapping()
{
  for (int i = 0; i < 26; ++i) {
	mapping[i] = 'a'+i;
	mapping_back[i] = 'a'+i;
  }

  map("our language is impossible to understand",
	 "ejp mysljylc kd kxveddknmc re jsicpdrysi");
  map("there are twenty six factorial possibilities",
	 "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
  map("so it is okay if you want to just give up",
	 "de kr kd eoya kw aej tysr re ujdr lkgc jv");
  map("qz", "zq");
}

int main(int argc, char *argv[])
{
  init_mapping();
  char line[123];
  int T, c;
  scanf("%d", &T); gets(line);
  for (c = 1; c <= T; ++c) {
	fgets(line, sizeof(line), stdin);
	printf("Case #%d: ", c);
	char *ch = line;
	while (*ch) {
	  if (*ch >= 'a' && *ch <= 'z') {
		putchar(mapping_back[*ch-'a']);
	  } else {
		putchar(*ch);
	  }
	  ++ch;
	}
  }

  return 0;
}
