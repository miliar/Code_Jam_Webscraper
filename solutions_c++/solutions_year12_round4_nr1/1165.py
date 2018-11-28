#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int pos[10005],len[10005];
int maxp[100005];
bool solve(int n,int d){
    if(pos[0]>len[0])
        return 0;
    maxp[0]=pos[0];
    if(maxp[0]>=d-pos[0])
        return 1;
    int i,j;
    int tmp,td;
    for(i=0;i<n;i++){
        if(maxp[i]>=d-pos[i])
            return 1;
        for(j=i+1;j<n;j++){
            td=pos[j]-pos[i];
            if(maxp[i]<td)
                continue;
            int tmp=td<len[j]?td:len[j];
            maxp[j]=tmp>maxp[j]?tmp:maxp[j];
        }
    }
    return 0;
}
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int cas,c;
    int n,d,i,j;
    scanf("%d",&cas);
    for(c=1;c<=cas;c++){
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%d%d",pos+i,len+i);
            maxp[i]=-1;
        }
        scanf("%d",&d);
        bool ans=solve(n,d);
        if(ans)
            printf("Case #%d: YES\n",c);
        else
            printf("Case #%d: NO\n",c);
    }
    return 0;
}
