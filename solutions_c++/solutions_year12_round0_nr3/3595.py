#include<iostream>
#include<cstdio>
#define MAX 1000
using namespace std;

int main(){
    int i,j,t,a,b,x,y,k1,k2,c,z,k3,t1,t2,cas=1;;
    bool f[MAX+1];
    scanf("%d",&t);
    while (t--){
          scanf("%d%d",&t1,&t2);
          c=0;
          a=max(t1,12);
          b=min(t2,99);
          for (x=0;x<10;++x){
              for (y=0;y<10;++y){
                  k1=10*x+y;
                  k2=10*y+x;
                  if (k1>=a && k1<=b && k2>=a && k2<=b && k1<k2){++c;}//cout<<k1<<" "<<k2<<endl;}
                  }
              }
          a=max(t1,101);
          b=min(t2,999);
          for (i=0;i<MAX;++i)f[i]=true;
          for (x=0;x<10;++x){
              for (y=0;y<10;++y){
                  for (z=0;z<10;++z){
                      k1 = 100*x+10*y+z;
                      k2 = 100*z+10*x+y;
                      k3 = 100*y+10*z+x;
                      if (k1>=a && k1<=b && k2>=a && k2<=b && k1!=k2 && (f[k1]&f[k2]) ){++c;}//cout<<c<<" -> "<<k1<<" "<<k2<<endl;}
                      if (k1>=a && k1<=b && k3>=a && k3<=b && k1!=k3 && (f[k1]&f[k3]) ){++c;}//cout<<c<<" -> "<<k1<<" "<<k3<<endl;}
                      if (k2>=a && k2<=b && k3>=a && k3<=b && k2!=k3 && (f[k2]&f[k3]) ){++c;}//cout<<c<<" -> "<<k2<<" "<<k3<<endl;}
                      f[k1]=false;
                      f[k2]=false;
                      f[k3]=false;
                      }
                  }
              }
          //cout<<c<<endl;
          printf("Case #%d: %d\n",cas,c);
          ++cas;
          }
    
    return 0;
    }
