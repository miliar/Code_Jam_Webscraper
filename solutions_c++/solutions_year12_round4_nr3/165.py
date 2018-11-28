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
int y[100005];
int a[100005];

void work(int k,int val,double t){
    int i,j=0;
    y[k]=val;
    for1(i,1,k)
      if(a[i]==k){
       if(j==0) j=t*(k-i)+1.5;
       work(i,val-j,j*1.0/(k-i));
      }
    return;
}

int main()
{
    int i,j,n,m,k,l,o,p;
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);

    scanf("%d",&p);
    for1(o,0,p){
        same(a);
        same(y);
        scanf("%d",&n);
        for1(i,1,n)
         scanf("%d",&a[i]);
        printf("Case #%d:",o+1);
        int flag=0;
        for1(i,1,n)
         if(flag==0)
         for1(j,i,n){
             if(j>i&&j<a[i]&&a[j]>a[i])
               flag=1;
         }
        if(flag==1) {
            printf(" Impossible\n");
            continue;
        }
        work(n,100000000,0);
        for1(i,1,n+1)
         printf(" %d",y[i]);
        printf("\n");
    }
    return 0;
}
