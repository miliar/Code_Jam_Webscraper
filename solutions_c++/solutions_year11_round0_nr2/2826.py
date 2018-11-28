#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int main(){
    freopen("B.in","r",stdin);
    freopen("B.txt","w",stdout);
    int t,n,c,d,i,j,k,l,s;
    char a[101],b[101],op[28][3],co[36][4];
    bool v;
    scanf("%d",&t);
    s=t;
    while(t>0){
               cin>>c;
               for(i=0;i<c;i++)cin>>co[i];
               cin>>d;
               for(i=0;i<d;i++)cin>>op[i];
               cin>>n;
               cin>>a;
               k=0;
               b[0]=a[0];
               for(i=1;i<n;i++){
                                  v=true;
                                  if(k>=0){
                                  for(j=0;j<c;j++){
                                                   if(((b[k]==co[j][0])&&(a[i]==co[j][1]))||((a[i]==co[j][0])&&(b[k]==co[j][1]))){
                                                                                                                                  v=false;
                                                                                                                                  b[k]=co[j][2];
                                                                                                                                  j=c;
                                                                                                                                  }
                                                   }
                                  }
                                  if(v){
                                        k++;
                                        b[k]=a[i];
                                        for(l=0;l<=k;l++){
                                                         for(j=0;j<d;j++){
                                                                          if(((b[l]==op[j][1])&&(a[i]==op[j][0]))||((b[l]==op[j][0])&&(a[i]==op[j][1]))){
                                                                                                                                                         k=-1;
                                                                                                                                                         j=d;
                                                                                                                                                         }
                                                                         }
                                                        }
                                       }    
                                  }
               cout<<"Case #"<<s-t+1<<": [";
               for(i=0;i<k;i++){
                                cout<<b[i]<<", ";
                                }
               if(k==-1){
                         cout<<"]"<<endl;}
               else{
               cout<<b[k]<<"]"<<endl;}
               t--;
               }
    }
