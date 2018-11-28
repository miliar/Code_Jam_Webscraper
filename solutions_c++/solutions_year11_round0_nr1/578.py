#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <cstring>

using namespace std;
int t,n;
int b[105],o[105],num;
char seq[105],c;
int main(int argc, char** argv) {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    for(int v = 1;v <= t; ++v){
        int ans = 0,nb = 0,no = 0;
        scanf("%d",&n);
        for(int i = 0;i < n; ++i){
            scanf("%s%d",&c,&num);
            seq[i] = c;
            if(seq[i] == 'O') o[no++] = num;
            if(seq[i] == 'B') b[nb++] = num;
        }
        int so = 1,sb = 1;
        no = nb = 0;
        for(int i = 0;i < n; ++i){
            if(seq[i] == 'O'){
                int tmp = abs(o[no] - so) + 1;
                ans += tmp;
                so = o[no];
                no ++;
                if(b[nb] > sb) sb += min(tmp,abs(b[nb] - sb));
                else sb -= min(tmp,abs(b[nb] - sb));
            }
            else{
                int tmp = abs(b[nb] - sb) + 1;
                ans += tmp;
                sb = b[nb];
                nb ++;
                if(o[no] > so) so += min(tmp,abs(o[no] - so));
                else so -= min(tmp,abs(o[no] - so));
            }
        }
        printf("Case #%d: %d\n",v,ans);
    }
    return 0;
}

