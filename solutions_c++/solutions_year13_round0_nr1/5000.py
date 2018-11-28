#include<cstdio>
using namespace std;

int N;
char data[5][5];
bool drawPossible = 1;

bool checkRows( char A )
{
    int flag;

    for(int i = 1;i <= 4;i++)
    {
        flag = 0;
        for(int j = 1;j <= 4;j++)
        {
            if(data[i][j] == 'T' || data[i][j] == A)flag++;
        }

        if(flag == 4)return 1;
    }

    return 0;
}

bool checkColumns( char A )
{
    int flag;

    for(int i = 1;i <= 4;i++)
    {
        flag = 0;
        for(int j = 1;j <= 4;j++)
        {
            if(data[j][i] == 'T' || data[j][i] == A)flag++;
        }

        if(flag == 4)return 1;
    }

    return 0;
}

bool checkDiag( char A )
{
    int flag = 0;
    if(data[1][1] == 'T' || data[1][1] == A)flag++;
    if(data[2][2] == 'T' || data[2][2] == A)flag++;
    if(data[3][3] == 'T' || data[3][3] == A)flag++;
    if(data[4][4] == 'T' || data[4][4] == A)flag++;
    if(flag == 4)return 1;

    flag = 0;
    if(data[4][1] == 'T' || data[4][1] == A)flag++;
    if(data[3][2] == 'T' || data[3][2] == A)flag++;
    if(data[2][3] == 'T' || data[2][3] == A)flag++;
    if(data[1][4] == 'T' || data[1][4] == A)flag++;
    if(flag == 4)return 1;

    return 0;
}


bool checkAll( char A )
{
    if( checkDiag( A ) )return 1;
    if( checkRows( A ) )return 1;
    if( checkColumns( A ) )return 1;
    return 0;
}

void solve(int counter)
{
    drawPossible = 1;

    for(int i = 1;i <= 4;i++)
     for(int j = 1;j <= 4;j++)
     {
        do
        {
            scanf("%c", &data[i][j]);
        }while( data[i][j] != 'T' && data[i][j] != 'O' && data[i][j] != 'X' && data[i][j] != '.' );

        if(data[i][j] == '.')drawPossible = 0;
     }

    if( checkAll('X') ){ printf("Case #%d: X won\n", counter); return; }
    if( checkAll('O') ){ printf("Case #%d: O won\n", counter); return; }

    (drawPossible)? printf("Case #%d: Draw\n", counter) : printf("Case #%d: Game has not completed\n", counter);
}

int main()
{
    scanf("%d", &N);
    for(int i = 1;i <= N;i++)solve(i);
    return 0;
}
