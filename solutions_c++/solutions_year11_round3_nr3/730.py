#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int main(){
    freopen("E.in","r",stdin);
    freopen("E.txt","w",stdout);
    int t,n,h,s,i,j,l,k;
    long long int e,d,mcm;
    bool b,c;
    int nota[10000];
    cin>>t;
    s=t;
    while(t>0){
               b=false;
               mcm=1;
               cin>>n>>l>>h;
               for(i=0;i<n;i++){
                                cin>>nota[i];
                                }
               for(i=l;(i<=h)&&!b;i++){
                                      c=true;
                                      for(j=0;j<n;j++){
                                                       if((i%nota[j]!=0)&&(nota[j]%i!=0)){
                                                                                          c=false;
                                                                                          j=n;}
                                                       }
                                      if(c){b=true;mcm=i;}
                                      }
               cout<<"Case #"<<s-t+1<<": ";
               if(b)cout<<mcm<<endl;
               else cout<<"NO"<<endl;
               t--;
               }
    }
