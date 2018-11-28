#include <iostream>
#define MAXN 5010
using namespace std;
int l, n, ntest, kq;
bool ok[MAXN][MAXN];
string p[MAXN];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.ou","w",stdout);
    
    scanf("%d%d%d\n",&l,&n,&ntest);
    for (int i=1; i<=n; i++)
    {
        char tam[MAXN];
        scanf("%s\n",&tam);
        p[i]=tam;
    }
    for (int test=1; test<=ntest; test++)
    {
        char tam[MAXN];
        scanf("%s\n",&tam);
        int lim=strlen(tam);
        memset(ok,false,sizeof(ok));
        int id=-1;
        bool in=false;
        for (int i=0; i<lim; i++)
            if (tam[i]=='(')
            {
               id++;
               in=true;
            }
            else
                if (tam[i]==')')
                   in=false;
                else
                    if (in)
                       ok[id][tam[i]]=true;
                    else
                    {
                        id++;
                        ok[id][tam[i]]=true;
                    }
        kq=0;
        for (int i=1; i<=n; i++)
        {
            bool duoc=true;
            for (int j=0; j<p[i].length(); j++)
                if (!ok[j][p[i][j]])
                {
                   duoc=false;
                   break;
                }
            if (duoc) kq++;
        }
        printf("Case #%d: %d\n",test,kq);
    }
    
    return 0;
}
