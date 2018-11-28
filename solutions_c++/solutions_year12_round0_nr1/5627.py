#include<stdio.h>
#include<string.h>

int k = 0;
const char word[26] = {'y','h','e','s','o','c','v','x','d','u','i',
                                    'g','l','b','k','r','z','t','n','w','j',
                                    'p','f','m','a','q'};

void xx()
{
    char c;
    printf("Case #%d: ",++k);
    while(scanf("%c",&c), c != '\n')
       if(c <= 'z' && c >= 'a') printf("%c",word[c-'a']);
          else printf("%c",c);
    printf("%c",c);
}

int main()
{
  int n,c;
  freopen("GCJ_A.in","r",stdin);
  freopen("GCJ_A.out","w",stdout);
  scanf("%d",&n);
  while(n--) xx();
  return 0;
}
