/*
TASK: Swinging Wild
LANG: C++
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
using namespace std;
#define X first
#define Y second
int N,M,T;
int a[10005],b[10005];
queue<pair<int,int> > Q;
pair<int,int> pr;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    int tt=0;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&N);
        for(i=1;i<=N;i++)
            scanf("%d%d",&a[i],&b[i]);
        scanf("%d",&M);
        pr.X=1; pr.Y=a[1];
        Q.push(pr);
        bool ok=false;
        int x,y;
        while(!Q.empty())
        {
            x=Q.front().X;
            y=Q.front().Y;
            Q.pop();
//            printf("[%d %d]\n",x,y);
            if(a[x]+y>=M)
            {
                ok=true;
                break;
            }
            for(i=x+1;i<=N;i++)
            {
                if(a[i]<=a[x]+y)
                {
                    pr.X=i;
                    pr.Y=min(a[i]-a[x],b[i]);
//                    printf("%d %d)\n",pr.X,pr.Y);
                    if(pr.Y>0)
                        Q.push(pr);
                }
            }
        }
        while(!Q.empty())
            Q.pop();
        tt++;
        if(ok)
            printf("Case #%d: YES\n",tt);
        else
            printf("Case #%d: NO\n",tt);
    }
}
