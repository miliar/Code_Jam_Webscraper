#include <cstdio>
#include <cstring>

inline int convert(int h,int m)
{
	return h*60+m;
}

bool adj[111][111];
int len,na,nb,sh,sm,th,tm,N,as[111],bs[111],at[111],bt[111],ans;
bool vis[111];
int pre[111];

bool findb(int i)
{
	int j;
	for(j = 1;j <= na;++j)
		if(adj[j][i] && (!vis[j]))
		{
			vis[j] = 1;
			if(pre[j] == 0 || findb(pre[j]))
			{
				pre[j] = i;
				return 1;
			}
		}
	return false;
}

bool finda(int i)
{
	int j;
	for(j = 1;j <= nb;++j)
		if(adj[i][j] && (!vis[j]))
		{
			vis[j] = 1;
			if(pre[j] == 0 || finda(pre[j]))
			{
				pre[j] = i;
				return 1;
			}
		}
	return false;
}

int main(){
	freopen("out1.txt","w",stdout);
	int k,i,j;
    scanf("%d",&N);
    for(k=1;k<=N;++k){
        scanf("%d%d%d",&len,&na,&nb);
        for(i=1;i<=na;++i){
            scanf("%d:%d%d:%d",&sh,&sm,&th,&tm);
            as[i]=convert(sh,sm);
            at[i]=convert(th,tm)+len;
        }
        for(i=1;i<=nb;++i){
            scanf("%d:%d%d:%d",&sh,&sm,&th,&tm);
            bs[i]=convert(sh,sm);
            bt[i]=convert(th,tm)+len;
        }
        memset(adj,0,sizeof(adj));
		memset(pre,0,sizeof(pre));
        for(i=1;i<=na;++i)
            for(j=1;j<=nb;++j)
                if(bt[j]<=as[i])
                    adj[i][j]=1;
        for(i=1,ans=0;i<=nb;++i){
            memset(vis,0,sizeof(vis));
            if(findb(i))++ans;
        }
        int ansa = na-ans;
		memset(pre,0,sizeof(pre));
        memset(adj,0,sizeof(adj));
        for(i=1;i<=nb;++i)
            for(j=1;j<=na;++j)
                if(at[j]<=bs[i])
                    adj[j][i]=1;
        for(i=1,ans=0;i<=na;++i){
            memset(vis,0,sizeof(vis));
            if(finda(i))++ans;
        }
        int ansb = nb-ans;
        printf("Case #%d: %d %d\n",k,ansa,ansb);
    }
    return 0;
}