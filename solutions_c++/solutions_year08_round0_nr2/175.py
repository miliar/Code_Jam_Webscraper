#include <stdio.h>
#include <string.h>
typedef struct
{
    int x, y;
}Train;
Train a[110], b[110];
int map[220][220];
int match[220];
int v[220];
int na, nb;
bool dfs( int p )
{
    if(v[p]) return false;
    v[p] = 1;
    for(int i = 0; i < na+nb; i++)
    {
        if( map[p][i] && ( match[i] == -1 || dfs(match[i]) ) )
        {
            match[i] = p;
            return true;
        }
    }
    return false;
}
void MaxMatch()
{
    memset( match, -1, sizeof( match ) );
    for(int i= 0; i < na+nb; i++)
    {
        memset( v, 0, sizeof( v ) );
        dfs(i);
    }
}

int main()
{
    freopen("B-large.in", "r", stdin );
    freopen("out.txt", "w", stdout );
    int kcase, s1, s2, t1, t2;
    int t;
    int tt=0;
    scanf("%d", &kcase);
    while(kcase--)
    {
        scanf("%d", &t);
        scanf("%d%d", &na, &nb );
        for( int i = 0; i < na; i++ )
        {
            scanf("%d:%d %d:%d", &s1, &s2, &t1, &t2 );
            a[i].x = s1*60+s2;
            a[i].y = t1*60+t2;
        }
        for( int i = 0; i < nb; i++ )
        {
            scanf("%d:%d %d:%d", &s1, &s2, &t1, &t2 );
            b[i].x = s1*60+s2;
            b[i].y = t1*60+t2;
        }
        memset( map, 0, sizeof( map ) );
        for( int i = 0; i < na; i++ )
        {
            for( int j = 0; j < nb; j++ )
            {
                if( a[i].y+t <= b[j].x )map[i][na+j]=1;
                if( b[j].y+t <= a[i].x )map[j+na][i]=1;
            }
        }
        MaxMatch();
        int ans1 = 0, ans2 = 0;
        for( int i = 0; i < na; i++ )if( match[i]==-1)ans1++;
        for( int j = na; j<na+nb;j++)if( match[j] == -1)ans2++;
        printf("Case #%d: %d %d\n", ++tt, ans1, ans2 );
    }
    return 0;
}
