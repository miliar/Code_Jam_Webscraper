#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
using namespace std;

int main () {

    freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
   
  
   
   map <char, char > hash;
   
   hash['a'] = 'y'; hash['b'] = 'h';
   hash['c'] = 'e'; hash['d'] = 's';
   hash['e'] = 'o'; hash['f'] = 'c';
   hash['g'] = 'v'; hash['h'] = 'x';
   hash['i'] = 'd'; hash['j'] = 'u';
   hash['k'] = 'i'; hash['l'] = 'g';
   hash['m'] = 'l'; hash['n'] = 'b';
   hash['o'] = 'k'; hash['p'] = 'r';
   hash['q'] = 'z'; hash['r'] = 't';
   hash['s'] = 'n'; hash['t'] = 'w';
   hash['u'] = 'j'; hash['v'] = 'p';
   hash['w'] = 'f'; hash['x'] = 'm';
   hash['y'] = 'a'; hash['z'] = 'q'; 
   hash[' '] = ' ';  

   int t,i=1;
   string letter;
   scanf("%d", &t);

 getline(cin,letter);
   while(t--)
   {
    
    
     getline(cin,letter);
     printf("Case #%d: ", i);  i++;
      for (int i =0; i < letter.length(); i++)
      {
          printf("%c", hash[ letter[i]]);
      }   
      printf("\n"); 
   }
}

