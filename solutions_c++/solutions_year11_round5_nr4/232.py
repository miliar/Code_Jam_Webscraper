#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;

typedef long long LL;

LL pow2[65];
LL sum,ans;
char s[100000],anss[100000];

void check(){
     LL t=(LL)sqrt(sum);
     LL tt=t*t;
     if (tt==sum) {
        ans=t;
        for (int i=0;i<strlen(s);i++) anss[i]=s[i];
     }
}

void dfs(int len,int dep){
     if (len<0) check();
        else {
             if (s[len]=='0') {
                dfs(len-1,dep+1);
             }
             if (s[len]=='1') {
                sum+=pow2[dep];
                dfs(len-1,dep+1);
                sum-=pow2[dep];
             }
             if (s[len]=='?') {
                for (int i=0;i<=1;i++) 
                    if (i==0) {
                       s[len]='0';
                       dfs(len-1,dep+1);
                       s[len]='?';
                    }
                       else {
                            s[len]='1';
                            sum+=pow2[dep];
                            dfs(len-1,dep+1);
                            sum-=pow2[dep];
                            s[len]='?';
                       }
             }
        }
}

void solve(){
     
     pow2[0]=1;
     for (int i=1;i<=61;i++) 
         pow2[i]=pow2[i-1]*2;
     
     scanf("%s",&s);
     int len=strlen(s);
     sum=0;
     ans=0;
     dfs(len-1,0);
     //cout<<ans<<endl;
     for (int i=0;i<strlen(s);i++)
         printf("%c",anss[i]);
     printf("\n");
}

int main(){
    
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    
    int test;
    scanf("%d",&test);
    for (int tot=1;tot<=test;tot++) {
        printf("Case #%d: ",tot);
        solve();
    }
    
    
    return 0;
}
