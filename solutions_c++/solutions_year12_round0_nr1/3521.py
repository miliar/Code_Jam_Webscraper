/* Author ]=  Jay Pandya */

// Standard includes
#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<limits.h>
#include<string.h>

//Data Structures
#include<algorithm>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>

using namespace std;

map<char,char> m;

void preprocess()
{
m[' ']= ' '; m['a']= 'y'; m['c']= 'e'; m['b']= 'h'; m['e']= 'o'; m['d']= 's'; m['g']= 'v'; m['f']= 'c'; m['i']= 'd'; m['h']= 'x'; m['k']= 'i'; m['j']= 'u'; m['m']= 'l'; m['l']= 'g'; m['o']= 'k'; m['n']= 'b'; m['q']= 'z'; m['p']= 'r'; m['s']= 'n'; m['r']= 't'; m['u']= 'j'; m['t']= 'w'; m['w']= 'f'; m['v']= 'p'; m['y']= 'a'; m['x']= 'm'; m['z']= 'q';
}
int main()
{
   preprocess();
   int test;
   scanf("%d ",&test);
   for(int i=1;i<=test;i++)
   {
      char c;
      printf("Case #%d: ",i);
      while(1)
      {
	 scanf("%c",&c);
	 if(c=='\n')
	 {
	    printf("\n");
	    break;
	 }
	 printf("%c",m[c]);
      }
   }
   return 0;
}


