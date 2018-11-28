#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
    freopen("F.in","r",stdin);
    freopen("F.txt","w",stdout);
    int t,i,j,c,s,l,n,sum,may,sum2,pos,may2,pos2;
    int a[1000];
    long long int ti;
    cin>>t;
    s=t;
    while(t>0){
               sum=sum2=may2=0;
               cin>>l>>ti>>n>>c;
               for(i=0;i<c;i++){
                                cin>>a[i];}
               for(i=0;i<n;i++){
                                sum=sum+a[i%c]*2;
                                }
               for(i=0;i<n;i++){
                                if((sum2+a[i%c]*2)>ti){
                                                      may=a[i%c]-(ti-sum2)/2;
                                                      pos=i;
                                                      i=n;
                                                      }
                                sum2=sum2+a[i%c]*2;
                                }
               if(l==1){
               for(i=pos+1;i<n;i++){
                                    if(a[i%c]>may){
                                                   may=a[i%c];
                                                   }
                                    }
               sum=sum-may;
               }
               if(l==2){
               for(i=pos+1;i<n;i++){
                                    if(a[i%c]>may2){
                                                   may2=a[i%c];
                                                   pos2=i;
                                                   }
                                    }
               sum=sum-may2;
               for(i=pos+1;i<n;i++){
                                    if((a[i%c]>may)&&(i!=pos2)){
                                                                may=a[i%c];
                                                                }
                                    }
               sum=sum-may;
               }
               cout<<"Case #"<<s-t+1<<": "<<sum<<endl;
               t--;
               }
    }

