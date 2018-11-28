#include <iostream>

using namespace std;

long long a[105][105],ans[1<<16];
int n,k,w[105][1<<16],t[105];
bool can[1<<16];

bool check(int x,int y)
{
     long long p=a[x][0]-a[y][0];
     for (int i=0;i<k;i++)
         if (p*(a[x][i]-a[y][i])<=0) return false;
     return true;
}

void give(long long a,long long &b)
{
    if ((a<b)||(b==-1)) b=a;
}

void dfs(int x){
    if (ans[x]==-1) return;
    int d,y,i=0;
    for (int y=0;y<n;y++)
        if (((1<<y)& x)==0) 
        {      d=y;
               for (int j=1;j<=t[d];j++)
               {
                   i=w[d][j];
                   give(ans[x]+1,ans[i|x]); 
               }
        }
}
long long work(){
    cin>>n>>k;
    int i,j,x,y;
    for (i=0;i<n;i++)
    for (j=0;j<k;j++)
        cin>>a[i][j];
    memset(can,true,sizeof(can));
    memset(t,0,sizeof(t));
    for (i=0;i<(1<<n);i++)
    {
        for (x=0;x<n;x++)
        if (((1<<x)&i)>0)
        for (y=x+1;y<n;y++)
        {
        if (((1<<y)&i)>0)
            if (!check(x,y)) {can[i]=false;break;}
        }
    }
    for (i=0;i<(1<<n);i++)
    {
        for (int d=0;d<n;d++)
        if ( ((i&(1<<d))==0) && (can[i|(1<<d)])  ) can[i]=false;
        if (can[i])
        for (int d=0;d<n;d++)
        if ((i&(1<<d))!=0) {t[d]++;w[d][t[d]]=i;}
    }
    memset(ans,-1,sizeof(ans));
    ans[0]=0;
    for (int i=0;i<((1<<n)-1);i++) dfs(i);
    return ans[(1<<n)-1];
}

int main(){
    freopen("gcj3.in","r",stdin);
    freopen("gcj3.out","w",stdout);
    int t;
    cin>>t;
    for (int ii=1;ii<=t;ii++)
    {
        cout<<"Case #"<<ii<<": "<<work()<<endl;
    }
}
