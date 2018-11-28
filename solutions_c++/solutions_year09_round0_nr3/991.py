#include<cstdio>
#include<cstring>

bool isAcChar(char c)
{
   return ((c >= 'a' && c <= 'z') || c == ' ');
}

int main()
{
   const char caption[] = "welcome to code jam";
   const int captLen = 19;
   const int modulo = 10000;

   int i, j, k, l, len, result;
   int N;
   char c = 0;
   bool wasLetter;
   char s[510];
   int t[500][captLen];

   scanf("%d", &N);

   for(i = 1 ; i <= N ; i++)
   {
      wasLetter = false;
      len = 0;
      while(isAcChar(c) || !wasLetter)
      {
         scanf("%c", &c);

         if (isAcChar(c))
         {
            s[len++] = c;
            wasLetter = true;
         }
      }

      result = 0;
      memset(t, 0, sizeof(t));

      for(j = 0 ; j < len ; j++)
      {
         if (s[j] == caption[0])
         {
            for(k = j + 1 ; k < len ; k++)
            {
               if(s[k] == caption[1])
               {
                  t[k][1]++;
                  t[k][1] %= modulo;
               }
            }
         }

         for(k = 1 ; k < captLen - 1 ; k++)
         {
            if (t[j][k])
            {
               for(l = j + 1 ; l < len; l++)
               {
                  if(s[l] == caption[k+1])
                  {
                     t[l][k+1] += t[j][k];
                     t[l][k+1] %= modulo;
                  }
               }
            }
         }

         if(t[j][captLen-1])
         {
            result += t[j][captLen-1];
            result %= modulo;
         }
      }
      printf("Case #%d: %.4d\n", i, result);
   }

   return 0;
}


