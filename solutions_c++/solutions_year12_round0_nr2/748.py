#include<stdio.h>
#include<stdlib.h>
void solve(int test){
    int n,s,p;
    scanf("%d %d %d",&n,&s,&p);
    int ans=0;
    for(int i=0;i<n;i++){
        int k;
        scanf("%d",&k);
        if(k%3!=0&&k/3+1>=p)ans++;
        else if(k%3==0&&k/3>=p)ans++;
        else if(s&&k%3==0&&k/3+1>=p&&k/3>0){
            ans++;s--;
        }
        else if(s&&k%3==1&&k/3+1>=p){
            ans++;s--;
        }
        else if(s&&k%3==2&&k/3+2>=p){
            ans++;s--;
        }
    }
    printf("Case #%d: %d\n",test,ans);
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)solve(i);
}
