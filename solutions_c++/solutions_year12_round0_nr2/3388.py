#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

const int MAXN = 100000 + 10;
const int INF = 1<<30;
const double eps = 1e-8;

int n,s,p,g[1000];

int main()
{
  //  freopen("B-large.in","r",stdin);
  //  freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d%d%d",&n,&s,&p);
        for(int i=0;i<n;i++)
            scanf("%d",&g[i]);
        sort(g,g+n);
        int ans=0;
        for(int i=n-1;i>=0;i--)
        {
            if(g[i]/3>=p) ans++;
            else if(g[i]/3+1>=p&&g[i]%3) ans++;
            else if(((g[i]/3+1>=p&&g[i]%3==0)||(g[i]/3+2>=p&&g[i]%3==2))&&s&&g[i])
            {
                s--;
                ans++;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
	return 0;
}
