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

int isugly(lli n)
{
  if(n == 0)return 1;
  if(n < 0)n = -n;
  
  if(n % 2 == 0)return 1;
  if(n % 3 == 0)return 1;
  if(n % 5 == 0)return 1;
  if(n % 7 == 0)return 1;
  /*
  for(int i = 2;i <= 7;i++){
    if(n % i == 0)return 1;
  }
  */
  return 0;
}

int count(int *d, int c, int len, lli sum, lli ov, lli pm)
{
  if(c == len - 1){
    lli lsum = sum + pm * (ov * 10 + d[c]);
    return isugly(lsum);
  }else{
    int ct = 0;
    
    // +
    ct += count(d, c + 1, len, sum + pm * (ov * 10 + d[c]), 0LL, 1LL);
    
    // -
    ct += count(d, c + 1, len, sum + pm * (ov * 10 + d[c]), 0LL, -1LL);
    
    // ( ß„tß)
    ct += count(d, c + 1, len, sum, ov * 10 + d[c], pm);
    return ct;
  }
}

int main()
{
  int zz;
  std::cin >> zz;
  
  for(int oo = 0;oo < zz;oo++){
    char s[14];
    memset(s,0,14);
    std::cin >> s;
    int d[14];
    memset(d,0,sizeof(int)*14);
    
    int len = strlen(s);
    for(int i = 0;i < len;i++){
      d[i] = s[i] - '0';
    }
    
    int ct = count(d, 0, len, 0, 0LL, 1LL);
    
//    fprintf(stdout, "Case #%d\n", oo + 1);
    std::cout << "Case #" << (oo + 1) << ": " << ct << std::endl;
  }
  
  return 0;
}
