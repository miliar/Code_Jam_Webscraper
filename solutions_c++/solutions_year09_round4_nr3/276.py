#include<vector>
#include<cstdio>
#include<algorithm>
using namespace std;
const int N=202;
int m,t,p[N],c[N][N];
int test(vector<int>& a,vector<int>& b)
{
    for(int i=0;i<m;i++)
        if(a[i]>=b[i])return 0;
    return 1;
}
int go(int v)
{
    if(v==t)return 1;
    if(p[v])return 0;
    p[v]=1;
    for(int i=0;i<=t;i++)
        if(c[v][i]-- && go(i))
            return ++c[i][v];
        else c[v][i]++;
    return 0;
}
int flow()
{
    int i,f=0;
    while(1){
        for(i=0;i<=t;i++)p[i]=0;
        if(!go(0))return f;
        f++;
    }
}
main()
{
    int i,j,k,n,T,C=1;
    scanf("%d",&T);
    while(T--){
        vector<int> s[101];
        scanf("%d %d",&n,&m);
        t=n*2+1;
        for(i=0;i<=t;i++)
            for(j=0;j<=t;j++)
                c[i][j]=0;
        for(i=0;i<n;i++){
            c[0][i+1]=c[i+n+1][t]=1;
            for(j=0;j<m;j++){
                scanf("%d",&k);
                s[i].push_back(k);
            }
        }
        sort(s,s+n);
        for(i=0;i<n;i++)
            for(j=i+1;j<n;j++)
                c[i+1][j+n+1]=test(s[i],s[j]);
        printf("Case #%d: %d\n",C++,n-flow());
    }
}
