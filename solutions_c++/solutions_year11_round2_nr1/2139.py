#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <queue>
#include <cstdlib>
#define MAXN 105
using namespace std;
int tt, n, sum, s;
double cnt;
struct Node
{
    char chara[MAXN];
    double wp, owp, oowp;
    int face;
}node[MAXN];

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    scanf("%d", &tt);
    for(int t=1; t<=tt; t++)
    {
        scanf("%d", &n);
        for(int i=0; i<n; i++)
        scanf("%s", node[i].chara);
        for(int i=0; i<n; i++)
        {
            s=0;sum=n;
            for(int j=0; j<n; j++)
            {
                if(node[i].chara[j]=='1') s++;
                if(node[i].chara[j]=='.') sum--;
            }
            node[i].wp=1.0*s/sum;
            node[i].face=sum;
        }
        for(int i=0; i<n; i++)
        {
            cnt=0;
            for(int j=0; j<n; j++)
            {
                if(node[i].chara[j]!='.')
                {
                    s=0;sum=n-1;
                    for(int k=0; k<n; k++)
                    {
                        if(i!=k)
                        {
                            if(node[j].chara[k]=='1') s++;
                            if(node[j].chara[k]=='.') sum--;
                        }
                    }
                    cnt+=1.0*s/sum;
                }
            }
            node[i].owp=1.0*cnt/node[i].face;
        }
        for(int i=0; i<n; i++)
        {
            cnt=0;
            for(int j=0; j<n; j++)
            {
                if(node[i].chara[j]!='.')
                cnt+=node[j].owp;
            }
            node[i].oowp=1.0*cnt/node[i].face;
        }
        printf("Case #%d:\n",t);
        for(int i=0; i<n; i++)
            printf("%lf\n", 0.25*node[i].wp+0.5*node[i].owp+0.25*node[i].oowp);
    }
    return 0;
}
