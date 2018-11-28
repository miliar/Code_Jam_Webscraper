/*
  Theme Park
  Author: Piotr Różański
  Compiler: GCC g++
*/

#include <cstdio>
#include <stdint.h>

struct Grupa
{
  int ilosc;
  int r;
  uint64_t euro;
  
  void czysc(void)
  {
    ilosc = 0;
    euro = 0;
    r = -1;
  }
};
  
Grupa grupy[1000];

int main(void)
{
  int T;
  scanf("%d",&T);
  for (int it=1; it<=T; ++it)
  {
    int R,K,N;
    uint64_t euro = 0;

    scanf("%d %d %d",&R,&K,&N);
    for (int i=0; i<N; ++i)
    {
      grupy[i].czysc();
      scanf("%d",&grupy[i].ilosc);
    }
    
    int poz=0, r=R;
    while (r > 0 && grupy[poz].r < 0)
    {
      grupy[poz].euro = euro;
      grupy[poz].r = r;
      int k=K, spoz=poz;
      while (k >= grupy[poz].ilosc)
      {
        k -= grupy[poz].ilosc;
        euro += grupy[poz].ilosc;
        if (++poz >= N) poz -= N;
        if (spoz == poz) break;
      }
      --r;
    }
    
    if (r > 0)
    {
      int dr = grupy[poz].r - r;
      euro += (euro - grupy[poz].euro) * (r / dr);
      r %= dr;
      while (r > 0)
      {
        int k=K, spoz=poz;
        while (k >= grupy[poz].ilosc)
        {
          k -= grupy[poz].ilosc;
          euro += grupy[poz].ilosc;
          if (++poz >= N) poz -= N;
          if (spoz == poz) break;
        }
        --r;
      }
    }
    
    printf("Case #%d: %llu\n", it, euro);
  }
}
