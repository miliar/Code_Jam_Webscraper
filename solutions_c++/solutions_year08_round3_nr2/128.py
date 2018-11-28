#include <iostream>
#include <cmath>
using namespace std;

#define mset(a,x) memset(a,x,sizeof(a))
typedef long long i64;
const int INF=INT_MAX/2;

char buf[100];
int len;
i64 sum;
i64 res;

void dfs(int d,i64 r,int p)
{
    if(d==len){
        sum+=p*r;
        if(sum%2==0 || sum%3==0 || sum%5==0 || sum%7==0){
            res++;
        }
        sum-=p*r;
    }
    else {
        sum+=p*r;
        dfs(d+1,buf[d]-'0',1);
        dfs(d+1,buf[d]-'0',-1);
        sum-=p*r;
        dfs(d+1,10*r+(buf[d]-'0'),p);
    }
}

int main()
{
    int T,kcase(0);
    scanf("%d",&T);
    while(T--){
        scanf("%s",buf);
        len=strlen(buf);
        sum=0;
        res=0;
        dfs(1,buf[0]-'0',1);
        printf("Case #%d: %d\n",++kcase,res);
    }
}
