#include <iostream>
using namespace std;
int v[50],sum[50],n;
int read(){
    while(cin.peek()==' '||cin.peek()=='\n')getchar();
    char ch=getchar();
    if(ch=='1')return 1;
    else if(ch=='0')return 0;
    else {
        printf("error\n");
        while(1);
    }
}
bool ok(int i,int t){
    sum[t]--;
    int tmp=0,sd,j;
     for(j=n;j>=1;j--){
        if(j>=i)sd=0;
        else sd=i-j;
        if(sum[j]+tmp>sd)break;
        tmp+=sum[j];
    }
    if(j==0){
        sum[t]++;
        return 1;
    }
    else {
        sum[t]++;
        return 0;
    }
}
bool ok2(int i,int t){
    sum[t]--;
    int tmp=0,sd,j;
     for(j=1;j<=n;j++){
        if(j<=i)sd=0;
        else sd=j-i;
        if(sum[j]+tmp>sd)break;
        tmp+=sum[j];
    }
    if(j==n+1){
        sum[t]++;
        return 1;
    }
    else {
        sum[t]++;
        return 0;
    }
}
void sp(int i,int j){
    int tmp=v[i];
    v[i]=v[j];
    v[j]=tmp;
}

int main(){
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    int cas,ca=1,i,j,k,a[50][50],res;
    cin>>cas;
    while(cas--){
        cin>>n;
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                a[i][j]=read();
            }
        }
        for(i=1;i<=n;i++){
            for(j=n;j>=1;j--){
                if(a[i][j]==1)break;
            }
            v[i]=j;
        }
        memset(sum,0,sizeof(sum));
        for(i=1;i<=n;i++){
            sum[v[i]]++;
        }
        int tmp=0;
        for(i=n;i>=1;i--){
            if(sum[i]+tmp>n-i+1)break;
            tmp+=sum[i];
        }
        if(i==0){
            res=0;
            for(i=n;i>=1;i--){
                for(j=i;j>=1;j--){
                    if(ok(i,v[j])){
                        sum[v[j]]--;
                        for(k=j;k<i;k++){
                            sp(k,k+1);
                            res++;
                        }
                        break;
                    }
                }
            }
        }
        else res=999999;
        int res2;
        res2=0;
        for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
                if(a[i][j]==1)break;
            }
            v[i]=j;
        }
        memset(sum,0,sizeof(sum));
        for(i=1;i<=n;i++){
            sum[v[i]]++;
        }
        tmp=0;
        for(i=1;i<=n;i++){
            if(sum[i]+tmp>i)break;
            tmp+=sum[i];
        }
        if(i==0){
            res2=0;
            for(i=1;i<=n;i++){
                for(j=i;j<=n;j++){
                    if(ok2(i,v[j])){
                        sum[v[j]]--;
                        for(k=j;k>i;k--){
                            sp(k,k-1);
                            res2++;
                        }
                        break;
                    }
                }
            }
        }
        else res2=999999;
        if(res2<res)res=res2;
        printf("Case #%d: %d\n",ca++,res);
    }
    return 0;
}
                    
