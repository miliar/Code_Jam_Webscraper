#include <iostream>
using namespace std;
int f[2049],m[2049];
int T,p,x;
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    cin >> T;
    for(int I = 1;I <= T;++I){
        cin >> p;
        memset(f,0,sizeof(f));
        for(int i = 0;i < (1<<p);++i)
            cin >> m[i];
        for(int i = 0;i < (1<<p)-1;++i)
            cin >> x;
        for(int i = (1<<p)-1;i < (2<<p)-1;++i){
            int cur(i);
            for(int j = 0;j < min(m[i-(1<<p)+1],p);++j)
                cur = (cur-1) / 2;
            while(cur){
                cur = (cur-1) / 2;
                f[cur] = 1;
            }
        }
        int ans(0);
        for(int i = 0;i < (1<<p)-1;++i)
            ans += f[i];
        printf("Case #%d: %d\n",I,ans);
    }
}
