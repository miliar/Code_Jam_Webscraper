#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

int c,d,n;
char str[5],tem[200];
int conbine[30][30],st[200],top,cases=1;
bool opp[30][30];

bool check_opp(int k)
{
    for(int i=1;i<=top;++i)
        if(opp[st[i]][k])
            return true;
    return false;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    while(t--)
    {
        memset(conbine,-1,sizeof(conbine));
        memset(opp,false,sizeof(opp));
        scanf("%d",&c);
        for(int i=0;i<c;++i)
        {
            scanf("%s",str);
            conbine[str[0]-'A'][str[1]-'A']=conbine[str[1]-'A'][str[0]-'A']=str[2]-'A';
        }
        scanf("%d",&d);
        for(int i=0;i<d;++i)
        {
            scanf("%s",str);
            opp[str[0]-'A'][str[1]-'A']=opp[str[1]-'A'][str[0]-'A']=true;
        }
        scanf("%d",&n);
        scanf("%s",tem);
        top=0;
        for(int i=0;tem[i];++i)
        {
            int u=tem[i]-'A';
            if(top==0)
            {
                st[++top]=u;
            }
            else
            {
                int v=st[top];
                if(conbine[u][v]!=-1)
                {
                    st[top]=conbine[u][v];
                }
                else
                {
                    if(check_opp(u))
                    top=0;
                    else
                    st[++top]=u;
                }
            }
        }
        printf("Case #%d: [",cases++);
        for(int i=1;i<=top;++i)
        {
            if(i==top)
            printf("%c",st[i]+'A');
            else
            printf("%c, ",st[i]+'A');
        }
        printf("]\n");
    }
    return 0;
}
