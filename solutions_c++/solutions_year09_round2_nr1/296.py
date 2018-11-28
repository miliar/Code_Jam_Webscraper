#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#define MAXN 110
#define MAXL 100010
using namespace std;
vector <string> tinh[MAXN];
double p[MAXL];
double kq;
int con[MAXL][2];
int ntest, L, N, num;
string name[MAXN], c[MAXL];

void doc(int u)
{
     char tam;
     scanf("%c",&tam);
     while (tam!='(') scanf("%c",&tam);
     scanf("%lf",&p[u]);
     scanf("%c",&tam);
     while ((tam<'a' || tam>'z') && tam!=')') scanf("%c",&tam);
     if (tam==')') 
     {
        c[u]="";
        return;
     }
     c[u]=tam;
     while (true)
     {
           scanf("%c",&tam);
           if (tam>='a' && tam<='z')
              c[u]+=tam;
           else
               break;
     }
     con[u][0]=++num;
     doc(num);
     con[u][1]=++num;
     doc(num);
     scanf("%c",&tam);
     while (tam!=')') scanf("%c",&tam);
}

void dfs(int u, int cur)
{
     kq*=p[u];
     if (con[u][0] && con[u][1])
     {
        for (int i=0; i<tinh[cur].size(); i++)
            if (tinh[cur][i]==c[u])
            {

               dfs(con[u][0],cur);
               return;         
            }    
        dfs(con[u][1],cur);
     }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.ou","w",stdout);
    
    scanf("%d\n",&ntest);
    for (int test=1; test<=ntest; test++)
    {
        memset(con,0,sizeof(con));
        printf("Case #%d:\n",test);
        scanf("%d\n",&L);
        num=1;
        doc(1);
        scanf("%d\n",&N);
        for (int i=1; i<=N; i++)
        {
            char tam[20];
            scanf("%s",&tam);
            name[i]=tam;
            int sl;
            scanf("%d",&sl);
            tinh[i].clear();
            tinh[i].resize(sl);
            for (int j=0; j<sl; j++)
            {
                char c;
                scanf("%c",&c);
                while (c<'a' || c>'z') scanf("%c",&c);                
                tinh[i][j]=c;
                while (true)
                {
                      scanf("%c",&c);
                      if (c>='a' && c<='z')
                         tinh[i][j]+=c;
                      else
                          break;
                }
            }                          
            scanf("\n");
            kq=1.0;
            dfs(1,i);
            printf("%.9lf\n",kq);
        }
    }
    
    return 0;
}
