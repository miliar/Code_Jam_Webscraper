#include<iostream>
#include<ios>
#include<fstream>
#include<string>
#include<sstream>
#include<algorithm>
using namespace std;
#define CLR(x,y) memset((x) ,y ,sizeof(x))
int g[110];

int main() {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int t,R,K,N,ans;
    int cas=1;
    while(scanf("%d",&t)!=EOF) {
        cas=1;
        while(t--) {
            scanf("%d%d%d",&R,&K,&N);
            for(int i=0; i<N; i++) scanf("%d",&g[i]);
            ans=0;
            int s=0;
            for(int i=0; i<R; i++) {
                int k=0,tmp=0;
                for(k=0; k<N; k++) {
                    if(tmp+g[(k+s)%N]<=K) {
                        tmp+=g[(k+s)%N];
                        ans+=g[(k+s)%N];
                    }
                    else break;
                }
                s=(k+s)%N;
            }
            printf("Case #%d: %d\n",cas++,ans);
        }
    }
    //system("pause");   
    return 0;
}
