#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int main(){
    freopen("A.in","r",stdin);
    freopen("A.txt","w",stdout);
    int t,n,i,s,bl,ora,bl1,or1,bl2,or2,aux,l;
    char b[101];
    int a[101];
    scanf("%d",&t);
    l=t;
    while(t>0){
               s=bl1=or1=or2=bl2=0;
               bl=ora=1;
               bool f=false;
               scanf("%d",&n);
               for(i=0;i<n;i++){
                                cin>>b[i];
                                cin>>a[i];
                                }
               for(i=0;i<n;i++){
                                if(b[i]=='O'){
                                              if(bl2>=abs(a[i]-ora)){
                                                                   aux=1;}
                                              else{
                                                   aux=abs(a[i]-ora)+1-bl2;}
                                              s=s+aux;
                                              bl2=0;
                                              or2=or2+aux;
                                              ora=a[i];
                                              }
                                if(b[i]=='B'){
                                              if(or2>=abs(a[i]-bl)){
                                                                   aux=1;}
                                              else{
                                                   aux=abs(a[i]-bl)+1-or2;}
                                              s=s+aux;
                                              or2=0;
                                              bl2=bl2+aux;
                                              bl=a[i];
                                              }
                                }
               cout<<"Case #"<<l-t+1<<": "<<s<<endl;
               t--;
               }
    }
