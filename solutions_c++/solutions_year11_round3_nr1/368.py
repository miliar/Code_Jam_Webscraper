#include <cstdio>

using namespace std;

int main()
{
    int T;
    scanf("%d",&T);
    for (int t=1;t<=T;++t)
    {
        int R,C;
        printf("Case #%d:\n",t);
        scanf("%d%d",&R,&C);
        char s[100][100];
        for (int i=0;i<R;++i)
            scanf("%s",s[i]);
        bool f = true;
        for (int i=0;i<R&&f;++i)
            for (int j=0;j<C&&f;++j)
                if (s[i][j]=='#')
                {
                    if (s[i+1][j]=='#' && s[i][j+1]=='#' && s[i+1][j+1]=='#')
                    {
                        s[i][j] = s[i+1][j+1] ='/';
                        s[i+1][j] = s[i][j+1] = '\\';
                    }
                    else
                        f=0;
                }
        if (f)
            for (int i=0;i<R;++i)
                printf("%s\n",s[i]);
        else
            printf("Impossible\n");
    }

    return 0;
}
