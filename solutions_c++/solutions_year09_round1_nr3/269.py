#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#define all(v) v.begin(),v.end()
int c/*total*/,n/*subset*/,quan;
vector<int> poss;
typedef long double ld;
ld prob;
map<pair<int,int>,ld> memo;
ld solve(int x,ld pp,int pasos){
  ld sum=0;
  pair<int,int> par(x,pasos);
  ld aprox=pp*pasos;
  if(x==((1<<c)-1)) return aprox;
  
  if(pasos>500) return 0;
  if(memo.find(par)!=memo.end()) return memo[par];
  
  ld next=pp*prob;
  for(int i=0;i<quan;i++){
    int xx=x|poss[i];
    sum+=solve((1<<__builtin_popcount(xx))-1,next,pasos+1);
  }
  
  return memo[par]=sum;
}

void halla_poss(){
 poss.clear();
 memo.clear();
 vector<int> carts(c,0);
 for(int i=0;i<n;i++) carts[i]=1;
  reverse(all(carts));
  //for(int i=0;i<c;i++) cout<<carts[i]<<" ";cout<<endl;
  do{
   int x=0;
   for(int i=0;i<c;i++) if(carts[i]) x=x|(1<<i);
   poss.push_back(x);
   //cout<<x<<endl;
  }while(next_permutation(all(carts)));
 quan=poss.size();
 prob=1.0/quan;
}
int main(){
 int t;
 cin>>t;
 for(int tt=1;tt<=t;tt++){
 
  cin>>c>>n;
  if(n>c) n=c;
  
  halla_poss();
  double ret=solve(0,1,0);
   cout<<"Case #"<<tt<<": ";
   printf("%.07lf\n",ret);
 }
  
}

/*
Case #1: 12.2306572                                                                                                                                                       
Case #2: 1.0000000                                                                                                                                                        
Case #3: 14.1232619                                                                                                                                                       
Case #4: 7.7966391                                                                                                                                                        
Case #5: 2.1250000                                                                                                                                                        
Case #6: 5.4200506                                                                                                                                                        
Case #7: 2.3333333                                                                                                                                                        
Case #8: 6.5852573                                                                                                                                                        
Case #9: 1.0000000                                                                                                                                                        
Case #10: 3.2393209                                                                                                                                                       
Case #11: 6.4877106                                                                                                                                                       
Case #12: 3.0798319                                                                                                                                                       
Case #13: 4.6568359                                                                                                                                                       
Case #14: 3.8767361                                                                                                                                                       
Case #15: 14.6988965                                                                                                                                                      
Case #16: 1.0000000                                                                                                                                                       
Case #17: 1.0000000                                                                                                                                                       
Case #18: 1.0000000                                                                                                                                                       
Case #19: 1.0000000                                                                                                                                                       
Case #20: 8.6257576                                                                                                                                                       
Case #21: 9.0462130                                                                                                                                                       
Case #22: 3.0000000                                                                                                                                                       
Case #23: 18.1403624                                                                                                                                                      
Case #24: 2.2000000                                                                                                                                                       
Case #25: 1.0000000                                                                                                                                                       
Case #26: 4.9339809                                                                                                                                                       
Case #27: 11.4166166                                                                                                                                                      
Case #28: 2.1250000                                                                                                                                                       
Case #29: 5.3253968                                                                                                                                                       
Case #30: 1.0000000                                                                                                                                                       
Case #31: 2.1111111                                                                                                                                                       
Case #32: 5.5000000                                                                                                                                                       
Case #33: 1.0000000                                                                                                                                                       
Case #34: 2.2000000                                                                                                                                                       
Case #35: 2.6296296                                                                                                                                                       
Case #36: 11.4166166                                                                                                                                                      
Case #37: 1.0000000                                                                                                                                                       
Case #38: 1.0000000  
*/

