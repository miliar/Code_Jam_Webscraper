#include <cstdio>

using namespace std;
int T,R,C;
char map[64][64];
bool marked(int r,int c)
{
    if(map[r][c]=='/'||map[r][c]=='\\') return true;
    return false;
}
bool tag(int r,int c);
bool tag(int r,int c)
{
    if(map[r][c]!='#') return true;
    if(r==R-1||c==C-1) return false;
    if(map[r][c+1]!='#') return false;
    if(map[r+1][c]!='#') return false;
    if(map[r+1][c+1]!='#') return false;
        //mark
    map[r][c]='/';
    map[r+1][c]='\\';
    map[r][c+1]='\\';
    map[r+1][c+1]='/';
    return true;
}
int main()
{
    int round=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d%d",&R,&C);
        for(int i=0;i<R;i++)
        {
            scanf("%s",map[i]);
        }
        bool success=true;
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                if(!tag(i,j))
                {
                    success=false;
                    goto out;
                }
            }
        }
        out:
        printf("Case #%d:\n",round++);
        if(success)
        {
            for(int i=0;i<R;i++)
                printf("%s\n",map[i]);
        }else
        {
            printf("Impossible\n");
        }
    }
    return 0;
}
