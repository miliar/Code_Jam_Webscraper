#include <iostream>
#include <conio.h>
#include <fstream>
using namespace std;
int t,n,s,p;
int ti[4];
int a[4],b[4],c[4];
int cases;
int x=0;
main(){
       ifstream dobj("B-small-attempt0.in");
       ofstream pobj("op2.in");
       dobj>>t;
       while(dobj>>n>>s>>p){
       cases=0;
       x++;                     
       for(int i=1;i<=n;i++){
       dobj>>ti[i];
       if(ti[i]%3==0){
       a[i]=ti[i]/3;               
       b[i]=ti[i]/3;
       c[i]=ti[i]/3;
       }
       else if(ti[i]%3==1){
       a[i]=ti[i]/3+1;               
       b[i]=ti[i]/3;
       c[i]=ti[i]/3;
       }
       else if(ti[i]%3==2){
       a[i]=ti[i]/3+1;               
       b[i]=ti[i]/3+1;
       c[i]=ti[i]/3;     
       }

if(a[i]>=p)cases+=1;

        if(s!=0&&(a[i]<p)&&(p-a[i]==1)&&(ti[i]%3==0)){
                                                    a[i]+=1;
                                                    c[i]-=1;
                                                    if(c[i]>0){
                                                               cases+=1;
                                                               s-=1;}}
        if((s!=0)&&(a[i]<p)&&(p-a[i]==1)&&(ti[i]%3==2)){
        a[i]+=1;
        b[i]-=1;
        if(b[i]>0){
                   cases+=1;
                   s-=1;}}
                   }
                   pobj<<"Case #"<<x<<": "<<cases<<endl;}
       getch();                             
}
