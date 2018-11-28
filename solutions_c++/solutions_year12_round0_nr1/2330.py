#include <iostream>
#include <math.h>
#include <stdio.h>

using namespace std;

char map(char a) {

   switch(a) 
   {

      case 'a': return 'y'; break;
      case 'b': return 'h'; break;
      case 'c': return 'e'; break;
      case 'd': return 's'; break;
      case 'e': return 'o'; break;
      case 'f': return 'c'; break;
      case 'g': return 'v'; break;
      case 'h': return 'x'; break;
      case 'i': return 'd'; break;
      case 'j': return 'u'; break;
      case 'k': return 'i'; break;
      case 'l': return 'g'; break;
      case 'm': return 'l'; break;
      case 'n': return 'b'; break;
      case 'o': return 'k'; break;
      case 'p': return 'r'; break;
      case 'q': return 'z'; break;
      case 'r': return 't'; break;
      case 's': return 'n'; break;
      case 't': return 'w'; break;
      case 'u': return 'j'; break;
      case 'v': return 'p'; break;
      case 'w': return 'f'; break;
      case 'x': return 'm'; break;
      case 'y': return 'a'; break;
      case 'z': return 'q'; break;
      default:
         return ' ';

   }


}

int main() 
{
   int n;
   char c;


   cin >> n;

   c = getchar();
   for(int t = 1; t <= n; t++)
   {
      cout << "Case #" << t << ": ";
      c = getchar();

      while(c != '\n') 
      {
         cout << map(c);
         c = getchar(); 
      }
      
      cout << endl;
   }
return 0;
}
