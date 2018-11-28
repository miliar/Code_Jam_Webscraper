#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<iostream>
#include<utility>
#define INF 1000000000

using namespace std;
typedef pair<int,int> ii;
int A,B;
bool vis[2000010];
long long int S=0;int TC;
inline long long int test(int u){

    long long int s=1;
    int x=1;
    int c=0;
    while(x<=u){
        x*=10;
        c++;
    }
    c--;
    x/=10;
    int z=x;
    int y=u;
    int f=10;vis[u]=true;
    while(c-->0){
        y=(u%f)*x+u/f;
        if(A<=y&&B>=y&&y>=z&&!vis[y]){
            s++;
            vis[y]=true;
        }
        f*=10;x/=10;
    }
    return s;
}

int main(){
    scanf("%d",&TC);
    int i,j,k;
    for(int tc=1;tc<=TC;tc++){
        scanf("%d%d",&A,&B);
        S=0;
        memset(vis,false,sizeof vis);
        for(i=A;i<=B;i++){

            if(!vis[i]){
                long long int z=test(i);
                S+=z*(z-1)/2;
            }
        }
        printf("Case #%d: %lld\n",tc,S);
    }
    //memset(vis,false,sizeof vis);
    //printf("%lld\n",test(122));
    //printf("%lld\n",test(212));
    return 0;
}
