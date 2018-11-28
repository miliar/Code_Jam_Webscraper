#include <stdio.h>
#include <memory.h>

char word[5005][20];
bool K[20][30];
int len, d;

bool isLet( char c )
{
    if( c<='z' && c>='a' ) return true;
    return false;
}

void read( int i )
{
    char c;
    while(1)
    {
    c = getchar();
    if( c == '(' || isLet(c) ) break;
    }
    if( c != '(' )
    {
    K[i][c-'a']=true;
    return;
    }
    while(1)
    {   
        c = getchar();
        if( c == ')' ) break;
        K[i][ c-'a' ] = true;
    }
}

int match()
{
    int i, j, sum = 0;
    for(i=0; i<d; ++i)
    {
        for(j=0; j<len; ++j)
        {
        if( !K[j][ word[i][j]-'a' ] ) break;
        }
            if( j == len ) sum++;
    }
    return sum;
}

int main()
{
    int n, i, j;
    freopen("A-large.in", "r", stdin);
    freopen("out2.txt", "w", stdout);
    scanf("%d %d %d", &len, &d, &n);
    for(i=0; i<d; ++i) scanf("%s", word[i]);
    for(i=0; i<n; ++i)
    {
        memset(K, 0, sizeof(K));
        for(j=0; j<len; ++j) read(j);
        printf("Case #%d: %d\n", i+1, match());
    }
//    getchar();    getchar();
return 0;
}
