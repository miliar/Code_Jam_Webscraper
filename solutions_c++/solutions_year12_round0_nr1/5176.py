#include <cstdio>
#include <cstring>

using namespace std;

char TABLE[26] = 
{ 'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd',
  'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't',
  'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

int main(void)
{
   int T;
   scanf("%d ", &T);
   for(int i = 1; i <= T; ++i)
   {
      printf("Case #%d: ", i);
      char buf[128];
      fgets(buf, 128, stdin);
      char* ptr;
      for(ptr = buf; *ptr != '\0'; ++ptr)
      {
         if(*ptr == ' ' || *ptr == '\n')
            putchar(*ptr);
         else
            putchar(TABLE[*ptr - 'a']);
      }
   }
   return 0;
   
}
