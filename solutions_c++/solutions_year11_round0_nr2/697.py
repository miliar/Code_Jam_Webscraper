#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
int opp[27][27];
char cmb[27][27];
int init()
{
    int i,j;
    for(i=0;i<27;i++)
    {
        for(j=0;j<27;j++)
        {
            opp[i][j] = -1;
            cmb[i][j] = '#';
        }
    }
    return 0;
}
int main()
{
    freopen("data.in","r",stdin);
    freopen("out.txt","w",stdout);
    int n,m,i,j,k,cs,t;
    char s[4];
    char ans[102],str[102];
    scanf("%d",&t);
    for(cs = 1;cs <= t;cs ++)
    {
        scanf("%d",&n);
        init();
        for(i=0;i<n;i++)
        {
            scanf("%s",s);
            cmb[s[1]-'A'][s[0]-'A'] = cmb[s[0]-'A'][s[1]-'A'] = s[2];
        }
        scanf("%d",&m);
        for(i=0;i<m;i++)
        {
            scanf("%s",s);
            opp[s[1]-'A'][s[0]-'A'] = opp[s[0]-'A'][s[1]-'A'] = 1;
        }
        scanf("%d",&n);
        scanf("%s",str);
        n = strlen(str);
        k = -1;
        for(i=0;i<n;i++)
        {
            if(i == 0) {ans[++k] = str[i];continue;}
            if(k >= 0 && cmb[str[i]-'A'][ans[k]-'A'] != '#')
            {
                ans[k] = cmb[str[i]-'A'][ans[k]-'A'];
            }
            else ans[++k] = str[i];
            if(k >= 0)
            {
                for(j=0;j<k;j++)
                {
                    if(opp[ans[j]-'A'][ans[k]-'A'] == 1) break;
                }
                if(j < k) k = -1;
            }
        }
        printf("Case #%d: [",cs);
        for(i=0;i<=k;i++)
        {
            if(i != 0) printf(" ");
            printf("%c",ans[i]);
            if(i != k) printf(",");
        }
        printf("]\n");
    }
    return 0;
}
