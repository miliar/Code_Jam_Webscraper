#include <cstdio>
#include <map>
#include <cstring>
#include <string>

using namespace std;

int main(void)
{
  std::map<char, char> m;

  m['a'] = 'y';
  m['b'] = 'h';
  m['c'] = 'e';
  m['d'] = 's';
  m['e'] = 'o';
  m['f'] = 'c';
  m['g'] = 'v';
  m['h'] = 'x';
  m['i'] = 'd';
  m['j'] = 'u';
  m['k'] = 'i';
  m['l'] = 'g';
  m['m'] = 'l';
  m['n'] = 'b';
  m['o'] = 'k';
  m['p'] = 'r';
  m['q'] = 'z';
  m['r'] = 't';
  m['s'] = 'n';
  m['t'] = 'w';
  m['u'] = 'j';
  m['v'] = 'p';
  m['x'] = 'm';
  m['w'] = 'f';
  m['y'] = 'a';
  m['z'] = 'q';
  m[' '] = ' ';
  m['\n'] = '\n';
  int t;
  char linha[1024];
  
  fgets(linha, sizeof(linha), stdin);
  sscanf(linha, "%d", &t);
  
  for(int z(0); z < t; ++z)
  {
    printf("Case #%d: ",z+1);
    fgets(linha, sizeof(linha), stdin);
    for(int x(0); x < strlen(linha); ++x)
    {
      printf("%c", m[linha[x]]);
    }
  }
  
  return 0;
}