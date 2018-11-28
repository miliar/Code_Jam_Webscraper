
#include<cstdio>
#include<iostream>
#include<string>

//English
#define MAX_SYMBOLS 26
#define INDEX_OFFSET 97

const char lookup[MAX_SYMBOLS] =
{'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};


int main(void)
{
  int test_count = 0;
  int i;
  char c;

  scanf("%d",&test_count);
  while(1) { scanf("%c",&c); if(c == '\n') {break;} }
  for(i=0;i<test_count;i++)
  {
    printf("Case #%d: ",i+1);
    while(1)
    {
      scanf("%c",&c);
      if(((c < 'a')||(c > 'z')) && (c != ' '))
      {
        printf("\n");
        break;
      }
      else if(c == ' ')
      {
        printf(" ");
      }
      else
      {
        printf("%c",lookup[c-INDEX_OFFSET]);
      }
    }
  }
return 0;
}
