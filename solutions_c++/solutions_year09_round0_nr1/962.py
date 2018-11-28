#include<stdio.h>
#include<string.h>
char dic[10000][20],str[10000],tmp[1000];
int ans,l,n,nq,nc;
bool dfs(int dep,int po,int id)
{
    int i,j;
    if(po==l) return true;
    if(str[dep]=='(')
    {
        for(i=dep;;i++) if(str[i]==')') break;
        for(j=dep+1;j<i;j++) if(str[j]==dic[id][po]) return dfs(i+1,po+1,id);
        return false;
    }
    else
    {
        if(str[dep]==dic[id][po]) return dfs(dep+1,po+1,id);
        else return false;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int i,len,ans;
    scanf("%d%d%d",&l,&n,&nq);
    for(i=1;i<=n;i++) scanf("%s",dic[i]);
    //for(i=1;i<=n;i++) printf("---%s\n",dic[i]);
    for(nc=1;nc<=nq;nc++)
    {
        scanf("%s",str);  
        ans=0;
        for(i=1;i<=n;i++)
        {
            if(dfs(0,0,i)) ans++;
        }
        printf("Case #%d: %d\n",nc,ans);
    }
    return 0;
}
