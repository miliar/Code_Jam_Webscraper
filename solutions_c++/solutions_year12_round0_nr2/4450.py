#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <utility>
#include <string>
#include <map>
#include <set>

#define INP "B.in"
#define OUP "B.out"

using namespace std;

int n,s,p;

int main()
{
    freopen(INP,"r",stdin);
    freopen(OUP,"w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int t=1;t<=tc;t++){
        scanf("%d%d%d",&n,&s,&p);
        int org_ans,surprise_ans;
        org_ans = surprise_ans = 0;
        for (int i=1;i<=n;i++){
            int cur;
            scanf("%d",&cur);
            if (cur - p<0)
                continue;
            if (p*2 - (cur - p)<=2){
                org_ans ++;
                continue;
            }
            if (p*2 - (cur - p)<=4){
                surprise_ans ++;
                continue;
            }
        }
        printf("Case #%d: %d\n",t,org_ans + min(surprise_ans,s));
    }
    return 0;
}
