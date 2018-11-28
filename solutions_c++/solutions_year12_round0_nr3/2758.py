//#pragma comment(linker, "/STACK:65536000")
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<iostream>
#define clr(x,y) memset(x,y,sizeof(x))
#define ll __int64
using namespace std;

bool hash[3000000];
int ans=0;
int i,a,b;

int getnum(int g[],int l,int r){
    int num=0;
    for(int i=r;i>=l;i--)
        num=num*10+g[i];
    return num;
}
void find(int num){
    int g[20],p=0,f[100],k=0;
    f[++k]=num;
    while(num){
        g[++p]=num%10;
        num/=10;
    }
    int cnt=1;
    for(int i=1;i<p;i++){
        g[p+i]=g[i];
        int tmp=0;
        if(g[i+p]!=0)
            tmp=getnum(g,i+1,p+i);
        if(tmp>=a&&tmp<=b){
            f[++k]=tmp;
            cnt++;
            hash[tmp]=true;
        }
    }
    f[0]=0;
    sort(f+1,f+k+1);
    for(int i=1;i<=k;i++){
        if(f[i]==f[i-1])
            cnt--;
    }
    ans+=cnt*(cnt-1)/2;
}
int main(){
    freopen("e:\\in.txt","r",stdin);
    freopen("e:\\out.txt","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--){
        cas++;
        ans=0;
        scanf("%d%d",&a,&b);
        for(i=a;i<=b;i++) hash[i]=false;
        for(i=a;i<=b;i++){
            if(hash[i]) continue;
            find(i);
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
