#include <cstdio>
#include <cstring>
using namespace std;

int zestawy, what[200];
char tab[200];

int main()
{
  scanf("%d", &zestawy);
  for(int z=0; z<zestawy; ++z)
  {
    for(int i='0'; i<='z'; ++i) what[i]=-1;
    scanf("%s", tab);
    int len=strlen(tab);
    what[tab[0]]=1;
    int i=1, base=2;
    for(; i<len; ++i)
      if(what[tab[i]]==-1) {what[tab[i]]=0; break;}
    for(; i<len; ++i)
      if(what[tab[i]]==-1) what[tab[i]]=base++;
    unsigned long long wynik=0, mnoznik=1;
    for(int i=len-1; i>=0; --i)
    {
      wynik+=mnoznik*what[tab[i]];
      mnoznik*=(unsigned long long)base;
    }
    printf("Case #%d: %llu\n", z+1, wynik);
  }
  return 0;
}
