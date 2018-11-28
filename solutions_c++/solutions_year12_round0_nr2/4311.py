#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int t,i,n,p,s;
int a[10000000];
char c;
bool rcmp(int a1,int a2){
    return a1>a2;
}
int main(){
    freopen("u2.in","r",stdin);
    freopen("u2.out","w",stdout);
    scanf("%d\n",&t);
    for(i=1;i<=t;i++){
        printf("Case #%d: ",i);
        scanf("%d%d%d",&n,&s,&p);
        for(int j=0;j<n;j++){
            scanf("%d",&a[j]);
        }
        sort(a,a+n,rcmp);
        int ct=0;
        int j;
        for(j=0;j<n;j++){
            if(a[j]>(p-1)*3)ct++;
            else break;
        }
        for(;j<n;j++){
            if(a[j]!=0&&a[j]>(p-1)*3-2&&s>0){
                ct++;
                s--;
            }
            else break;
        }
        printf("%d",ct);
        printf("\n");
    }
    return 0;
}
