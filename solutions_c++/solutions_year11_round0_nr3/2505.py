#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define inf 1<<30 

using namespace std;
int ct=1;


void doit(){
   int n,x;
   long long total=0;
   scanf("%d",&n);
   int xoro=0;
   int menor=inf;
   for(int i=0;i<n;++i){
      scanf("%d",&x);
      menor=min(menor,x);
      total+=x;
      xoro^=x;
   } 
   printf("Case #%d: ",ct++);
   
   if(xoro==0){
      printf("%lld\n",total-menor);
   }
   else{
      printf("NO\n");
   }

}


int main(){
   int t;
   scanf("%d",&t);
   for(int i=0;i<t;++i){
      doit();
   }
}

