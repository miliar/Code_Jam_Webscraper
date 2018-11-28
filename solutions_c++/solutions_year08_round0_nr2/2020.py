#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int n,as[110],at[110],bs[110],bt[110],adj[110][110],pre[110];
bool vis[110];
inline int convert(int s,int t){
    return s*60+t;
}
bool find(int i){
    //printf("*%d\n",i);
    //system("pause");
    for(int j=0;j<n;++j){
        if(adj[i][j]&&!vis[j]){
            vis[j]=true;
            if(pre[j]==-1||find(pre[j])){
                pre[j]=i;
                return true;
            }
        }
    }
    return false;
}
void test(){
    int i,j;
    for(i=0;i<n;++i){
        for(j=0;j<n;++j)printf("%d ",adj[i][j]);
        printf("\n");
    }
    for(i=0;i<n;++i)printf("%d %d\n",i,pre[i]);
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int N,k,i,j,len,na,nb,sh,sm,th,tm,ans,aa,bb;
    scanf("%d",&N);
    for(k=1;k<=N;++k){
        scanf("%d%d%d",&len,&na,&nb);
        n=(na>nb?na:nb);
        for(i=0;i<na;++i){
            scanf("%d:%d%d:%d",&sh,&sm,&th,&tm);
            as[i]=convert(sh,sm);
            at[i]=convert(th,tm)+len;
        }
        for(i=0;i<nb;++i){
            scanf("%d:%d%d:%d",&sh,&sm,&th,&tm);
            bs[i]=convert(sh,sm);
            bt[i]=convert(th,tm)+len;
        }
        memset(adj,0,sizeof(adj));
        memset(pre,-1,sizeof(pre));
        for(i=0;i<na;++i)
            for(j=0;j<nb;++j)
                if(bt[j]<=as[i])
                    adj[j][i]=1;//test();
        for(i=0,ans=0;i<nb;++i){
            memset(vis,0,sizeof(vis));
            if(find(i))++ans;
        }//printf("%d %d %d \n",pre[0],pre[1],pre[2]);
        
        aa=na-ans;
        memset(adj,0,sizeof(adj));
        memset(pre,-1,sizeof(pre));
        for(i=0;i<nb;++i)
            for(j=0;j<na;++j)
                if(at[j]<=bs[i])
                    adj[j][i]=1;
        for(i=0,ans=0;i<na;++i){
            memset(vis,0,sizeof(vis));
            if(find(i))++ans;
        }
        bb=nb-ans;
        printf("Case #%d: %d %d\n",k,aa,bb);
    }
    return 0;
}

    
