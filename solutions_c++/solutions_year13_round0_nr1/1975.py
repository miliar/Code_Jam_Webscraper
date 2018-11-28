//Aleksander Łukasiewicz
#include<cstdio>
using namespace std;

int t;
int rows[10], columns[10];
char board[10][10];

inline void read()
{
    for(int i=1; i<=4; i++)
	scanf("%s", board[i]+1);
}

bool check(char player)
{
    for(int i=1; i<=4; i++) rows[i] = columns[i] = 0;
    for(int i=1; i<=4; i++) for(int j=1; j<=4; j++)
	if(board[i][j]==player || board[i][j]=='T')
	    rows[i]++, columns[j]++;
    for(int i=1; i<=4; i++)
	if(rows[i]==4 || columns[i]==4) return true;

    int d1=0, d2=0;
    for(int i=1; i<=4; i++)
    {
	if(board[i][i]==player || board[i][i]=='T') d1++;
	if(board[i][4-i+1]==player || board[i][4-i+1]=='T') d2++;
    }
    return (d1==4 || d2==4);
}

inline bool draw()
{
    for(int i=1; i<=4; i++) for(int j=1; j<=4; j++)
	if(board[i][j]=='.') return false;
    return true;
}

int main()
{
    scanf("%d", &t);
    for(int i=1; i<=t; i++)
    {
	printf("Case #%d: ", i);
	read();
	if(check('X')) puts("X won");
	else if(check('O')) puts("O won");
	else if(draw()) puts("Draw");
	else puts("Game has not completed");
    }

return 0;
}