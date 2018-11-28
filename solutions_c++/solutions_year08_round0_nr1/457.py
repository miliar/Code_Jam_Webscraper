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

int seek(int *att, int i, int e, int lim)
{
  for(;i < lim && att[i] != e;i++);
  return i == lim ? -1 : i;
}

int rec(int *att, int s, int q, int pos)
{
  if(pos == q)return 0;
  
  bool flag[100];
  memset(flag, 0, sizeof(bool)*100);
  for(int p = pos;p < pos + s - 1 && p < q;p++){
    flag[att[p]] = true;
  }
  
  int min = 1000;
  for(int i = 0;i < s;i++){
    if(flag[i])continue;
    
    int see = seek(att, pos, i, q);
    if(see == -1)return 0;
    
    int v = rec(att, s, q, see) + 1;
    if(v < min)min = v;
  }
  return min;
}

int main()
{
  int n;
  std::cin >> n;
  
  char **engine = new char *[100];
  for(int i = 0;i < 100;i++){
    engine[i] = new char[101];
    memset(engine[i], 0, 101);
  }
  
  char **query = new char *[1000];
  for(int i = 0;i < 1000;i++){
    query[i] = new char[101];
    memset(query[i], 0, 101);
  }

  for(int t = 0;t < n;t++){
    int ret,s,q;
    
    std::cin >> s;
//    std::cin >> query[999];
    char ddd[101];
    std::cin.getline(ddd, 100);
    for(int i = 0;i < s;i++){
//      fscanf(stdin,"%s",&engine[i]);
      std::cin.getline(engine[i],100);
//      std::cout << engine[i] << std::endl;
    }
    
    bool flag[100];
    memset(flag, 0, sizeof(bool) * 100);
    
    int att[1000];
    
    std::cin >> q;
    std::cin.getline(ddd, 100);
    for(int i = 0;i < q;i++){
      std::cin.getline(query[i],100);
      for(int j = 0;j < s;j++){
        att[i] = -1;
        if(!strcmp(engine[j], query[i])){
          flag[j] = true;
          att[i] = j;
          break;
        }
      }
    }
    
    int f;
    for(f = 0;f < s && flag[f];f++);
    if(f < s){
      ret = 0;
      goto XX;
    }
    
    ret = rec(att, s, q, 0);
    
XX:
    std::cout << "Case #" << (t + 1) << ": " << ret << std::endl;
    
  }
  
  return 0;
}
