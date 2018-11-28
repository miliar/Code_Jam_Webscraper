#include <cstdio>
#include <map>
using namespace std;

bool isok(char *wz, int l, char *t)
{
  int r = 0;

  for(int c=0;c<l;++c)
  {
    bool ok = false;

    if(t[r] == '(')
    {
      while(t[r] != ')')
      {
        ok |= t[r] == wz[c];
        ++r;
      }
      ++r;
    }
    else
    {
      ok = wz[c] == t[r];
      ++r;
    }

    if(!ok)
      return false;
  }

  return true;
}

int main()
{
  char tmp[5000000];
  int l, d, n;
  scanf("%d%d%d", &l, &d, &n);

  char ** dict = new char * [d];
  for(int i=0;i<d;++i)
  {
    dict[i] = new char[l+1];
    scanf(" %s", dict[i]);
  }

  for(int i=0;i<n;++i)
  {
    scanf(" %s", tmp);
    int licznik = 0;
    for(int k=0;k<d;++k)
      licznik += isok(dict[k], l, tmp);

    printf("Case #%d: %d\n", i+1, licznik);
  }

  return 0;
}

