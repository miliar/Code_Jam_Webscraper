#include<stdio.h>
#include<vector>
#define SIZE 2010
#define MAX 1000000000
#define pb push_back
using namespace std;
int to[SIZE],N,h[SIZE];
bool go(int ll,int rr,int ratio){
    vector<int>qq;
    qq.pb(ll);
    while(qq.back()<rr)qq.pb(to[qq.back()]);
    if(qq.back()>rr)return 0;
    for(int i=(int)qq.size()-1;i>0;i--){
        h[qq[i-1]]=h[qq[i]]-(qq[i]-qq[i-1])*ratio;
        ratio++;
        if(qq[i-1]+1<qq[i]){
            if(!go(qq[i-1]+1,qq[i],ratio))return 0;
        }
    }
    return 1;
}
int main(){
    int T,i,j,cs=0;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&N);
        for(i=1;i<N;i++)scanf("%d",&to[i]);
        printf("Case #%d:",++cs);
        h[N]=MAX;
        if(!go(1,N,0))puts(" Impossible");
        else{
            for(i=1;i<=N;i++)printf(" %d",h[i]);
            puts("");
        }
    }
    return 0;
}
