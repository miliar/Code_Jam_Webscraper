#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <utility>
#include <sstream>
#include <algorithm>
using namespace std;
#define ll long long
const long long LINF = ~(((long long)0x1)<<63)/2;
const int INF=0X3F3F3F3F;
const double eps=1e-7;
struct Node
{
    Node(){};
    int d,i;
    Node(int _p,int _d)
    {
        i=_p;d=_d;
    }
};
int a[11000][2];
int dp[11000];
int main()
{
    int T,i,j,k,cas;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(cas=1;cas<=T;cas++)
    {
        queue<Node> Q;
        int n,D;
        scanf("%d",&n);
        for(i=0;i<n;i++) scanf("%d%d",&a[i][0],&a[i][1]);
        scanf("%d",&D);
        Q.push(Node(0,a[0][0]));
        bool flag=false;
        memset(dp,0,sizeof(dp));
        while(!Q.empty())
        {
            Node p=Q.front();
            Q.pop();
            if(p.d+a[p.i][0]>=D)
            {
                flag=true;
                break;
            }
            for(j=p.i+1;j<n;j++)
                if(a[p.i][0]+p.d<a[j][0])
                    break;
                else
                {

                        int value=min(a[j][0]-a[p.i][0],a[j][1]);
                        if(dp[j]<value)
                        {
                            dp[j]=value;
                            Q.push(Node(j,value));
                        }
                }
        }
        printf("Case #%d: ",cas);
        if(flag)
            puts("YES");
        else
            puts("NO");
    }
    return 0;
};
