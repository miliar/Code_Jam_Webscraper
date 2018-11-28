
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<cstring>
using namespace std;

int p[1000];
int main(){
        int t,cnt = 1;
        scanf("%d", &t);
        while(t--){
                int n,l,h;
                scanf("%d%d%d", &n,&l,&h);
                for(int i=0; i<n;i++)
                        scanf("%d", &p[i]);
                int f,ans;
                for(int i=l; i<=h;i++){
                        f = 0;
                        for(int j=0; j<n;j++){
                                if(p[j]%i !=0 && i%p[j]!=0) {f = 1; break;}
                        }
                        if(f) continue;
                        else {ans = i;break;}
                }
                printf("Case #%d: ", cnt++);
                if(f) printf("NO\n");
                else printf("%d\n", ans);
        }
        return 0;
}
