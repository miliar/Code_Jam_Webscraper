#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

int main(int argc, char** argv) {
    int T,cas=1;
    scanf("%d",&T);
    while(cas<=T){
        int n,s,p,cnt=0;
        scanf("%d%d%d",&n,&s,&p);
        for(int i=0;i<n;i++){
            int tmp;
            scanf("%d",&tmp);
            if(tmp>3*p-3) cnt++;
            else if(s>0&&tmp==3*p-3&&tmp>=3){
                cnt++;
                s--;
            }
            else if(s>0&&tmp==3*p-4&&tmp>=2){
                cnt++;
                s--;
            }
        }
        printf("Case #%d: %d\n",cas,cnt);
        cas++;
    }
    return 0;
}

