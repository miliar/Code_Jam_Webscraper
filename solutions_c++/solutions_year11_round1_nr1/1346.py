#include<cstdio>
#include<cstring>

#define  ll long long
int gcd(int a,int b){
    if(!b)return a;
    return gcd(b,a%b);
}
int solve(int n,int p1,int p2){
    if(p2==100&&p1<100)return 0;
    if(p2==0&&p1>0)return 0;
    int t=gcd(p1,100);
    t=100/t;
    if(n<t)return 0;
    return 1;
}
int main(){
    freopen("A-small-attempt2.in","r",stdin);
   // freopen("B-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int t,num=1;
    scanf("%d",&t);
    while(t--){
        int n,p1,p2;
        scanf("%d%d%d",&n,&p1,&p2);
        printf("Case #%d: ",num++);
        printf(solve(n,p1,p2)?"Possible\n":"Broken\n");

    }

    return 0;
}
