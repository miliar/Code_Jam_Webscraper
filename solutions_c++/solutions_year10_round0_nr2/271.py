#include<iostream>
#include<algorithm>
#define maxn 1005
#define maxl 60

using namespace std;

struct bignum{
    int d[maxl];
}a[maxn],now,mid;

void clear(bignum &a){
    int i;
    for(i=0;i<maxl;++i)a.d[i]=0;
}

bool bigger(const bignum &a,const bignum &b,int wei){
    if(a.d[0]-wei>b.d[0])return true;
    if(a.d[0]-wei<b.d[0])return false;
    int i;
    for(i=b.d[0];i>0;--i){
        if(a.d[i+wei]>b.d[i])return true;
        if(a.d[i+wei]<b.d[i])return false;
    }
    return true;
}


bool operator <(const bignum &a,const bignum &b){
    return !bigger(a,b,0);
}

void jian(bignum &a,bignum &b,int wei){
    int i,x=0;
    for(i=1;i<=a.d[0]-wei;++i){
        x=10+a.d[i+wei]-b.d[i]+x;
        a.d[i+wei]=x%10;
        x=x/10-1;
    }
    while((a.d[0]>1)&&(a.d[a.d[0]]==0))--a.d[0];
}

void div(bignum &a,bignum &b){
    if(a<b)return;
    int i;
    for(i=a.d[0]-b.d[0];i>=0;--i)
        while(bigger(a,b,i))jian(a,b,i);
    while((a.d[0]>1)&&(a.d[a.d[0]]==0))--a.d[0];
}

bignum gcd(bignum a,bignum b){
    while(true){
        div(a,b);
        if((a.d[0]==1)&&(a.d[1]==0))return b;
        div(b,a);
        if((b.d[0]==1)&&(b.d[1]==0))return a;
    }
}

void print(bignum &a){
    int i;
    for(i=a.d[0];i>0;--i)printf("%d",a.d[i]);
    printf("\n");
}

char s[maxl+5];

void solve(){
    int n,len,i,j;
    scanf("%d",&n);
    for(i=1;i<=n;++i){
        scanf("%s",s+1);
        len=strlen(s+1);
        clear(a[i]);
        a[i].d[0]=len;
        for(j=1;j<=len;++j)a[i].d[j]=s[len+1-j]-48;
    }
    sort(&a[1],&a[n+1]);
    now=a[2];
    jian(now,a[1],0);
    for(i=3;i<=n;++i){
        mid=a[i];
        jian(mid,a[i-1],0);
        if((mid.d[0]>1)||(mid.d[1]>0))now=gcd(now,mid);
    }
    div(a[1],now);
    //print(now);
    if((a[1].d[0]==1)&&(a[1].d[1]==0))now=a[1];else jian(now,a[1],0);
    print(now);
}

int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int t,i;
    scanf("%d",&t);
    for(i=1;i<=t;++i){
        printf("Case #%d: ",i);
        solve();
    }
}
