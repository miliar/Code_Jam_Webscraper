#include<math.h>
#include<iostream>
#include<stdio.h>
using namespace std;
int sum(){
    }

int main(){
    freopen("C.in","r",stdin);
    freopen("C.txt","w",stdout);
    int a[1000],c,t,s,n,i,j,f,g,l,h,m,sum,max,aux;
    scanf("%d",&t);
    s=t;
    while(t>0){
               max=sum=0;
               cin>>n;
               g=pow(2,n-1);
               for(i=0;i<n;i++){
                                cin>>a[i];
                                sum=sum+a[i];
                                }
               for(i=1;i<g;i++){
                                aux=i;
                                l=h=m=0;
                                for(j=0;j<n;j++){
                                                 if((aux%2)==0){
                                                                  l=l^a[j];
                                                                  m=m+a[j];}
                                                 else{
                                                      h=h^a[j];}
                                                      
                                                 aux=aux>>1;
                                                 }
                                if(h==l){
                                         if(m>max)max=m;
                                         m=sum-m;
                                         if(m>max)max=m;
                                         }
                                }
               if(max>0){
                         cout<<"Case #"<<s-t+1<<": "<<max<<endl;}
               else{
                    cout<<"Case #"<<s-t+1<<": NO"<<endl;}
               t--;
               }
    }
