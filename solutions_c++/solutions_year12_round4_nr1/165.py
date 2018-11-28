#include<cmath>
#include<cstdio>
#include<cctype>
#include<vector>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;

#define sqr(a) (a)*(a)
#define cub(a) (a)*(a)*(a)
#define for1(i,a,b) for(i=(a);i<(b);i++)
#define for2(i,a,b) for(i=(a);i>(b);i--)
#define same(a) memset((a),0,sizeof(a));
#define ll long long

int cmpint(const void*a,const void *b)
{
    if(((int*)a)[0]==((int*)b)[0])
      return ((int*)a)[1]-((int*)b)[1];
    return ((int*)a)[0]-((int*)b)[0];
}

char s[1000005];
int a[1000005][3]={0};

int min(int a,int b){
    if(a>b) return b;
    return a;
}

int main()
{
    int i,j,n,m,k,l,o,p;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&p);
    for1(o,0,p){
        same(a);
        scanf("%d",&n);
        for1(i,0,n)
         scanf("%d%d",&a[i][0],&a[i][1]);
        scanf("%d",&m);
        qsort(a,n,sizeof(int)*3,cmpint);
        a[n][0]=m;
        a[n][1]=1;
        n++;
        a[0][2]=a[0][0];
        for1(i,0,n){
            //printf("^^%d ",a[i][2]);
            for1(j,i+1,n){
                if(a[j][0]>a[i][0]+a[i][2]) break;
                if(a[j][2]==0)
                  a[j][2]=min(a[j][1],a[j][0]-a[i][0]);
                //printf("$%d %d ",j,a[j][2]);
            }
        }
        printf("Case #%d: ",o+1);
        if(a[n-1][2]>0) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
