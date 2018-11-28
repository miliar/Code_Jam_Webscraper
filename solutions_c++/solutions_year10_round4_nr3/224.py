#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#define DEBUG(x) cout<<#x<<" = "<<x<<"\n"
using namespace std;

struct rect{
 int x1;
 int x2;
   int y1;
   int y2;
};

rect ret[1002];
int pai[1002];
int tam[1002];

void ufini(){
     
     for(int i =0; i < 1002;i++){
       pai[i]=i;
       tam[i]=1;
       }
     }

int FIND(int a){
if( pai[a]==a) return a;
return pai[a]=FIND(pai[a]);
}

void UNION(int a, int b){
  int pa= FIND(a);
  int pb = FIND(b);
  if(pa==pb) return;
  if(tam[pa]>tam[pb]){
  pai[pb]=pa;
  tam[pa]+=tam[pb]; 
   }else{
   pai[pa]=pb;
   tam[pb]+=tam[pa];   
   }
}
int R;
bool intersect(rect a, rect b){
//LEFT OF A
if( b.x2 +1< a.x1  ) return false;
//RIGHT
if( b.x1-1>a.x2  ) return false;
//UP
if( b.y2+1<a.y1  ) return false;
//DOWN
if( b.y1-1>a.y2  ) return false;

//TL
if( b.x2+1 == a.x1&&b.y2+1==a.y1  ) return false;

//BR
if( b.x1-1==a.x2 && b.y1-1 == a.y2  ) return false;
return true;
}


int getSurTime(int a){
int mx=10000000;
int my=10000000;
int MX=-1;
int MY=-1;
int md = 100000000;
for(int r = 0; r < R ; r++)
  if(FIND(r)==FIND(a)){
             
             if(ret[r].x1<mx)
                mx=ret[r].x1;
             if(ret[r].y1<my)
                my=ret[r].y1;
             
             if(ret[r].y2>MY)
                MY=ret[r].y2;
             if(ret[r].x2>MX)
                MX=ret[r].x2;
                
             if(ret[r].y1+ret[r].x1<md)
                md=ret[r].y1+ret[r].x1;
             }
  //DEBUG(MX);
  //DEBUG(MY);
  //DEBUG(mx);
  //DEBUG(my);
  //DEBUG(md);
    
  MX-=mx;
  MY-=my;
  md-=(mx+my);
  return MX+MY-md+1;

}

int main(){
 int T;
  cin>>T;
  for(int t = 1 ; t <= T ; t++){
          ufini();
          cout<<"Case #"<<t<<": ";
          cin>>R;
          for(int r = 0; r < R; r++)
           cin>>ret[r].x1>>ret[r].y1>>ret[r].x2>>ret[r].y2;   
          
          for(int r = 0; r < R; r++)
            for(int r2 = r+1; r2 < R; r2++)
             if(intersect(ret[r],ret[r2]))
                 UNION(r,r2);
          int MT = -1;
          for(int c = 0; c < R; c++)
              {
              int mt = getSurTime(c);
              if(mt>MT)MT=mt;
              }
          cout<<MT<<"\n";
          }



}
