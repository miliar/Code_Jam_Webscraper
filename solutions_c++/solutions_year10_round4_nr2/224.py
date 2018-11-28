 #include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#define DEBUG(x) // cout<<#x<<" = "<<x<<"\n"
using namespace std;
int nP;
int P;


int M[13][1035];
bool B[13][1035];
int casc(int a, int b){
int ret = 0;
DEBUG("inc");
while(a<P+1)
  if( B[a][b]==0)
 { 
 B[a][b]=1;
 b/=2;
  a++;
  ret++;
}else break;
DEBUG("outc");
return ret;
}



int doit(){
int ret = 0;

for(int r = 1; r <= P; r++)
 for(int g = 0 ; g < (1<<(P-r)); g++)
   B[r][g]=0;

for(int r = 1; r <= P; r++){
  
  for(int g = 0 ; g < (1<<(P-r)); g++)
   if(!B[r][g])
   {
     if(M[r-1][2*g]==0||M[r-1][2*g+1]==0)
       ret+=casc(r,g);
     M[r][g]= (M[r-1][2*g]>M[r-1][2*g+1])?M[r-1][2*g+1]:M[r-1][2*g];
     M[r][g]--;
   }

}
return ret;

}




int main(){
    
int T;
cin>>T;
for(int t = 1; t<=T;t++ ){
       cout<<"Case #"<<t<<": ";
       cin>>P;
       int nP = 1<<P;
       
       for(int i =0 ; i < nP; i++)
        cin>>M[0][i];
       
       int price;
       DEBUG(nP-1);
       for(int i =0 ; i < nP-1; i++)
        cin>>price;
       DEBUG("a");
       
       int ret = doit();       
       DEBUG("b");
       cout<<price*ret<<"\n";

}




}
 
 
 
