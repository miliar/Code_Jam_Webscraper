#include <cstdio>
#include <cstring>

int main()
{
     int t, i, j;
     scanf("%d", &t);

     for (i = 1; i <= t; ++i) {
	  char number[62];
	  bool appear[128];
	  long long digit[128];
	  long long len, ans, base;
	  scanf("%s", number);
	  len = strlen(number);
	  memset(appear, 0, sizeof(appear));

	  appear[number[0]] = true;
	  digit[number[0]] = 1;
	  j = 1;
	  while (j < len && number[j] == number[0])
	       ++j;
	  if (j < len) {
	       appear[number[j]] = true;
	       digit[number[j]] = 0;
	       ++j;
	  }
	  base = 2;
	  for (; j < len; ++j)
	       if (!appear[number[j]]) {
		    appear[number[j]] = true;
		    digit[number[j]] = base;
		    ++base;
	       }

	  ans = 0;
	  for (j = 0; j < len; ++j) {
	       ans = ans * base + digit[number[j]];
	  }
	  
	  printf("Case #%d: %lld\n", i, ans);
     }
     
     return 0;
}
