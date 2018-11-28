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

#define MOD 1000000007LL

struct comp_first
{
  bool operator()(const std::pair<int,int>& p1,const std::pair<int,int>& p2)const
  {
    if(p1.first == p2.first)return p1.second < p2.second;
    return p1.first < p2.first;
  }
};

lli cted[1001];

lli count(lli *a, int m, int p)
{
  lli ct = 1LL;
  for(int i = p + 1;i < m;i++){
    if(a[p] < a[i]){
      /*
      ERR("p = " << p);
      ERR("i = " << i);
      ERR("cted = " << cted[i]);
      */
//      assert(cted[i] < 0LL);
      ct += cted[i] % MOD;
//      ct += count(a, m, i);
    }
  }
  return ct;
}

int main()
{
  int zz;
  std::cin >> zz;
  
  for(int oo = 0;oo < zz;oo++){
    memset(cted,0,sizeof(lli)*1001);
    dad(int,n);
    dad(int,m);
    dad(lli,x);
    dad(lli,y);
    dad(lli,z);
    lli a[1001];
    
    for(lli i = 0;i < m;i++){
      std::cin >> a[i];
    }
    for(lli i = m;i < n;i++){
      a[i] = (x * a[i - m] + y * (i - m + 1)) % z;
    }
    
//    DA(a,n);
    
    lli ct = 0LL;
//    ERR(n);
    for(int i = n - 1;i >= 0;i--){
      cted[i] = count(a,n,i) % MOD;
//      ERR(i << '\t' << cted[i]);
      ct += cted[i];
      /*
      if(oo == 0 && ct < 0LL){
        ERR(i);
      }
      */
      ct %= MOD;
    }
//    lli lct = ct % MOD;
    
//    fprintf(stdout, "Case #%d\n", oo + 1);
    std::cout << "Case #" << (oo + 1) << ": " << ct << std::endl;
  }
  
  return 0;
}
