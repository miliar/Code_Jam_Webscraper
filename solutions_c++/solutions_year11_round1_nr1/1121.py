#include<iostream>
#include<string.h>
using namespace std;
int main(){
    freopen("A.in","r",stdin);
    freopen("A.txt","w",stdout);
    int i,t,n,pd,pg,j,s,l,len;
    bool p;
    char d[20];
    cin>>t;
    s=t;
    while(t>0){
               p=false;
               cin>>d>>pd>>pg;
               len=strlen(d);
               if(len>=3){if(((pd==100)||(pg!=100))&&((pd==0)||(pg!=0)))p=true;}
               else{
                    if(len==2)n=(d[0]-48)*10+d[1]-48;
                    if(len==1)n=d[0]-48;
               for(i=1;i<=n;i++){
                                 if((i*pd)%100==0){
                                                   j=i-i*pd/100;
                                                   l=i*pd;
                                                   if(((j==0)||(pg!=100))&&((l==0)||(pg!=0)))p=true;
                                                   }
                                 }
               }
               if(p)cout<<"Case #"<<s-t+1<<": Possible"<<endl;
               else cout<<"Case #"<<s-t+1<<": Broken"<<endl;
               t--;
               }
    }
