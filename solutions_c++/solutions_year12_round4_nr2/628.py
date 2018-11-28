#include <vector>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <map>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <string>
#include <set>
#include <cstring>
using namespace std;
#define For(i,n) for(int i=0;i<n;i++)
#define sz(i) int(i.size())
#define mst(i,n) memset(i,n,sizeof(i))
#define eps 1e-9
#define INF 1e20
#define MOD 1000000007
#define LL long long
#define pi acos(-1)
LL gcd(LL a,LL b){if(a==0)return b;return gcd(b%a,a);}
struct T{
    int r,ind;
    double x,y;
}t[1<<10];
bool cmp(struct T a,struct T b){
    return a.r>b.r;
}
bool cmp2(struct T a,struct T b){
    return a.ind<b.ind;
}
bool dis(struct T a,struct T b){
    return sqrt( (a.x-b.x)*(a.x-b.x) + (a.y-b.y)*(a.y-b.y) ) > a.r+b.r;
}
int main()
{
    int T;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&T);
    For(ca,T)
    {
        int w,l,n;
        scanf("%d %d %d",&n,&w,&l);
        For(i,n){
            scanf("%d",&t[i].r);
            t[i].ind = i;
        }
        //sort(t,t+n,cmp);
        t[0].x=t[0].y=0;
        For(i,n){
            if(!i) continue;
            int tm = 50 ;
            double len = w;
            int pos = -1;
            double X,Y;
            For(pp,tm - 1){
                t[i].y=1.0*l/tm*pp;
                double high = w,low = 0;
                while(high-low>0.1){
                    double mid = (high+low) / 2;
                    t[i].x = mid;
                    bool flag = true;
                    For(j,i){
                        if(!dis(t[i],t[j])){
                            flag = false;
                            break;
                        }
                    }
                    if(flag){
                        high = mid;
                        if(mid<len){
                            len = mid;
                            pos = 0;
                            X=t[i].x;
                            Y=t[i].y;
                        }
                    }
                    else
                        low = mid;
                }
            }
            if(pos!=-1)
                t[i].x=X,t[i].y=Y;
            else{
                fprintf(stderr,"Fuck\n");
            }
        }
        printf("Case #%d:",1+ca);
        For(i,n) printf(" %lf %lf",t[i].x,t[i].y);
        printf("\n");
    }
}
