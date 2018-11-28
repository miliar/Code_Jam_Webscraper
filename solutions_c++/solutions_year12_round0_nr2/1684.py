#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
#include<cmath>
using namespace std;
int n,s,p;
bool check(int a,int d){
    for(int i=0;i<=10;i++)
        for(int j=0;j<=10;j++)
            for(int k=0;k<=10;k++){
                if(i+j+k!=a) continue;
                if(abs(i-j)>d||abs(i-k)>d||abs(j-k)>d) continue;
                if(i>=p||j>=p||k>=p) return true;
            }
    return false;
}
int main(){
    //freopen("out","w",stdout);
    int cas=0,T,t;
    cin>>T;
    while(T--){
        cin>>n>>s>>p;        
        int ans=0;
        for(int i=0;i<n;i++){
            cin>>t;
            if(check(t,1)) ans++;
            else if(s&&check(t,2)) ans++,s--;
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    //fclose(stdout);
    return 0;
}
