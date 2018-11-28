#include<cstdio>
#include<cstring>

using namespace std;

int main(){
    int T,n,m,i;
    scanf("%d",&T);
    for(int test=1;test<=T;++test){
        scanf("%d%d",&n,&m);
        bool ok=true;
        for(i=0;i<n;++i)
            if(!((1<<i)&m)) ok=false;
        if(ok) printf("Case #%d: ON\n",test);
        else printf("Case #%d: OFF\n",test);
    }
}
