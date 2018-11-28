#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int T;
char a[4][5];


void calc2(int count)
{
    int i,j;
    for( i = j = 0;i < 4; ++i )
    {
        if( (a[i][j] == 'O' || a[i][j] == 'T') && (a[i][j+1] == 'O' || a[i][j+1] == 'T') && (a[i][j+2] == 'O' || a[i][j=2] == 'T') && (a[i][j+3] == 'O' || a[i][j+3] == 'T') )
        {
            printf("Case #%d: O won\n",count);
            return;
        }

        if( (a[i][j] == 'X' || a[i][j] == 'T') && (a[i][j+1] == 'X' || a[i][j+1] == 'T') && (a[i][j+2] == 'X' || a[i][j+2] == 'T') && (a[i][j+3] == 'X' || a[i][j+3] == 'T') )
        {
            printf("Case #%d: X won\n",count);
            return;
        }

    }

    for( j = i = 0;j < 4; ++j )
    {
        if( (a[i][j] == 'O' || a[i][j] == 'T') && (a[i+1][j] == 'O' || a[i+1][j] == 'T') && (a[i+2][j] == 'O' || a[i+2][j] == 'T') && (a[i+3][j] == 'O' || a[i+3][j] == 'T') )
        {
            printf("Case #%d: O won\n",count);
            return;
        }

         if( (a[i][j] == 'X' || a[i][j] == 'T') && (a[i+1][j] == 'X' || a[i+1][j] == 'T') && (a[i+2][j] == 'X' || a[i+2][j] == 'T') && (a[i+3][j] == 'X' || a[i+3][j] == 'T') )
        {
            printf("Case #%d: X won\n",count);
            return;
        }

    }

    if( (a[0][0] == 'O' || a[0][0] == 'T') && (a[1][1] == 'O' || a[1][1] == 'T') && (a[2][2] == 'O' || a[2][2] == 'T') && (a[3][3] == 'O' || a[3][3] == 'T') )
    {
            printf("Case #%d: O won\n",count);
            return;
    }

    if( (a[0][0] == 'X' || a[0][0] == 'T') && (a[1][1] == 'X' || a[1][1] == 'T') && (a[2][2] == 'X' || a[2][2] == 'T') && (a[3][3] == 'X' || a[3][3] == 'T') )
    {
            printf("Case #%d: X won\n",count);
            return;
    }



    if( (a[0][3] == 'O' || a[0][3] == 'T') && (a[1][2] == 'O' || a[1][2] == 'T') && (a[2][1] == 'O' || a[2][1] == 'T') && (a[3][0] == 'O' || a[3][0] == 'T') )
    {
            printf("Case #%d: O won\n",count);
            return;
    }

    if( (a[0][3] == 'X' || a[0][3] == 'T') && (a[1][2] == 'X' || a[1][2] == 'T') && (a[2][1] == 'X' || a[2][1] == 'T') && (a[3][0] == 'X' || a[3][0] == 'T') )
    {
            printf("Case #%d: X won\n",count);
            return;
    }

    for( i = 0;i < 4; ++i )
        for( j = 0; j < 4; ++j )
            if( a[i][j] == '.')
            {
                printf("Case #%d: Game has not completed\n",count );
                return;
            }
    printf("Case #%d: Draw\n",count);


}
int main()
{
     freopen("i.in","r",stdin);
     freopen("output.out","w",stdout);
    cin >> T;

    for( int count = 1; count <= T; ++count )
    {
        // scanf("%s",a[0]);
        // scanf("%s",a[1]);
        // scanf("%s",a[2]);
        // scanf("%s",a[3]);
        cin >> a[0] >> a[1] >> a[2] >> a[3];
        //printf("%s\n%s\n%s\n%s\n\n",a[0],a[1],a[2],a[3]);
        calc2(count);

    }

    return 0;
}
