#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

struct node{
    int u, x, flag;
    bool operator <(const node &a)const{
        if(a.x==x)
            return a.u > u;
        return a.x > x;
    }
}nod[52];

int n, k, b, t;

int main(){
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);
    int nca;
    scanf("%d", &nca);
    for(int ii=1;ii<=nca;ii++){
        int cnt=0;
        scanf("%d%d%d%d", &n, &k, &b, &t);
        for(int i=0;i<n;i++){
            scanf("%d", &nod[i].x);
        }
        for(int i=0;i<n;i++){
            scanf("%d", &nod[i].u);
            if(nod[i].u*t>=b-nod[i].x){
                cnt++;
                nod[i].flag=1;
            }
            else nod[i].flag=0;
        }
        if(cnt<k){
            printf("Case #%d: IMPOSSIBLE\n",ii);
        }
        else{
            int ans=0;
            sort(nod, nod+n);
            for(int i=n-1;i>=0&&k;i--){
                if(nod[i].flag)k--;
                else{
                    for(int j=i-1;j>=0;j--){
                        if(nod[j].flag){
                            ans+=i-j;
                            k--;
                            nod[j].flag=0;
                            break;
                        }
                    }
                }
            }
            printf("Case #%d: %d\n", ii, ans);
        }
    }
    return 0;
}