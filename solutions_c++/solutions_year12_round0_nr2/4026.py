
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<queue>
#include<cstdio>

using namespace std;
int m, n;
int main()
{
    int T;
    scanf("%d", &T);
    int it;
    for(it = 1; it <= T; it++) {
        printf("Case #%d: ", it);
        int n;
        scanf("%d",&n);
        int s,t;
        int p;
        scanf("%d%d",&s,&p);
        int i;
        int ans = 0;
        for(i = 0; i < n; i++) {
            scanf("%d",&t);
            if(t >= 3*p || (p > 0 && t >= 3*p - 2)) ans++;
            else if(s > 0 && p > 1 && t >= 3*p-4) ans++,s--; 
        }
        cout << ans << endl;
    }
   return 0;
}
