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

using namespace std;
vector<int>oran,blue;
vector<char>v;
deque<int>nar,azul;
int rp=1;

void doit(){
   v.clear();
   oran.clear();
   blue.clear();
   nar.clear();
   azul.clear();
   int n,x;
   char c;
   scanf("%d",&n);
  // cout<<n<<"tmr"<<endl;
   for(int i=0;i<n;++i){
      scanf(" %c %d",&c,&x);
      if(c=='O')oran.push_back(x);
      if(c=='B')blue.push_back(x);
      v.push_back(c);
   }
   scanf("\n");
   //crea colas
   int act=1,ct=0;
   for(int i=0;i<oran.size();++i){
      if(oran[i]>=act){
       ct=oran[i]-act;
       ct++;
       nar.push_back(ct);
       act=oran[i];
      }
      else{
         ct=act-oran[i];
         ct++;
         nar.push_back(ct);
         act=oran[i];
      }
   }
   
   act=1,ct=0;
   for(int i=0;i<blue.size();++i){
      if(blue[i]>=act){
       ct=blue[i]-act;
       ct++;
       azul.push_back(ct);
       act=blue[i];
      }
      else{
         ct=act-blue[i];
         ct++;
         azul.push_back(ct);
         act=blue[i];
      }
   }
   
   long long time=0;
   
   for(int i=0;i<v.size();++i){
      if(v[i]=='O'){
         if(nar[0]<=0){time++;}
         else {time+=nar[0];}
         if(!azul.empty()){
            if(nar[0]<=0){azul[0]--;}
            else {azul[0]-=nar[0];}   
         }
         nar.pop_front();
      }
      if(v[i]=='B'){
         if(azul[0]<=0){time++;}
         else {time+=azul[0];}
         if(!nar.empty()){
            if(azul[0]<=0){nar[0]--;}
            else {nar[0]-=azul[0];}   
         }
         azul.pop_front();
      }
   }
   
   printf("Case #%d: %lld\n",rp++,time);
   
}



int main(){
   int t;
   scanf("%d",&t);
   for(int i=0;i<t;++i){
      doit();
   }
}
