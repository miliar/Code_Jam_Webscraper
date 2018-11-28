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

int s2(int x1,int y1,int x2,int y2,int x3,int y3)
{
  int xx0 = x2 - x1;
  int yy0 = y2 - y1;
  int xx1 = x3 - x1;
  int yy1 = y3 - y1;
  
  int ss2 = xx0 * yy1 - yy0 * xx1;
  if(ss2 < 0)ss2 = -ss2;
  return ss2;
}

int main()
{
  int zz;
  std::cin >> zz;
  
  for(int oo = 0;oo < zz;oo++){
    dad(int,n);
    dad(int,m);
    dad(int,a);
    
    int x1, y1;
    int x2,y2,x3,y3;
    int flag = 0;
    x1 = y1 = 0;
    
    for(x2 = 0;x2 <= n;x2++){
    for(y2 = 0;y2 <= m;y2++){
    for(x3 = x2;x3 <= n;x3++){
    for(y3 = 0;y3 <= m;y3++){
      if(s2(x1,y1,x2,y2,x3,y3) == a){
        flag = 1;
        goto FOUND;
      }
    }
    }
    }
    }
    
FOUND:
//    fprintf(stdout, "Case #%d\n", oo + 1);
    if(flag){
      std::cout << "Case #" << (oo + 1) << ": " << x1 << ' ' << y1 << ' ' << x2 << ' ' << y2 << ' ' << x3 << ' ' << y3 << std::endl;
    }else{
      std::cout << "Case #" << (oo + 1) << ": IMPOSSIBLE" << std::endl;
    }
  }
  
  return 0;
}
