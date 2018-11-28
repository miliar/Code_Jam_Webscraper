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

int inc(int *a, int n)
{
  int p, q, i, j;
  
  // search top
  for(p = n - 2;p >= 0 && a[p] > a[p + 1];p--);
  if(p == -1)return -1;
  
  // search new top
  for(q = n - 1;a[p] > a[q];q--);
  int d = a[p];
  a[p] = a[q];
  a[q] = d;
  
  // reverse
  for(i = p + 1, j = n - 1;i < j;i++, j--){
    d = a[i];
    a[i] = a[j];
    a[j] = d;
  }
  return p;
}

void perm(char *dst, char *str, int *fact, int k)
{
  int len = strlen(str);
  assert(len % k == 0);
  memset(dst,0,len + 1);
  for(int i = 0;i < len;i+=k){
    for(int j = 0;j < k;j++){
      dst[i + j] = str[i + fact[j]];
    }
  }
}

int countblock(char *src)
{
  int ct = 0;
  char c = '\0';
  for(char *p = src;*p;p++){
    if(*p != c){
      ct++;
      c = *p;
    }
  }
  return ct;
}

int main()
{
  int zz;
  std::cin >> zz;
  char str[50001];
  char dst[50001];
  
  for(int oo = 0;oo < zz;oo++){
    dad(int,k);
    memset(str,0,sizeof(str));
    std::cin >> str;
    
    int fact[5];
    for(int i = 0;i < k;i++){
      fact[i] = i;
    }
    
    int len = strlen(str);
    int min = len;
    while(1){
      perm(dst,str,fact,k);
      /*
      if(strlen(str) != strlen(dst)){
        ERR(str);
        ERR(dst);
      }
      */
//      assert(strlen(str) == strlen(dst));
      int v = countblock(dst);
      if(v < min)min = v;
      
//      DA(fact,k);
//      std::cerr << std::endl;
      if(inc(fact,k) == -1)break;
    }
    
//    fprintf(stdout, "Case #%d\n", oo + 1);
    std::cout << "Case #" << (oo + 1) << ": " << min << std::endl;
  }
  
  return 0;
}
