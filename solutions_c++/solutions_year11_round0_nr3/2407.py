#include<cstdio>
#include<cstring>
#define abs(x) ((x)<0?-(x):(x))
#define min(x,y) (x<y?x:y)
#define clr(a,b) memset(a,b,sizeof(a))

using namespace std;

int T,n;
int d[1000];
int s,r,m;

void work()
{
    scanf("%d",&n);
    s=0;
    r=0;
    int e;
    m=10000000;
    for (int i=0;i<n;i++){
        scanf("%d",&e);
        s+=e;
        r=(r^e);
        m=min(m,e);
    }
    if (r==0)
        printf("%d\n",s-m);
    else
        printf("NO\n");
}


int main()
{
    FILE *cin=freopen("C-large.in", "r", stdin);
    FILE *cout=freopen("C.txt", "w", stdout);
    scanf("%d",&T);
    for (int tnum=1;tnum<=T;tnum++){
        printf("Case #%d: ",tnum);
        work();
    }
}
