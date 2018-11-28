/*
TASK: Diamond Inheritance
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
vector<int> v[1005];
int N,M,T;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("xxx1.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int ii=0;
    queue<int> Q;
    int chk[1005];
    while(T--)
    {
        ii++;
        scanf("%d",&N);
        for(i=1;i<=N;i++)
        {
            scanf("%d",&M);
            for(j=1;j<=M;j++)
            {
                scanf("%d",&k);
                v[i].push_back(k);
            }
        }
        bool ok=false;
        for(int iii=1;iii<=N;iii++)
        {
            Q.push(iii);
            memset(chk,0,sizeof chk);
            chk[iii]=1;
            while(!Q.empty())
            {
                k=Q.front();
                Q.pop();
//                printf("%d\n",k);
                if(ok)  continue;
                for(i=0;i<v[k].size();i++)
                {
                    if(chk[v[k][i]]!=0)
                    {
                        ok=true;
                        break;
                    }
                    else
                    {
                        Q.push(v[k][i]);
//                        printf("--%d\n",v[k][i]);
                        chk[v[k][i]]=1;
                    }
                }
                chk[k]=2;
            }
//            system("pause");
        }
        if(ok)  printf("Case #%d: Yes\n",ii);
        else    printf("Case #%d: No\n",ii);
        for(i=1;i<=N;i++)
            v[i].clear();
    }
}
