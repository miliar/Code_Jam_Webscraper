#include<cstdio>
#include<string>

#define maxn 510
char dic[5010][40];
struct Word {
    int num[40];
    char ch[300];
}word[maxn];
bool flag[40];
int count[510];

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen ( "A-small-attempt0.out", "w", stdout );
    int L, D, N, cas;
    int i, j, k , l;
    char c[500];
    while ( scanf ( "%d%d%d", &L, &D, &N ) == 3 )
    {
        memset ( word, 0, sizeof ( word ) );
        memset ( dic, 0, sizeof ( dic ) );
        memset ( count, 0, sizeof ( count ) );
        for ( i = 0;i < D;i++ )
            scanf ( "%s", dic[i] );
        getchar();
        for ( cas = 0, j = 0; j < N;j++ )
        {
            memset ( c, 0, sizeof ( c ) );
            scanf ( "%s", c );
            for ( i = 0, k = 0, l = 0;c[i] != '\0';i++ , k++ )
            {
                if ( c[i] == '(' ) {
                    while ( c[++i] != ')' )
                    {
                        word[j].ch[l++] = c[i];
                        word[j].num[k]++;
                    }
                }
                else
                {
                    word[j].ch[l++] = c[i];
                    word[j].num[k]++;
                }
            }
            for ( int m = 0;m < N; m++ )
            {
                for (int i = 0;i < D;i++ )
                {
                    bool temp = true;
                    memset ( flag, false, sizeof ( flag ) );
                    for (int r =  k = 0;k < L;k++ )
                    {
                        for ( l = 0;l < word[m].num[k];l++, r++ ) {
                            if ( dic[i][k] == word[m].ch[r] )
                                flag[k] = true;
                        }
                    }
                    for ( int s = 0; s < L;s++ )
                        if ( !flag[s] ) {
                            temp = false;
                            break;
                        }
                    if ( temp )
                        count[m]++;
                }
            }
            printf ( "Case #%d: %d\n", ++cas, count[j] );
        }
    }
    return 0;
}