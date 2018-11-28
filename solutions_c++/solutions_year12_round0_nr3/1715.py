#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;
int cnt[2000001],c,p;
int tran(int n){
    int ret=n;    
    for(int i=1;i<c;i++)
        ret=min(ret,n=n/10+n%10*p);
    return ret;
}
int main(){
    //freopen("out","w",stdout);
    int cas=0,T,a,b;
    cin>>T;
    while(T--){
        memset(cnt,0,sizeof(cnt));        
        int ans=0;
        cin>>a>>b;
        c=0,p=1;
        for(int t=a;t;t/=10,p*=10) c++;
        p/=10;
        for(int i=a;i<=b;i++){
            int t=tran(i);
            ans+=cnt[t];
            cnt[t]++;
        }
        cout<<"Case #"<<++cas<<": "<<ans<<endl;
    }
    //fclose(stdout);
}
