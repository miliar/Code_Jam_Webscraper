#include <cstdio>
#include <cstring>
#include <stack>
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <map>
using namespace std;
int w[10000];

int main()
{
    int t,n;
    freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
    scanf("%d",&t);
    int cas=0;
    while(t--)
    {
        scanf("%d",&n);
        int sum=0;
        int rr=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&w[i]);
            rr=rr^w[i];
            sum+=w[i];
        }
        sort(w,w+n);
        //cout<<rr<<endl;
        if(rr)
            printf("Case #%d: NO\n",++cas);
        else
            printf("Case #%d: %d\n",++cas,sum-w[0]);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
