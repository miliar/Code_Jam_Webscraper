#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
#define maxn 300
struct Node{
    double sc;
    int id;
}nd[maxn];
bool cmp(const Node &nd1,const Node &nd2)
{
    return nd1.sc > nd2.sc;
}
double ans[maxn];
int main()
{
    int T,n;
    int i,j,k,cnt,cs;
    double sum,left;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    while(scanf("%d",&T)!=EOF)
    {
        cs = 1;
        while(T--)
        {
            sum = 0.0;
            scanf("%d",&n);
            for(i = 0 ;i < n ; i++)
            {
                scanf("%lf",&nd[i].sc);
                nd[i].id = i;
                sum += nd[i].sc;
            }

            sort(nd,nd + n,cmp);
            left = sum;
            cnt = n;
            printf("Case #%d:",cs++);
            for(i = 0 ; i < n; i++)
            {
                if((left + sum) < nd[i].sc*cnt)
                {
                    ans[nd[i].id] = 0.0;
                    left -= nd[i].sc;
                    cnt--;
                }
                else
                {
                    ans[nd[i].id] = ((left + sum)/(double)cnt - nd[i].sc)/sum;
                }

            }
            for(i = 0;i < n; i++)
                printf(" %.6lf",ans[i]*100);
            printf("\n");
        }

    }
    return 0;
}
