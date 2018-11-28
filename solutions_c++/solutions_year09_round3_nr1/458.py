#include <cstdio>
#include <cstring>
#include <ctype.h>
#include <map>
using namespace std;

long long dec(char * line)
{
  int len = strlen(line);
  int *tab = new int[len];

  map<char, int> mapa;
  mapa[line[0]] = 1;

  int k = 0;

  for(int i=0;i<len;++i)
  {
    if(mapa.find(line[i]) == mapa.end())
    {
      mapa[line[i]] = k;
      k += k == 0 ? 2 : 1;
    }

    tab[i] = mapa[line[i]];
  }

  int max = 0;
  for(int i=0;i<len;++i)
    if(tab[i] > max)
      max = tab[i];

  ++max;

  int mn = 1;
  long long res = 0;
  for(int i=len-1;i>=0;--i)
  {
    res += tab[i] * mn;
    mn *= max;
  }

  delete [] tab;

  return res;
}

int main()
{
  char line[80];
  int n;
  scanf("%d\n", &n);

  for(int i=0;i<n;++i)
  {
    long long res = 9000000000000000000ll;
    gets(line);
    printf("Case #%d: %lld\n", i + 1, dec(line));
  }
}

