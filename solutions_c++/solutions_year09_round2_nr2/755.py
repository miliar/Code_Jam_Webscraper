#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main( void )
{
 int T;
 cin>>T;
 for(int X=1;X<=T;++X){
  int K;
  cin>>K;
  vector<int> KK;
  while(K>0){KK.push_back(K%10);K/=10;}
  reverse(KK.begin(),KK.end());
  if(!next_permutation(KK.begin(),KK.end())){
   KK.push_back(0);
   sort(KK.begin(),KK.end());
   for(int i=0;i<KK.size();i++){
    if(KK[i]){
     int t=KK[0];KK[0]=KK[i];KK[i]=t;break;
    }
   }
  }
  K=0;
  for(int i=0;i<KK.size();i++){
   K=K*10+KK[i];
  }
  printf("Case #%d: %d\n",X,K);
 }
}

