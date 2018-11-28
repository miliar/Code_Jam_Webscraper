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

#define INITA(type,a,b) type a[b];memset(a,0,sizeof(type)*b);
#define INITAD(type,a,b) type *a = new type[b];memset(a,0,sizeof(type)*b);
#define INITA2(type,a,b,c) type a[b][c];memset(&a[0][0],0,sizeof(type)*b*c);
#define INITAD2(type,a,b,c) type **a = new type*[b];for(int qq = 0;qq < b;qq++){a[qq] = new type[c];memset(a[qq],0,sizeof(type)*c);}
#define FREED2(a,b) for(int qq = 0;qq < b;qq++){delete[] a[qq];}delete[] a;
#define ERR(a) std::cerr << a << std::endl;
#define READL(a,b) std::cin.getline(a,b);
#define INIT(a,b) memset(a,0,b);
#define dad(type,a) type a;std::cin >> a;
#define MIN(a,b) ((a) > (b) ? (b) : (a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define DA(a,b) for(int xx = 0;xx < b;xx++){std::cerr << xx << '\t' << a[xx] << std::endl;}
#define lli long long int

struct comp_first
{
  bool operator()(const std::pair<int,int>& p1,const std::pair<int,int>& p2)const
  {
    if(p1.first == p2.first)return p1.second < p2.second;
    return p1.first < p2.first;
  }
};

int main()
{
  int zz;
  std::cin >> zz;
  
  for(int oo = 0;oo < zz;oo++){
    dad(int,p);
    dad(int,k);
    dad(int,l);
    
    lli ll[1000];
    for(int i = 0;i < l;i++){
      std::cin >> ll[i];
    }
    
    std::sort(ll, ll + l);
    
    lli ct = 0;
    lli pp = l - 1;
    lli j;
    for(lli f = 1;;f++){
      for(j = pp;j > pp - k && j >= 0;j--){
        ct += ll[j] * f;
      }
      pp = j;
      if(j == -1)break;
    }
    
    
//    fprintf(stdout, "Case #%d\n", oo + 1);
    std::cout << "Case #" << (oo + 1) << ": " << ct << std::endl;
  }
  
  return 0;
}
