#include <stdio.h>
#include <math.h>
#include <map>

using namespace std;

map<char, char> mapping;

void solve(int testCaseNumber)
{
   char googlerese[101];
   gets(googlerese);

   printf("Case #%d: ", testCaseNumber + 1);

   for(int i = 0; i < 100; i++)
   {
      if(googlerese[i] == '\0')
         break;
      printf("%c", mapping[googlerese[i]]);
   }

   printf("\n");
}

int main(int argc, char** argv)
{
   mapping['y'] = 'a';
   mapping['n'] = 'b';
   mapping['f'] = 'c';
   mapping['i'] = 'd';
   mapping['c'] = 'e';
   mapping['w'] = 'f';
   mapping['l'] = 'g';
   mapping['b'] = 'h';
   mapping['k'] = 'i';
   mapping['u'] = 'j';
   mapping['o'] = 'k';
   mapping['m'] = 'l';
   mapping['x'] = 'm';
   mapping['s'] = 'n';
   mapping['e'] = 'o';
   mapping['v'] = 'p';
   mapping['z'] = 'q';
   mapping['p'] = 'r';
   mapping['d'] = 's';
   mapping['r'] = 't';
   mapping['j'] = 'u';
   mapping['g'] = 'v';
   mapping['t'] = 'w';
   mapping['h'] = 'x';
   mapping['a'] = 'y';
   mapping['q'] = 'z';
   mapping[' '] = ' ';

   int noOfTestCases = 0;
   scanf("%d\n", &noOfTestCases);
   for(int i = 0; i < noOfTestCases; i++)
   {
      solve(i);
   }
   return 0;
}