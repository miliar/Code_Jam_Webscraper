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

char map[80][80];
int gm, gn;

int lim[11] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};

int cache[10][1025];
int col;

int rec(int y, int proh)
{
  if(y == -1){
    return 0;
  }
  
  int &ct = cache[y][proh];
  if(ct >= 0)return ct;
  
  int max = 0;
  for(int i = 0;i < lim[col];i++){
    if(i & proh)continue;
    int a[10];
    int xx = 0;
    int flag = 1;
    int count = 0;
    
    for(int cc = 1;cc < lim[col];cc <<= 1){
      if(i & cc){
        a[xx] = 1;
        if(map[y][xx] == 'x'){
          flag = 0;
          break;
        }
        count++;
      }else{
        a[xx] = 0;
      }
      xx++;
    }
    if(!flag)continue;
    
    int proh = 0;
    for(int j = 0;j < col;j++){
      if(!a[j])continue;
      if(j >= 1 && a[j - 1] == 1){flag = 0;break;}
      if(j < col - 1 && a[j + 1] == 1){flag = 0;break;}
      if(j - 1 >= 0)proh |= (1 << (j - 1));
      if(j + 1 < col)proh |= (1 << (j + 1));
    }
    if(!flag)continue;
//    err(i << " " << proh << " " << rec(y - 1, proh));
    int v = count + rec(y - 1, proh);
    if(v > max)max = v;
  }
  ct = max;
  return ct;
}

int main()
{
  int zz;
  std::cin >> zz;
  char seat[80][80];
  
  for(int oo = 0;oo < zz;oo++){
    err(oo);
    dad(int,m);
    dad(int,n);
    gm = m;
    gn = n;
    for(int i = 0;i < m;i++){
      fscanf(stdin,"%s",&seat[i][0]);
//      fprintf(stderr,"%s\n",&seat[i][0]);
    }
    memset(cache, 0xff, sizeof(cache));
    
    memcpy(&map[0][0], &seat[0][0], sizeof(seat));
    col = n;
    
//    fprintf(stdout, "Case #%d\n", oo + 1);
    std::cout << "Case #" << (oo + 1) << ": " << rec(m - 1, 0) << std::endl;
  }
  
  return 0;
}
