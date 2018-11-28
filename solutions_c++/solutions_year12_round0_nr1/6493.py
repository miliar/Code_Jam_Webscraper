#include <stdio.h>
#include <map>
#include <utility>
#include <string.h>
#include <stdlib.h>
#include <iostream>

using namespace std;
int main()
{
   map<char,char> ch_map;
   
   ch_map['d'] = 's';
   ch_map['i'] = 'd';
   ch_map['k'] = 'i';
   ch_map['o'] = 'k';
   ch_map['e'] = 'o';
   ch_map['c'] = 'e';
   ch_map['f'] = 'c';
   ch_map['w'] = 'f';
   ch_map['t'] = 'w';
   ch_map['r'] = 't';
   ch_map['p'] = 'r';
   ch_map['v'] = 'p';
   ch_map['g'] = 'v';
   ch_map['l'] = 'g';
   ch_map['m'] = 'l';
   ch_map['x'] = 'm';
   ch_map['h'] = 'x';
   ch_map['b'] = 'h';
   ch_map['n'] = 'b';
   ch_map['s'] = 'n';
   ch_map['y'] = 'a';
   ch_map['a'] = 'y';
   ch_map['z'] = 'q';
   ch_map['q'] = 'z';
   ch_map['j'] = 'u';
   ch_map['u'] = 'j';
   ch_map[' '] = ' ';
   int test_cases, index = 1;
   scanf("%d", &test_cases);
   char buffer[1001];

   gets(buffer);
   while(test_cases > 0)
   {
       cin.getline(buffer, 1000);
       for(int i = 0; buffer[i]!='\0'; i++)
       {
          buffer[i] = ch_map[buffer[i]];  
       }
       cout << "Case #" << index << ": "<< buffer << endl;
       index++;
       test_cases--;
   }
   
   return 0;
}

