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

int getroot(int *leaf,int *gate, int m)
{
  for(int i = (m - 1) / 2 - 1;i >= 0;i--){
    if(gate[i] == 1){
      leaf[i] = leaf[2 * i + 1] & leaf[2 * i + 2];
    }else{
      leaf[i] = leaf[2 * i + 1] | leaf[2 * i + 2];
    }
  }
  return leaf[0];
}

#define OUT 99999

int rec2(int *leaf, int *gate, int *cable,int m,int pos)
{
  if(pos >= (m + 1) / 2 - 1){
    return OUT;
  }
  
  int lp = leaf[pos];
  int ll = leaf[2 * pos + 1];
  int lr = leaf[2 * pos + 2];
  if(cable[pos] == 1){
    if(lp == 0){
      if(gate[pos] == 0){
        int a = rec2(leaf,gate,cable,m,2 * pos + 1);
        int b = rec2(leaf,gate,cable,m,2 * pos + 2);
        return MIN(a,b);
      }else{
        if(ll == 0 && lr == 0){
          int a = rec2(leaf,gate,cable,m,2 * pos + 1);
          int b = rec2(leaf,gate,cable,m,2 * pos + 2);
          return MIN(a,b) + 1;
        }else{
          return 1;
        }
      }
    }else{
      if(gate[pos] == 0){
        if(ll == 1 && lr == 1){
          int a = rec2(leaf,gate,cable,m,2 * pos + 1);
          int b = rec2(leaf,gate,cable,m,2 * pos + 2);
          return MIN(a,b) + 1;
        }else{
          return 1;
        }
      }else{
        int a = rec2(leaf,gate,cable,m,2 * pos + 1);
        int b = rec2(leaf,gate,cable,m,2 * pos + 2);
        return MIN(a,b);
      }
    }
  }else{
    if(lp == 0){
      if(gate[pos] == 0){
        int a = rec2(leaf,gate,cable,m,2 * pos + 1);
        int b = rec2(leaf,gate,cable,m,2 * pos + 2);
        return MIN(a,b);
      }else{
        int ret = 0;
        if(ll == 0)ret += rec2(leaf,gate,cable,m,2 * pos + 1);
        if(lr == 0)ret += rec2(leaf,gate,cable,m,2 * pos + 2);
        return ret;
      }
    }else{
      if(gate[pos] == 0){
        int ret = 0;
        if(ll == 1)ret += rec2(leaf,gate,cable,m,2 * pos + 1);
        if(lr == 1)ret += rec2(leaf,gate,cable,m,2 * pos + 2);
        return ret;
      }else{
        int a = rec2(leaf,gate,cable,m,2 * pos + 1);
        int b = rec2(leaf,gate,cable,m,2 * pos + 2);
        return MIN(a,b);
      }
    }
  }
}


int main()
{
  int zz;
  std::cin >> zz;
  
  for(int oo = 0;oo < zz;oo++){
    dad(int,m);
    dad(int,v);
    
    int leaf[10000];
    int gate[10000];
    int cable[10000];
    memset(leaf,0,sizeof(leaf));
    memset(gate,0,sizeof(gate));
    memset(cable,0,sizeof(cable));
    
    for(int i = 0;i < (m - 1) / 2;i++){
      std::cin >> gate[i];
      std::cin >> cable[i];
    }
    
    for(int i = 0;i < (m + 1) / 2;i++){
      std::cin >> leaf[i + (m - 1) / 2];
    }
    
    int min;
    int root = getroot(leaf,gate,m);
    if(root != v){
      min = rec2(leaf,gate,cable,m,0);
    }else{
      min = 0;
    }
    
    if(min >= OUT){
      std::cout << "Case #" << (oo + 1) << ": IMPOSSIBLE" << std::endl;
    }else{
      std::cout << "Case #" << (oo + 1) << ": " << min << std::endl;
    }
  }
  
  return 0;
}
