#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define INF 0x3f3f3f3f

typedef long long int int64;

//int memo[1000][1000];
int64 tmin;

long long int space(int a[],int n,int64 t,int l,int p,int to) {
        if(l < 0 || to > tmin) return INF;
        if(p == n) {
             if(to < tmin) tmin = to;            
             return to;
        }    
        //if(memo[p][l] > 0) return memo[p][l];
        int64 taux = t - to;
        if(taux < 0) taux = 0;
        if(taux > a[p]*2) taux = a[p]*2;
        return min(space(a,n,t,l,p+1,to+a[p]*2),space(a,n,t,l-1,p+1,to+taux+(a[p]-taux/2)));
        //memo[p][l] = min(space(a,n,t,l,p+1,to+a[p]*2),space(a,n,t,l-1,p+1,to+taux+(a[p]-taux/2)));
        //return memo[p][l];
    
}    

int main() {
    int T;
    scanf("%d",&T);
    for(int i = 1;i <= T;i++) { 
            int L,n,c;
            int64 t;
            int a[1010];
            scanf("%d %lld %d %d",&L,&t,&n,&c);
            tmin = INF;
            //for(int j = 0;j < n;j++)
              //    memset(memo[j],-1,sizeof(memo[j]));
            for(int j = 0;j < c;j++)
                    scanf("%d",&a[j]);
            for(int j = c;j < n;j++)
                  a[j] = a[j-c];        
            long long int total = space(a,n,t,L,0,0);
            
            printf("Case #%d: %lld\n",i,total);

    }
    return 0;
}
