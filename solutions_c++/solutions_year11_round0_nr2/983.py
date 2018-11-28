#include<assert.h>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>
#include<set>
#include<vector>
#include<queue>

using namespace std;

#define FOR(i,n) for(int i=0;i<(n);++i)
#define REP(i,a,b) for(int i=(a);i<=(b);++i)
#define CLR(a,x) memset(a,(x),sizeof(a))

typedef long long LL;
typedef pair<int,int> pii;

char combines[300][300];
bool enemy[300][300];
char str[300], ans[300];
int F, E, N;


int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int T; scanf("%d",&T);

    REP(kase,1,T)
    {
        CLR(combines,-1);
        CLR(enemy,0);

        scanf("%d",&F);
        FOR(i,F)
        {
            char temp[5];
            scanf("%s",temp);
            combines[temp[0]][temp[1]] = combines[temp[1]][temp[0]] = temp[2];
        }

        scanf("%d",&E);
        FOR(i,E)
        {
            char temp[5];
            scanf("%s",temp);
            enemy[temp[0]][temp[1]] = enemy[temp[1]][temp[0]] = 1;
        }

        scanf("%d",&N);
        scanf("%s",str);
        int endPos = -1;

        FOR(i,N)
        {
            char ch;
            // try to combine first
            if(endPos>=0 && (ch=combines[str[i]][ans[endPos]])!=-1)
            {
                ans[endPos] = ch;
            }
            else
            {
                bool destroy = 0;
                REP(j,0,endPos)
                {
                    if(enemy[ans[j]][str[i]]) destroy = 1;
                }

                if(destroy)
                {
                    endPos = -1;
                }
                else
                    ans[++endPos] = str[i];
            }
        }

        printf("Case #%d: ",kase);
        printf("[");

        REP(i,0,endPos)
        {
            if(i>0) printf(", ");
            printf("%c",ans[i]);
        }

        printf("]\n");
    }

    return 0;
}
