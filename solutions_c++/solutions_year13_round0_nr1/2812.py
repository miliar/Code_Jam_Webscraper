#include <iostream>
#include <cstdio>
using namespace std;

char s[6][6];

int check (char p1, char p2, char p3, char p4)
{
    if (p1 == 'T')
        swap (p1, p2);
    if (p1 == '.') return 0; 
    if (p2 != p1 && p2 != 'T') return 0;
    if (p3 != p1 && p3 != 'T') return 0;
    if (p4 != p1 && p4 != 'T') return 0;
    
    return p1=='X'? 1 : 2;
        
}

string solve ()
{
    getchar();
    int i;
    for (i = 0 ; i < 4; i ++)
    {
        gets (s[i]);
    }
 
    int ret = 0; 
    for (i = 0; i < 4; i ++)
    {
        ret |= check (s[i][0], s[i][1], s[i][2], s[i][3]);
        ret |= check (s[0][i], s[1][i], s[2][i], s[3][i]);
        
    }
    
    int dot = 0, j;
    for (i = 0; i < 4; i ++)
        for (j = 0; j < 4; j ++)
            dot |= (s[i][j] == '.');
    
    ret |= check (s[0][0], s[1][1], s[2][2], s[3][3] );
    ret |= check (s[3][0], s[2][1], s[1][2], s[0][3] );
    
    switch (ret)
    {
        case 0: return dot==0? "Draw" : "Game has not completed";
        case 1: return "X won";
        case 2: return "O won";
        case 3: return "Draw";
    }
    return "This shit shouldn't happen!!";
}


int main ()
{
    int t;
    scanf ("%d", &t);
    
    int i;
    for (i = 1; i <=t; i ++)
    {
        printf ("Case #%d: %s\n", i, solve().c_str());
    }
       return 0;
}