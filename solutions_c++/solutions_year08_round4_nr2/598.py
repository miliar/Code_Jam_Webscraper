//#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)


int n,m;
long long goal;


long long t,t2;

long long  extended_gcd(long long a,long long b , long long &x,long long &y){
    if (b==0) {
      x=1; y=0;
      return a;
    }    
   else {
       t2=extended_gcd(b,a % b,x,y);
       t=x;
       x=y;
       y=t-(a / b) *y;
       return t2;
   }    
}
/*
readln(a,b,n);
  d:=extended_gcd(a,n,x,y);
  if b mod d<>0 then begin writeln('NO answer');  exit;end;
  e:=x*(b div d) mod n;
  if e<0 then e:=e+n;
  for i:=0 to d-1 do
     ans[i+1]:=(e+i*n div d) mod n;
  for i:=0 to d-1 do
    write(ans[i+1],' ');
  */  
    
bool finds;


int x2,y2,x3,y3,x4,y4;

long long min(long long a, long long b){
    if (a<b) return a;else return b;
}    

bool check( long long a, long long b )  {
        long long a1=0,b1=0,a2=a,b2,a3=b,b3,x1,y1;
        
        
        foru(b3,-m,m)
          foru(b2,-m,m) if (a*b3-b2*b==goal){
             
                     
           x1=min(min(a1,a2),a3);
           y1=min(min(b1,b2),b3);
           
            if (a1-x1<=n && a2-x1<=n && a3-x1<=n)
             if (b1-y1<=m && b2-y1<=m && b3-y1<=m) {
                    
                 x2=a1-x1;  x3=a2-x1; x4=a3-x1;
                 y2=b1-y1;  y3=b2-y1; y4=b3-y1;
                 return true;
             }   


           if (a1-x1<=m && a2-x1<=m && a3-x1<=m)
             if (b1-y1<=n && b2-y1<=n && b3-y1<=n) {
                    
                 y2=a1-x1;  y3=a2-x1; y4=a3-x1;
                 x2=b1-y1;  x3=b2-y1; x4=b3-y1;
                 return true;
             }
              
          }   
          return false; 
/*
        if (a==0 || b==0) {
            if (a==0 && b==0) return false;
            if (a==0){
                if (goal % b!=0) return false;
                b3=0;
                b2= -goal / b;
            }
            else {
               if (goal % a!=0) return false;
               b2=0;
               b3=goal / a;    
            }        
           x1=min(min(a1,a2),a3);
           y1=min(min(b1,b2),b3);
           
            if (a1-x1<=n && a2-x1<=n && a3-x1<=n)
             if (b1-y1<=m && b2-y1<=m && b3-y1<=m) {
                    
                 x2=a1-x1;  x3=a2-x1; x4=a3-x1;
                 y2=b1-y1;  y3=b2-y1; y4=b3-y1;
                 return true;
             }   


           if (a1-x1<=m && a2-x1<=m && a3-x1<=m)
             if (b1-y1<=n && b2-y1<=n && b3-y1<=n) {
                    
                 y2=a1-x1;  y3=a2-x1; y4=a3-x1;
                 x2=b1-y1;  x3=b2-y1; x4=b3-y1;
                 return true;
             }
       }    
    
        long long x,y,i;
        long long d=extended_gcd(a,b,x,y);
        
//        if (d==0) return false;
        
        if (goal % d!=0) return false;
        long long e=x*(goal / d) % b;
        

           
             
        rep(i,d){
           b3=(e+ b*i / d) % b;   
           b2=(b3*a  - goal) / b;
           
           
           x1=min(min(a1,a2),a3);
           y1=min(min(b1,b2),b3);
           
           if (a1-x1<=n && a2-x1<=n && a3-x1<=n)
             if (b1-y1<=m && b2-y1<=m && b3-y1<=m) {
                    
                 x2=a1-x1;  x3=a2-x1; x4=a3-x1;
                 y2=b1-y1;  y3=b2-y1; y4=b3-y1;
                 return true;
             }   


           if (a1-x1<=m && a2-x1<=m && a3-x1<=m)
             if (b1-y1<=n && b2-y1<=n && b3-y1<=n) {
                    
                 y2=a1-x1;  y3=a2-x1; y4=a3-x1;
                 x2=b1-y1;  x3=b2-y1; x4=b3-y1;
                 return true;
             }
        }    
        return false;
        
        */
}    

int main(){
    freopen("binput3.in","r",stdin);
    freopen("output3.txt","w",stdout);
    int i,j,k,test,cases;
    
    cases=0;
    scanf("%d",&test);
    while (test){
        test--; cases++;
        scanf("%d%d%d",&n,&m,&j);
        goal=j;
        
        
        
        
        finds=false;
        foru(i,0,n)  if (finds) break; else
          foru(j,i,n) {
              if (check(i,j)) {finds=true; break;}
          }    
        if (finds)
        printf("Case #%d: %d %d %d %d %d %d\n",cases,x2,y2,x3,y3,x4,y4);
        else 
        printf("Case #%d: IMPOSSIBLE\n",cases);
    }
    return 0;
}
