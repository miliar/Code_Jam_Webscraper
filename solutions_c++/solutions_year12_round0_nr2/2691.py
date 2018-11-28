#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;


bool A[35][15];
bool B[35][15];
int tcase,n,s,p,sum[155];

void precompute(){
   memset(A,false,sizeof(A)); memset(B,false,sizeof(B));
   for(int a=0; a<=10; ++a) for(int b=0; b<=10; ++b)
    for(int c=0; c<=10; ++c){
       if(abs(a-b)>2 || abs(a-c)>2 || abs(b-c)>2) continue;
       bool suprising = false;
       if(abs(a-b)==2 || abs(a-c)==2 || abs(b-c)==2) suprising = true;
       if(!suprising) A[a+b+c][max(a,max(b,c))] = true;
      else B[a+b+c][max(a,max(b,c))] = true;
    }
   for(int i=0; i<=30; ++i) 
    for(int j=9; j>=0; --j) {
          A[i][j] |= A[i][j+1]; B[i][j] |= B[i][j+1];
     }
}
int main(){
  precompute();
  scanf("%d",&tcase);
  for(int tc=1; tc<=tcase; ++tc){
     scanf("%d %d %d",&n,&s,&p); int a,b; a = b = 0;
     for(int i=0; i<n; ++i){
        int x; scanf("%d",&x); 
        if(x==0 && p<=0) ++a; 
        else if(x==1 && p<=1) ++a;
        else if(x==29 || x==30) ++a;
        else if(A[x][p]) ++a;
        else if(B[x][p]) ++b;   
     } 
     int res = a+min(b,s); 
     printf("Case #%d: %d\n",tc,res);
  }
  return 0;
}
