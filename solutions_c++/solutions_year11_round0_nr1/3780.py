#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
using namespace std;
#define maxn 1000
int val1[maxn];
int val2[maxn];
struct Node
{
    char ch;
    int val;
}nd[maxn];
int t,n;
int main()
{
    int i;
    int t1,t2,ans,tmp,cs;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    while(scanf("%d",&t)!=EOF)
    {
        cs = 1;
        while(t--)
        {
            scanf("%d",&n);
            t1 = t2 = 1;
            for(i = 0; i < n; i++)
            {
                scanf("%c%c%d",&nd[i].ch,&nd[i].ch,&nd[i].val);
                if(nd[i].ch == 'O')
                {
                    val1[t1++] = nd[i].val;
                }
                else
                {
                    val2[t2++] = nd[i].val;
                }
            }
            if(t1 != 1)
                val1[0] = val1[1];
            if(t2 != 1)
                val2[0] = val2[1];
            int p1,p2,pos1,pos2;
            p1 = p2 = 1;
            pos1 = pos2 = 1;
            ans = 0;
            for(i=0;i<n;i++)
            {
                if(nd[i].ch == 'O')
                {
                    tmp = abs(val1[p1] - pos1) + 1;
                    ans += tmp;
                    if(val2[p2] > pos2)
                        pos2 = (pos2 + tmp) > val2[p2] ? val2[p2]:(pos2 + tmp);
                    else
                        pos2 = (pos2 - tmp) > val2[p2] ? (pos2 - tmp) : val2[p2];
                    pos1 = val1[p1];
                    p1++;
                }
                else
                {
                    tmp = abs(val2[p2] - pos2) + 1;
                    ans += tmp;
                    if(val1[p1] > pos1)
                        pos1 = (pos1 + tmp) > val1[p1] ? val1[p1]:(pos1 + tmp);
                    else
                        pos1 = (pos1 - tmp) > val1[p1] ? (pos1 - tmp) : val1[p1];
                    pos2 = val2[p2];
                    p2++;
                }
            }
            printf("Case #%d: %d\n",cs++,ans);
        }
    }
    return 0;
}
