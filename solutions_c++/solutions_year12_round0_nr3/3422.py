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

bool vis[3000000];
int A,B;
int ans;

int main()
{
   // freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d%d",&A,&B);
        ans=0;
        memset(vis,0,sizeof(vis));
        for(int i=A;i<B;i++)
        {
            int k1=10,k2;
            if(i<10) k2=1;
            else if(i<100) k2=10;
            else if(i<1000) k2=100;
            else if(i<10000) k2=1000;
            else if(i<100000) k2=10000;
            else if(i<1000000) k2=100000;
            else k2=1000000;
            while(k1<=i)
            {
                int t=i/k1+i%k1*k2;
                if(t<=B)

                if(t<=B&&t>i&&!vis[t])
                {
                    vis[t]=true;
                    ans++;
                }
                k1*=10;
                k2/=10;
            }
            k1=10;
            if(i<10) k2=1;
            else if(i<100) k2=10;
            else if(i<1000) k2=100;
            else if(i<10000) k2=1000;
            else if(i<100000) k2=10000;
            else if(i<1000000) k2=100000;
            else k2=1000000;
            while(k1<=i)
            {
                int t=i/k1+i%k1*k2;
                vis[t]=false;
                k1*=10;
                k2/=10;
            }
        }
        printf("Case #%d: %d\n",cas,ans);
    }
	return 0;
}
