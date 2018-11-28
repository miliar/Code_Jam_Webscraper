#include <iostream>
#include <string>

using namespace std;


int t, Map[3000],l,n;
char s[3000];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    Map['a'] = 'y';
    Map['b'] = 'h';
    Map['c'] = 'e';
    Map['d'] = 's';
    Map['e'] = 'o';
    Map['f'] = 'c';
    Map['g'] = 'v';
    Map['h'] = 'x';
    Map['i'] = 'd';
    Map['j'] = 'u';
    Map['k'] = 'i';
    Map['l'] = 'g';
    Map['m'] = 'l';
    Map['n'] = 'b';
    Map['o'] = 'k';
    Map['p'] = 'r';
    Map['q'] = 'z';
    Map['r'] = 't';
    Map['s'] = 'n';
    Map['t'] = 'w';
    Map['u'] = 'j';
    Map['v'] = 'p';
    Map['w'] = 'f';
    Map['x'] = 'm';
    Map['y'] = 'a';
    Map['z'] = 'q';
    
    
    
    
    
    
    scanf("%d\n",&t);
    int cnt = 0;
    while (t--)
    {
          cnt ++;
          gets(s);
          n = strlen(s);
          for (l=0; l<n; l++)
              if (s[l]!=' ') s[l] = Map[s[l]];
          printf("Case #%d: ", cnt);
          puts(s);
          
          
    }
}
