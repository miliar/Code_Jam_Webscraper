#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>

using namespace std;

char b[5][5];

bool equal(char a, char t)
{
    return (a == t || a == 'T');
}
bool win(char c)
{
    int i, j;
    for(i = 0 ; i < 4; i++){
        if(!equal(b[i][i], c))
            break;
	}
    if(i == 4) return true;
    for(i = 0; i < 4; i++)
        if(!equal(b[3-i][i], c))
            break;
    if(i == 4) return true;

    for(i = 0; i < 4; i++){
        if(equal(b[i][0], c) && equal(b[i][1], c) && equal(b[i][2], c) && equal(b[i][3], c))
            return true;
        if(equal(b[0][i], c) && equal(b[1][i], c) && equal(b[2][i], c) && equal(b[3][i], c))
            return true;
	}
    return false;
}
int main()
{
	int T, cas = 1;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    while(T--){
        int empty = 0;
	    for(int i = 0; i < 4; i++){
		    scanf("%s", b[i]);
            for(int j = 0; j < 4; j++)
                if(b[i][j] == '.')
                    empty = 1;
		}
		printf("Case #%d: ", cas++);
        if(win('X'))
            puts("X won");
		else if(win('O'))
            puts("O won");
		else if(!empty)
            puts("Draw");
		else
            puts("Game has not completed");
	}
    return 0;
}

