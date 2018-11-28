#include<cstdio>
#include<algorithm>
#include<string>
#include<iostream>
#include<cstring>
using namespace std;
int a,b;
string tos(int a_){
    string s;
    while(a_){
        s+=(a_%10+'0');
        a_/=10;
    }

    int i,si=s.size();
    for(i=0;i<si/2;i++){
        char c=s[i];
        s[i]=s[si-1-i];
        s[si-i-1]=c;
    }
    return s;
}
bool iscy(int a_,int b_){
    string aa,bb;
    aa=tos(a_);
    bb=tos(b_);
    aa+=aa;
    int si=bb.size();
    //cout<<aa<<' '<<bb<<endl;
    for(int i=0;i<si;i++)
        if(aa.substr(i,si)==bb)
            return true;
    return false;
}
int main(){
    int t,i,j,k;
   // freopen("C-small-attempt0.in","r",stdin);
   //freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(k=1;k<=t;k++){
        scanf("%d %d",&a,&b);
        int cnt=0;
        for(i=a;i<=b;i++){
            for(j=i+1;j<=b;j++){
                if(i!=j && iscy(i,j)){
                   // cout<<i<<' '<<j<<endl;
                    cnt++;
                }
            }
        }
        printf("Case #%d: %d\n",k,cnt);
    }
}
