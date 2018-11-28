#include<iostream>
#include<string>

using namespace std;

int n,d[500][19];
string p="welcome to code jam",s;
const int mod=10000;

int f(int i,int k){
    int &res=d[i][k];
    if(res<0){
        res=0;
        if(i>=0&&i>=k){
            if(s[i]==p[k])
                if(k)res=(res+f(i-1,k-1))%mod;
                else res=1;
            res=(res+f(i-1,k))%mod;
        }
    }
    return res;
}

int main(){
    freopen("C-large.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc,m=p.size();
    scanf("%d\n",&tc);
    for(int t=1;t<=tc;++t){
        getline(cin,s);
        n=s.size();
        memset(d,-1,sizeof(d));
        printf("Case #%d: %.4d\n",t,f(n-1,m-1));
    }
    return 0;
}
