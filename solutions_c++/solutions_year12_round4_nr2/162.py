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
    if(((int*)b)[0]==((int*)a)[0])
     return ((int*)a)[1]-((int*)b)[1];
    return ((int*)b)[0]-((int*)a)[0];
}
int cmp(const void*a,const void *b)
{
    return ((int*)a)[1]-((int*)b)[1];
}

char s[1000005];
int a[1000005][2];
int x[10005],y[10005];

int max(int a,int b){
    if(a>b) return a;
    return b;
}
int abs(int a){
    if(a>0) return a;
    return -a;
}
int main()
{
    int i,j,n,m,k,l,o,p;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&p);
    int W,L;
    for1(o,0,p){
        same(a);
        same(x);
        same(y);
        scanf("%d%d%d",&n,&W,&L);
        for1(i,0,n){
            scanf("%d",&a[i][0]);
            a[i][1]=i;
        }
        qsort(a,n,sizeof(int)*2,cmpint);
        k=0;l=0;
        int tk=0;
        for1(i,0,n){
            if(l==0){
                if(k==0) x[a[i][1]]=k;
                else x[a[i][1]]=k+a[i][0];
                y[a[i][1]]=l;
                l+=a[i][0];
                if(k==0)
                  tk=max(tk,a[i][0]);
                else tk=max(tk,a[i][0]*2);
                if(l>=L){
                    k+=tk;
                    l=0;
                    tk=0;
                }
                continue;
            }
            if(l+a[i][0]>L){
                i--;
                k+=tk;
                l=0;
                tk=0;
                continue;
            }
            if(l+a[i][0]<=L&&l+a[i][0]*2>=L){
                 if(k==0) x[a[i][1]]=k;
                 else x[a[i][1]]=k+a[i][0];
                 y[a[i][1]]=L;
                 if(k==0)
                  tk=max(tk,a[i][0]);
                 else tk=max(tk,a[i][0]*2);
                 l=0;
                 k=k+tk;
                 tk=0;
                 continue;
            }
            if(1){
                if(k==0) x[a[i][1]]=k;
                else x[a[i][1]]=k+a[i][0];
                y[a[i][1]]=l+a[i][0];
                l+=a[i][0]*2;
                 if(k==0)
                  tk=max(tk,a[i][0]);
                 else tk=max(tk,a[i][0]*2);
            }
        }
        /*
        qsort(a,n,sizeof(int)*2,cmp);
        printf("Case #%d:",o+1);
        for1(i,0,n){
            for1(j,0,n){
                if(i!=j){
                    if(a[i][0]+a[j][0]>abs(x[i]-x[j])&&a[i][0]+a[j][0]>abs(y[i]-y[j]))
                    printf("%d %d\n",i,j);
                    //printf("x%d %d %d %d %d %d\n",a[i][0],a[j][0],x[i],x[j],y[i],y[j]);
                }
            }
        }
        printf("\n");
        */

        printf("Case #%d:",o+1);
        for1(i,0,n){
            printf(" %d %d",x[i],y[i]);
            //if(x[i]>W) printf("error\n");
        }
        printf("\n");

    }
    return 0;
}
