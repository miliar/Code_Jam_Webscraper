#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <numeric>
#include <utility>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <algorithm>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

const int oo = 0x7fffffff;
const double PI = atan2(0.0, -1.0);
const double eps=(1.0e-9);

int gcd(int a, int b)
{
   if(b==0) return a;
   else return gcd(b,a%b);
}

struct node{
    bool leaf;
    int g;
    int c;
    int v;
}t[32],tmp[32];

bool valid(int* bit,int n)
{
    for(int i=1;i<=n;++i)
        if(bit[i-1]&&t[i].leaf==false&&t[i].c==0)
            return false;
    return true;
}

int f(int k,int n)
{
    if(tmp[k].leaf)
        return tmp[k].v;
    if(tmp[k].g)
        return (f(2*k,n)*f(2*k+1,n)>0?1:0);
    else
        return (f(2*k,n)+f(2*k+1,n)>0?1:0);
}

int cal(int* bit,int n,int v)
{
    int i,cnt=0;

    for(i=1;i<32;++i)
        tmp[i]=t[i];

    for(i=1;i<=n;++i)
        if(bit[i-1]){
            tmp[i].g=(tmp[i].g==1?0:1);
            ++cnt;
        }
    if(f(1,n)==v)
        return cnt;
    return oo;
}

int main()
{
    int i,j,bit[32],re,cas,m,v,ans,limit;

    freopen("A-small.in","r",stdin);
    freopen("A-small.out","w",stdout);
    
    for(scanf("%d",&re),cas=1;re--;++cas){
        scanf("%d%d",&m,&v);
        for(i=1;i<=(m-1)/2;++i){
            scanf("%d%d",&t[i].g,&t[i].c);
            t[i].leaf=false;
        }
        for(j=1;j<=(m+1)/2;++j,++i){
            scanf("%d",&t[i].v);
            t[i].leaf=true;
        }
        
        ans=oo;
        limit=(1<<( (m-1)/2 ) );
        for(i=0;i<limit;++i){
            for(j=0;j<(m-1)/2;++j)
                bit[j]=( (i>>j)&1 );
            if(valid(bit,(m-1)/2))
                ans=min(ans,cal(bit,(m-1)/2,v));
        }
        if(ans==oo)
            printf("Case #%d: IMPOSSIBLE\n",cas);
        else
            printf("Case #%d: %d\n",cas,ans);
    }
    
}















