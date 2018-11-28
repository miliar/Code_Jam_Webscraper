#include<stdio.h>
#include<string.h>

const int maxn=32;
const int maxs=1024*1024;
int g1[maxn][maxn];
int g2[maxn][maxn];
char s[maxs];
int K;
int ans;
int st[maxn];
bool flag[maxn];
int len;
int maxlen;

void input()
{
    scanf("%d",&K);
    scanf("%s",&s);
}

void add(int sp,int ep)
{
    int i,j;
    for(i=sp;i<=ep;i++){
        for(j=sp;j<=ep;j++){
            if(s[i]==s[j]){
                g1[i-sp][j-sp]++;
            }
        }
    }
}

void build()
{
    int i,j,k;
    len=strlen(s);
    memset(g1,0,sizeof(g1));
    memset(g2,0,sizeof(g2));
    add(0,K-1);
    for(i=K;i<len;i+=K){
        add(i,i+K-1);
        for(j=0;j<K;j++) for(k=0;k<K;k++){
            if(s[i-K+j]==s[i+k]){
                g2[j][k]++;
            }
        }
    }
}

void dfs(int sum,int p,int step)
{
    int i;
    if(sum+(step+1)*maxlen<=ans) return;
    if(step==0){
        sum+=g2[p][st[K]];
        if(ans<sum) ans=sum;
        return;
    }
    for(i=0;i<K;i++){
        if(flag[i]) continue;
        flag[i]=true;
        st[step]=i;
        dfs(sum+g1[p][i],i,step-1);
        flag[i]=false;
    }
}

int solve()
{
    int i,j;
    build();
    ans=0;
    maxlen=0;
    for(i=0;i<K;i++) for(j=0;j<K;j++){
        if(g1[i][j]>maxlen) maxlen=g1[i][j];
        if(g2[i][j]>maxlen) maxlen=g2[i][j];
    }
    memset(flag,0,sizeof(flag));
    dfs(0,K,K);
    return len-ans;
}

void show()
{
    int i,j;
    printf("g1:\n");
    for(i=0;i<K;i++){
        for(j=0;j<K;j++) printf("%d ",g1[i][j]);
        printf("\n");
    }
    printf("g2:\n");
    for(i=0;i<K;i++){
        for(j=0;j<K;j++) printf("%d ",g2[i][j]);
        printf("\n");
    }
    printf("maxlen=%d\n",maxlen);
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int i,T;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
        input();
        printf("Case #%d: ",i);
        printf("%d\n",solve());
        //show();
    }
    //while(1);
    return 0;
}
