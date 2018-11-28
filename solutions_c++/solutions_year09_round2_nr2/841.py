#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int zestawy, z, i;
char tab[30];

int main()
{
  scanf("%d", &zestawy);
  for(int z=0; z<zestawy; ++z)
  {
    scanf("%s", tab);
    int dl=strlen(tab);
    int i=dl-2;
    for(; i>=0; --i)
      if(tab[i]<tab[i+1]) break;
    if(i<0)
    {
      tab[dl++]='0';
      tab[dl]=NULL;
      for(int j=dl-1; j>=0; --j)
        if(tab[j]!='0') {swap(tab[j], tab[0]); break;}
      sort(tab+1, tab+dl);
    }
    else
    {
      for(int j=dl-1; j>=0; --j)
        if(tab[j]>tab[i]) {swap(tab[j], tab[i]); break;}
      sort(tab+i+1, tab+dl);
    }
    printf("%s\n", tab);
  }
}
