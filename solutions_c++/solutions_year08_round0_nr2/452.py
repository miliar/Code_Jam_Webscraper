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
  int n;
  std::cin >> n;
  
  for(int t = 0;t < n;t++){
    int tt;
    std::cin >> tt;
    
    int na, nb;
    std::cin >> na >> nb;
    std::pair<int,int> tr[400];
    
    for(int i = 0;i < na * 2;i += 2){
      int a,b,c,d;
      fscanf(stdin,"%d:%d %d:%d",&a,&b,&c,&d);
      
      tr[i].first = a * 60 + b;
      tr[i].second = 2;
      
      tr[i + 1].first = c * 60 + d;
      tr[i + 1].second = 0;
    }
    
    for(int i = na * 2;i < (na + nb) * 2;i += 2){
      int a,b,c,d;
      fscanf(stdin,"%d:%d %d:%d",&a,&b,&c,&d);
      tr[i].first = a * 60 + b;
      tr[i].second = 3;
      
      tr[i + 1].first = c * 60 + d;
      tr[i + 1].second = 1;
    }
    int nab = (na + nb) * 2;
    
    std::sort(tr, tr + nab, comp_first());
    
    /*
    for(int i = 0;i < nab;i++){
      std::cout << tr[i].first << "\t" << tr[i].second << std::endl;
    }
    */
    
    int aaa = 0;
    int bbb = 0;
//    int aleft = 0;
//    int bleft = 0;
    std::queue<int> qa;
    std::queue<int> qb;
    
//    int prevta = -1000;
//    int prevtb = -1000;
    for(int i = 0;i < nab;i++){
      switch(tr[i].second){
      case 2:
        if(qa.empty() || qa.front() > tr[i].first){
          aaa++;
        }else{
          qa.pop();
        }
        break;
      case 0:
        qb.push(tr[i].first + tt);
        break;
      case 3:
        if(qb.empty() || qb.front() > tr[i].first){
          bbb++;
        }else{
          qb.pop();
        }
        break;
      case 1:
        qa.push(tr[i].first + tt);
        break;
      default: break;
      }
    }
    
    std::cout << "Case #" << (t + 1) << ": " << aaa << " " << bbb << std::endl;
    
  }
  
  return 0;
}
