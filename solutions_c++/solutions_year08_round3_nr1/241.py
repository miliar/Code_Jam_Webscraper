#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<vector>
#include<map>
#include<string>
#define int64 long long
using namespace std;

int t, p, k, l;
vector<int64> f;

int main() {
    scanf("%d",&t);
    for(int z=0;z<t;z++) {
        f.clear();
        scanf("%d %d %d",&p,&k,&l);
        int tmp;
        for(int i=0;i<l;i++) {
            scanf("%I64d",&tmp);
            f.push_back(tmp);
        }
        sort(f.rbegin(),f.rend());
        int64 ret = 0, ti = 0;
        for(int i=0;i<l;i++) {
            if(i%k == 0) ti++;
            ret += ti*f[i];
        }
        printf("Case #%d: %I64d\n",z+1,ret);
    }
    return 0;
}
        
            
