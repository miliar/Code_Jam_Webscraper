/* snapper_chain */
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
const int maxn=32;
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}
inline void fill(int *a,int b,int c){
  for (int i=0;i<c/4;i++,a++) *a=b;}
int n,m,ans,sro;
bool a[maxn],b[maxn];
int main(){
    int tt,ii,i,j,k,t;
    #ifndef ONLINE_JUDGE
    freopen("snapper_chain.in","r",stdin);
    freopen("snapper_chain.out","w",stdout);
    #endif
    scanf("%d",&tt);
    for (ii=1;ii<=tt;ii++)
    {
        scanf("%d%d",&n,&m);
        printf("Case #%d: %s\n",ii,((m+1)%(1<<n))?"OFF":"ON");
    }
    return 0;
}
