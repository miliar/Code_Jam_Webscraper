#include <iostream>
using namespace std;
#define N 2100
int f[N],m[N];
int p;
int offset;
int ans;
void init(){
    int x;
    cin >> p;
    memset(f,0,sizeof(f));
    offset = (1<<p);
    for(int i = 0;i < offset;++i)	cin >> m[i];
    for(int i = 0;i < offset-1;++i)	cin >> x;
}

void work(){
    ans = 0;
    int len = (2<<p)-1;
	for(int i = offset-1;i < len;++i){
	    int x = i;
        for(int j = 0;j < min(m[i-offset+1],p);++j)
            x = (x-1)>>1;
        while(x){
            x = (x-1)>>1;
            f[x] = 1;
        }
    }
    for(int i = 0;i < offset-1;++i)	ans += f[i];
}
        
int main(){
    int T;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    cin >> T;
    for(int index = 1;index <= T;++index){
        init();
        work();
        printf("Case #%d: %d\n",index,ans);
    }
}

