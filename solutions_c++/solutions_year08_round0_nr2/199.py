#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

const int maxn=128;
struct node{
    int ts,te;
    int from;
    int flag;
}a[maxn*2];
int na,nb;
int T;
int s1,s2;

int getTime(char s[])
{
    int ans=0;
    ans=60*(10*(s[0]-'0')+(s[1]-'0'))+(10*(s[3]-'0')+(s[4]-'0'));
    return ans;
}

void input()
{
    int i;
    char str[10];
    scanf("%d",&T);
    scanf("%d%d",&na,&nb);
    for(i=0;i<na;i++){
        scanf("%s",&str);
        a[i].ts=getTime(str);
        scanf("%s",&str);
        a[i].te=getTime(str);
        a[i].from=0;
        a[i].flag=0;
    }
    for(;i<na+nb;i++){
        scanf("%s",&str);
        a[i].ts=getTime(str);
        scanf("%s",&str);
        a[i].te=getTime(str);
        a[i].from=1;
        a[i].flag=0;
    }
}

void dfs(int x, int from, int sp)
{
    int i;
    a[x].flag=1;
    for(i=sp;i<na+nb;i++){
        if(a[i].flag==0 && a[i].from==from && a[i].ts>=a[x].te+T){
            dfs(i,1-from,sp+1);
            return;   
        }
    }
}

bool cmp(const node& a, const node& b)
{
    if(a.ts!=b.ts) return a.ts<b.ts;
    return a.te<b.te;    
}

void solve()
{
    int i;
    s1=s2=0;
    sort(a,a+na+nb,cmp);
    for(i=0;i<na+nb;i++){
        if(a[i].flag==0){
            dfs(i,1-a[i].from,i+1);
            if(a[i].from==0) s1++;
            else s2++;
        }
    }
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    int i,cas;
    scanf("%d",&cas);
    for(i=1;i<=cas;i++){
        input();
        solve();
        printf("Case #%d: %d %d\n",i,s1,s2);
    }
    return 0;
} 
