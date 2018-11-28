#include<iostream>
#include<cmath>
#include<string>
using namespace std;
const int Maxn=210;
string s[Maxn][Maxn],ss[Maxn];
int tot[Maxn],len,total,T,n,m;
void Init(){
     int i;
     string st;
     //for (i=0;i<Maxn;i++)
     //for (int j=0;j<Maxn;j++)
     //s[i][j]="";
     cin>>n>>m;
     for (i=1;i<Maxn;i++) tot[i]=0;
     for (i=1;i<=n;i++){
         cin>>st;
         while (st!=""){
               if (st[0]=='/'){
                  s[i][++tot[i]]="";
               }else
               s[i][tot[i]]=s[i][tot[i]]+st[0];
               st.erase(0,1);
         }
     }
}
int work(){
    int now,i,j;
    now=len;
    for (i=1;i<=n;i++){
        j=0;
        while (j<len && (ss[j+1]==s[i][j+1])) j++;
        if (len-j<now) now=len-j;
    }
    return now;
}
void solve(){
     int Ans,i;
     string st;
     Ans=0;
     while (m--){
           cin>>st;
           len=0;
           while (st!=""){
                 if (st[0]=='/'){
                    ss[++len]="";
                 }else
                 ss[len]=ss[len]+st[0];
                 st.erase(0,1);
           }
           Ans+=work();
           tot[++n]=len;
           for (i=1;i<=len;i++){
               s[n][i]=ss[i];
           }
     }
     cout<<Ans<<endl;
}
int main(){
freopen("1.in","r",stdin);
freopen("1.out","w",stdout);
    cin>>T;
    for (int t=1;t<=T;t++){
          if (t==47){
          int j=0;
          j=1;
          j=2;
          }
          cout<<"Case #"<<t<<": ";
          Init();
          solve();
          
    }
    return 0;
}
