#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char s[120];
char st[120];
int C,D,N;
char mp[200][200];
bool del[200][200];

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);

    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        memset(mp, 0, sizeof(mp));
        memset(del, 0, sizeof(del));
        scanf("%d",&C);
        for(int i = 0; i < C; i++)
        {
            scanf("%s",s);
            mp[s[0]][s[1]] = s[2];
            mp[s[1]][s[0]] = s[2];
        }
        scanf("%d",&D);
        for(int i = 0; i < D; i++)
        {
            scanf("%s",s);
            del[s[0]][s[1]] = 1;
            del[s[1]][s[0]] = 1;
        }
        scanf("%d%s",&N,s);
        int top = 0;
        for(int i = 0; i < N; i++)
        {
            char c = s[i];
            while(top)
            {
                if(mp[c][st[top]])
                {
                    c = mp[c][st[top]];
                    top--;
                }
                else break;
            }
            bool d = 0;
            for(int j = 1; j <= top; j++)
                if(del[c][st[j]])d = 1;
            if(d){top = 0;continue;}
            st[++top] = c;
        }
        printf("Case #%d: [",++cas);
        for(int i = 1; i <= top; i++)
        {
            printf("%c",st[i]);
            if(i!=top)printf(", ");
        }
        puts("]");

    }

    return 0;
}
