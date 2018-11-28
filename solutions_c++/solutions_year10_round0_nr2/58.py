/* fair_warning */
/* produced by wegnahz */
#include <iostream>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#define skip(x) for(int i=1;i<=x;++i) getchar();
#define xx first
#define yy second
using namespace std;
const int inf=0x3FFFFFFF;
const double pi=acos(-1.0);
const double eps=1e-8;
const int move[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
const int maxn=1003,mm=1000000;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
typedef int number[12];
int n,m,ans;
number a[maxn],b[maxn],bantu,tmp;
char s[60];
void print(number &a){
    printf("%d",a[a[0]]);
    for (int i=a[0]-1;i;i--)
    {
        if (a[i]<100000) printf("0");
        if (a[i]<10000) printf("0");
        if (a[i]<1000) printf("0");
        if (a[i]<100) printf("0");
        if (a[i]<10) printf("0");
        printf("%d",a[i]);
    }
    printf("\n");
}
void convert(char *s,number &a){
    int len=strlen(s); a[0]=(len+5)/6;
    for (int i=1;i<=a[0];i++)
        for (int tmp=len-i*6,j=max(0,tmp);j<tmp+6;j++)
            a[i]=a[i]*10+s[j]-'0';
}
int cmp(number &a,number &b){
    if (a[0]<b[0]) return -1;else
    if (a[0]>b[0]) return 1;
    for (int i=a[0];i;i--)
        if (a[i]<b[i]) return -1;else
        if (a[i]>b[i]) return 1;
    return 0;
}
bool iszero(number &a){
    return a[0]==1 && a[1]==0;
}
void minuss(number &a,number &b){
    for (int i=1;i<=a[0];i++)
    {
        if (a[i]<b[i]) --a[i+1],a[i]+=mm;
        a[i]-=b[i];
    }
    while (a[a[0]]==0 && a[0]>1) --a[0];
}
void mmod(number &a,number &b){
    if (b[0]>a[0]) return;
    int d=a[0]-b[0],i,j;
    for (i=a[0];i>d;i--) b[i]=b[i-d];
    for (i=d;i;i--) b[i]=0;
    for (b[0]=a[0],i=0;;i++)
    {
        while (cmp(a,b)>=0) minuss(a,b);
        if (i==d) break;
        for (j=1;j<b[0];j++) b[j]=b[j+1];
        b[b[0]--]=0;
    }
}
void gcd(number &a,number &b){
    while (!iszero(b))
    {
        memcpy(tmp,b,sizeof(b));
        memcpy(b,a,sizeof(a));
        memcpy(a,tmp,sizeof(tmp));
        mmod(b,tmp);
    }
}
int main(){
    int tt,ii,i,j,k,t;
    #ifndef ONLINE_JUDGE
    freopen("fair_warning.in","r",stdin);
    freopen("fair_warning.out","w",stdout);
    #endif
    scanf("%d",&tt);
    for (ii=1;ii<=tt;ii++)
    {
        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        scanf("%d",&n);
        for (i=1;i<=n;i++)
        {
            scanf("%s",s);
            convert(s,a[i]);
        }
        memcpy(a[n+1],a[1],sizeof(a[1]));
        for (i=1;i<=n;i++)
            if (cmp(a[i],a[i+1])<0)
            {
                memcpy(b[i],a[i+1],sizeof(b[i]));
                minuss(b[i],a[i]);
            }else
            {
                memcpy(b[i],a[i],sizeof(b[i]));
                minuss(b[i],a[i+1]);
            }
        for (j=1;iszero(b[j]);j++);
        memcpy(bantu,b[j],sizeof(bantu));
        for (++j;j<=n;j++)
            if (!iszero(b[j]))
                gcd(bantu,b[j]);
        //print(bantu);
        mmod(a[1],bantu);
        if (iszero(a[1]))
        {
            printf("Case #%d: 0\n",ii);
            continue;
        }
        minuss(bantu,a[1]);
        printf("Case #%d: ",ii);
        print(bantu);
    }
    return 0;
}
