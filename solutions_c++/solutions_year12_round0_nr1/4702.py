
/* -------- Author: Harshit Agrawal --------- */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
#include <limits.h>

using namespace std;

#define MAXN 100
#define x first
#define y second

typedef pair<int,int> ii;
typedef long long int ll;
int myGCD( int a, int b)
{
   if(b==0) return a;
   else 
      return myGCD(b,a%b);
}

int myPOW(int a, int b)
{
   int val;
   if( b==0 ) return 1;
   if( b==1 ) return a;
   val = myPOW(a,b/2);
   val = val*val;
   return (b%2)?val*a:val;
}

int main() {
   map<char,char> M;
   M['a'] = 'y';
   M['b'] = 'h';
   M['c'] = 'e';
   M['d'] = 's';
   M['e'] = 'o';
   M['f'] = 'c';
   M['g'] = 'v';
   M['h'] = 'x';
   M['i'] = 'd';
   M['j'] = 'u';
   M['k'] = 'i';
   M['l'] = 'g';
   M['m'] = 'l';
   M['n'] = 'b';
   M['o'] = 'k';
   M['p'] = 'r';
   M['q'] = 'z';
   M['r'] = 't';
   M['s'] = 'n';
   M['t'] = 'w';
   M['u'] = 'j';
   M['v'] = 'p';
   M['w'] = 'f';
   M['x'] = 'm';
   M['y'] = 'a';
   M['z'] = 'q';
   M[' '] = ' ';
   int n;
   scanf("%d",&n);
   int i=1;
   int le ;
   char str[200000];
   while(i<=n)
   {
      scanf(" %[^\n] ",str);
      le = strlen(str);
      printf("Case #%d: ",i);
      for(int j=0;j<le;j++)
	 printf("%c",M[str[j]]);
      printf("\n");
      i++;
   }
   return 0;
}

