#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <assert.h>
#include <limits.h>
#include <bitset>

#define inita(type,a,b) type a[b];memset(a,0,sizeof(a));
#define initad(type,a,b) type *a = new type[b];memset(a,0,sizeof(a));
#define inita2(type,a,b,c) type a[b][c];memset(&a[0][0],0,sizeof(a));
#define initad2(type,a,b,c) type **a = new type*[b];for(int qq = 0;qq < b;qq++){a[qq] = new type[c];memset(a[qq],0,sizeof(type)*c);}
#define freed2(a,b) for(int qq = 0;qq < b;qq++){delete[] a[qq];}delete[] a;

#define err(a) std::cerr << a << std::endl;
#define erra(a,b) for(int xx = 0;xx < b;xx++){std::cerr << xx << '\t' << a[xx] << std::endl;}

#define readl(a,b) std::cin.getline(a,b);
#define set0(a) memset(a,0,sizeof(a));
#define dad(type,a) type a;std::cin >> a;
#define lli long long int

int rx[10];
int ry[10];
int gh;
int gw;
int gr;

lli cache[101][101];

lli count(int x, int y)
{
  if(x == gw && y == gh)return 1;
  if(x >= gw)return 0;
  if(y >= gh)return 0;
  for(int i = 0;i < gr;i++){
    if(x == rx[i] && y == ry[i])return 0;
  }
  
  lli& ct = cache[x][y];
  if(ct >= 0L)return ct;
  ct = count(x + 2, y + 1) + count(x + 1, y + 2);
  
  return ct;
}

int main()
{
  int zz;
  std::cin >> zz;
  
  for(int oo = 0;oo < zz;oo++){
    err(oo);
    dad(int,h);
    dad(int,w);
    dad(int,r);
    gh = h;
    gw = w;
    gr = r;
    for(int i = 0;i < r;i++){
      std::cin >> ry[i] >> rx[i];
    }
    memset(cache, 0xff, sizeof(lli) * 101 * 101);
    
//    fprintf(stdout, "Case #%d\n", oo + 1);
    std::cout << "Case #" << (oo + 1) << ": " << (count(1, 1) % 10007L) << std::endl;
  }
  
  return 0;
}
