#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
#define M 105
int T;
int c,d,n;
string C,D;
char st[M],N[M];
int used[M];
void solve()
{
    for (int num=1;num<=T;num++)
    {
        C="";
        D="";
        scanf("%d",&c);
        if (c>0)
            cin>>C;
        scanf("%d",&d);
        if (d>0)
            cin>>D;
        cin>>n;
        cin>>N;
        int i,j,top=0;
        memset(st,0,sizeof(st));
        for (i=0;i<n;i++)
        {
            if (i==0) st[top++]=N[i];
            else
            {
                if (N[i]==C[0] && st[top-1]==C[1])
                {
                    st[top-1]=C[2];
                    N[i]=C[2];
                }
                else if (N[i]==C[1] && st[top-1]==C[0])
                {
                    st[top-1]=C[2];

                    N[i]=C[2];
                }
                else if (N[i]==D[0])
                {
                    bool find=0;
                    for (j=top-1;j>=0;j--)
                        if (st[j]==D[1]) find=1;
                    if (find==1)
                    {
                        memset(st,0,sizeof(st));
                        top=0;
                        continue;
                    }
                    else st[top++]=N[i];
                }
                else if (N[i]==D[1])
                {
                    bool find=0;
                    for (j=top-1;j>=0;j--)
                        if (st[j]==D[0]) find=1;
                    if (find==1)
                    {
                        memset(st,0,sizeof(st));
                        top=0;
                        continue;
                    }
                    else st[top++]=N[i];
                }
                else st[top++]=N[i];
            }
        }
        printf("Case #%d: [",num);
        if (strlen(st)>0)
            putchar(st[0]);
        for (i=1;i<strlen(st);i++)
            printf(", %c",st[i]);
        printf("]\n");
    }
}
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    scanf("%d",&T);
    solve();
}
