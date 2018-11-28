#include<cstdio>
#include<cmath>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);

  for(int C=1; C<=T; ++C) {
    char s[64];
    scanf("%s", s);

    int q = 0;
    for(int i=0; s[i]; ++i)
      if(s[i]=='?') q++;
    printf("Case #%d: ", C);
    for(int i=0; i<(1<<q); ++i) {
      long long t = 0;
      int x = 0;
      for(int j=0; s[j]; ++j)
	if(s[j]=='?') t = t*2 + ((i & (1<<(x++))) != 0 ? 1 : 0);
	else t = t*2 + s[j]-'0';
      long long p = (long long)sqrt((double)t);
      if(p*p==t || (p-1)*(p-1)==t || (p+1)*(p+1)==t) {
	x=0;
	for(int j=0; s[j]; ++j)
	  if(s[j]=='?') putchar((i & (1<<(x++))) ? '1' : '0');
	  else putchar(s[j]);
	puts("");
	break;
      }
    }
  }
}
