#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int maxn = 10010;
const int maxm = 104;

bool g[maxn][26]; // i has j
bool f[maxn][26]; // i !ok in j
int list[maxn], list0[maxn];
char word[maxn][11];
int len[maxn];
char str[maxm][27];
int ans[maxm], ansi[maxm];
int cas, n, m;

void solve(int k )
{
    for (int i = 0; i<n; i++ )
    {
        if (len[i] == len[k])
            for (int j = 0; word[k][j]; j++ )
                if (word[k][j] != word[i][j])
                {
                    f[i][word[k][j]-'a'] = 1;
                    f[i][word[i][j]-'a'] = 1;
                }
    }
    int tot = 0, totTmp;
    for (int i = 0; i<n; i++ )
        if (len[i] == len[k] && i!=k) list0[tot++] = i;
    totTmp = tot;
    //cout<<k<<endl;
    for (int t = 0; t<m; t++ )
    {
        memcpy(list, list0, sizeof(list0));
        tot = totTmp;
        int score = 0;
        for (int p = 0; p<26 && tot; p++ )
        {
            int ch = str[t][p] - 'a';
            //cout<<ch;
            bool has = g[k][ch];
            for (int i = 0; i<tot && !has; i++ )
                if (g[list[i]][ch]) has = 1;
            if (!has) continue;
            if (g[k][ch])
            {
                int tot0 = 0;
                for (int i = 0; i<tot; i++ )
                    if (!f[list[i]][ch]) list[tot0++] = list[i];
                tot = tot0;
                if (tot == 0) break;
            }
            else
            {
                ++score;
                int tot0 = 0;
                for (int i = 0; i<tot; i++ )
                    if (!g[list[i]][ch]) list[tot0++] = list[i];
                tot = tot0;
                if (tot == 0) break;
            }
        }
        //cout<<endl<<"score  "<<t<<' '<<score<<endl<<endl;
        if (tot!=0) cout<<"yes"<<endl;
        if (score>ans[t])
        {
            ans[t] = score;
            ansi[t] = k;
        }
    }
}

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small-attempt1.out","w",stdout);
    scanf("%d",&cas);
    for (int run = 1; run<=cas; run++ )
    {
        memset(ans, -1, sizeof(ans));
        memset(g, 0, sizeof(g));
        scanf("%d%d",&n,&m);
        for (int i = 0; i<n; i++ )
        {
            scanf("%s",word[i]);
            len[i] = strlen(word[i]);
            for (int j = 0; word[i][j]; j++ )
                g[i][word[i][j]-'a'] = 1;
        }
        for (int i = 0; i<m; i++ )
            scanf("%s",str[i]);
        for (int k = 0; k<n; k++ )
        {
            memset(f, 0, sizeof(f));
            solve(k);
        }
        printf("Case #%d:",run);
        for (int i = 0; i<m; i++ )
            printf(" %s",word[ansi[i]]);
        printf("\n");
        //for (int i = 0; i<m; i++ )
          //  cout<<ans[i]<<endl;
    }
    //system("pause");
    fclose(stdin);
    fclose(stdout);
    return 0;
}
