#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int MaxN = 105;
double w[MaxN],o[MaxN], oo[MaxN];
char g[MaxN][MaxN];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d",&n);
        for(int i = 0; i < n; i++)
        {
            scanf("%s",g[i]);
            int ct = 0, tot = 0;
            for(int j = 0; j < n; j++)
                if(g[i][j] != '.')
                {
                    tot++;
                    if(g[i][j]=='1')ct++;
                }
            w[i] = (double)ct/tot;
            //printf("1: %f\n",w[i]);
        }
        for(int i = 0; i < n; i++)
        {
            int tot = 0;
            double s = 0;
            for(int j = 0; j < n; j++)
                if(g[i][j]!='.')
                {
                    tot++;
                    int ct = 0, tt = 0;
                    for(int k = 0; k < n; k++)
                        if(k!=i && g[j][k]!='.')
                        {
                            ct++;
                            if(g[j][k]=='1')tt++;
                        }
                    s += (double)tt/ct;
                }
            o[i] = s/tot;
            //printf("2: %f\n",o[i]);
        }
        for(int i = 0; i < n; i++)
        {
            int tot = 0;
            double s = 0;
            for(int j = 0; j < n; j++)
                if(g[i][j]!='.')
                {
                    tot++;
                    s += o[j];
                }
            oo[i] = s/tot;
        }
        printf("Case #%d:\n",++cas);
        for(int i = 0; i < n; i++)
            printf("%.7f\n",0.25*w[i]+0.50*o[i]+0.25*oo[i]);
    }

    return 0;
}
