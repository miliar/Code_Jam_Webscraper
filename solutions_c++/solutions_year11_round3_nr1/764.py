#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int main(){
    freopen("D.in","r",stdin);
    freopen("D.txt","w",stdout);
    int t,r,c,s,i,j;
    bool b;
    char a[60][60];
    cin>>t;
    s=t;
    while(t>0){
               cin>>r>>c;
               for(i=0;i<r;i++){
                                cin>>a[i];
                                }
               cout<<"Case #"<<s-t+1<<":"<<endl;
               b=true;
               for(i=0;i<r;i++){
                                for(j=0;j<c;j++){
                                                 if(a[i][j]=='#'){
                                                                 a[i][j]='/';
                                                                 if(a[i][j+1]=='#'){
                                                                                   a[i][j+1]=92;
                                                                                   }
                                                                 else b=false;
                                                                 if(a[i+1][j]=='#'){
                                                                                   a[i+1][j]=92;
                                                                                   }
                                                                 else b=false;
                                                                 if(a[i+1][j+1]=='#'){
                                                                                     a[i+1][j+1]='/';
                                                                                     }
                                                                 else b=false;
                                                                 }
                                                 }
                                }
               if(!b)cout<<"Impossible"<<endl;
               if(b){
                     for(i=0;i<r;i++){
                                      cout<<a[i]<<endl;
                                      }
                     }
               t--;
               }
    }
