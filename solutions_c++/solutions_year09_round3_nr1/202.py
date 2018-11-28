#include <iostream>
#include <algorithm>
#include <map>
using namespace std;
char s[1000];
map <char,int> peta;
int d[100];
long long pangkat(int a,int b){
     long long tmp=1;
     for (int j=1;j<b;j++){
         tmp*=a;}
         
         return tmp;
     }
int main(){int T;

freopen("Ain.txt","r",stdin);
  freopen("A.out","w",stdout);
    scanf("%d",&T);
    for (int t=1;t<=T;t++){
    scanf("%s",s);
    peta=map <char,int> ();
    int x=strlen(s);
    peta[s[0]]=2;
    d[x]=2;
    int zzz=1;
    
    //cout<<d[x]-1;
    for (int i=1;i<x;i++){
        if (peta[s[i]]==0){
                           peta[s[i]]=zzz;
                           zzz++;
                           if (zzz==2)zzz++;
                           }
        d[x-i]=peta[s[i]];
    //    cout<<d[x-i]-1;
        
        }
        zzz--;
        zzz=max(zzz,2);
  //      cout<<zzz<<endl;
        long long ans=0;
        for (int i=1;i<=x;i++){
            ans+=((d[i]-1)*pangkat(zzz,i));
            
//cout<<d[i]-1<<" "<<           pangkat(zzz,i)<<endl;
 }
            cout<<"Case #"<<t<<": "<<ans<<endl;}
       // system("pause");
    
    }
