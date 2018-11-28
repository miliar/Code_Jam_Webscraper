#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

int f(int s)
{
    switch(s)
    {
        case 4*'X':
        case 3*'X'+'T': return 'X';
        case 4*'O':
        case 3*'O'+'T': return 'O';
        default: return 0;
    }
}


int main(void)
{
    int T;
    char a[8][8];
    
    cin >> T;
    
    for(int cst = 1; cst <= T; ++cst)
    {
        for(int i = 0; i < 4; ++i)
            scanf("%s", a[i]);
            
        int flag = 0;
        for(int i = 0; i < 4; ++i)
        {
            flag = f(a[i][0]+a[i][1]+a[i][2]+a[i][3]);
            if(flag) goto END;
            
            flag = f(a[0][i]+a[1][i]+a[2][i]+a[3][i]);
            if(flag) goto END;
        }
        
        flag = f(a[0][0]+a[1][1]+a[2][2]+a[3][3]);
        if(flag) goto END;
        
        flag = f(a[3][0]+a[2][1]+a[1][2]+a[0][3]);
        if(flag) goto END;
        
        for(int i = 0; i < 4; ++i)
        {
            for(int j = 0; j < 4; ++j)
            {
                if(a[i][j] == '.')
                {
                    flag = 1;
                    goto END;
                }
            }
        }
        
        END:
        switch(flag)
        {
            case 0: printf("Case #%d: Draw\n", cst); break;
            case 1: printf("Case #%d: Game has not completed\n", cst); break;
            case 'X': printf("Case #%d: X won\n", cst); break;
            case 'O': printf("Case #%d: O won\n", cst); break;
        }
    }
}
