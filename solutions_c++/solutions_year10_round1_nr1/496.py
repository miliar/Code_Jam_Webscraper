#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <climits>
#include <sstream>

using namespace std;
#define MAXN 1000

char B[MAXN][MAXN];
int N,K,T;
bool red,blue;

void rotate(){
  
   char A[MAXN][MAXN];
   int j=0;
   for(int i=N-1;i>=0;--i){
     for(int k=0;k<N;++k) A[k][j]=B[i][k];
     ++j;
   }
   memcpy(B,A,sizeof(A));
   return;
  
}
void gravity(){
 
  for(int i=0;i<N;++i){  
    
    
    for(int k=N-1;k>=0;--k){
      
       bool vl = false;
       for(int j=0;j<k;++j) if(B[j][i]!='.') vl = true;
       if(!vl) continue;
   
      
      while(B[k][i]=='.'){
       for(int j=k;j>0;--j)
        B[j][i]=B[j-1][i];
       B[0][i]='.';
      }  
    }
  } 
  return;
  
}

void print(){

 for(int i=0;i<N;++i)
 {
   for(int j=0;j<N;++j)
   cout<<B[i][j];
  cout<<endl;
 }

}

void check(int i,int j,char v){
  
  int ct1,ct2,ct3,ct4;
  ct1=ct2=ct3=ct4=0;
  
  for(int a=0;a<K;++a){
    if(j+a<N && B[i][j+a]==v) ct1++;
    if(i+a<N && B[i+a][j]==v) ct2++;
    if(i+a<N && j+a<N && B[i+a][j+a]==v) ct3++;
    if(i+a<N && j-a>=0 && B[i+a][j-a]==v) ct4++;
  }
  
  if(ct1==K || ct2==K || ct3==K ||ct4==K){
    if(v=='R') red = true;
    else blue = true;
  }  
    
}

int main(){
  
  freopen("A-large.in","r",stdin);
  freopen("out.txt","w",stdout);
    
  cin>>T;
  for(int i=1;i<=T;++i){
     
     cin>>N>>K;
     
     
     for(int j=0;j<N;++j)
      cin>>B[j];
     
    // for(int j=0;j<N;++j)
    //  cout<<B[j]<<endl;
    rotate();
    // print();
    // cout<<"------------"<<endl;
     gravity();
    // print();
     red = false;
     blue = false;
     
     for(int j=0;j<N;++j)
      for(int k=0;k<N;++k){
        check(j,k,'R');
        check(j,k,'B'); 
      }
    
    cout<<"Case #"<<i<<": ";
    if(red && blue) cout<<"Both"<<endl;
    else if(red) cout<<"Red"<<endl;
    else if(blue) cout<<"Blue"<<endl;
    else cout<<"Neither"<<endl;
  }     

  return 0;
}
