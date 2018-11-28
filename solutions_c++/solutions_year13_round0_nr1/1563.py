#include <cstdio>
#include <iostream>

using namespace std;

char a[4][5];

int main()
{
    int t;

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    
    cin >> t;
    
    for (int i = 1; i <= t; i++)
    {
        bool ok = false;
        
        for (int j = 0; j < 4; j++) scanf("%s", &a[j]);

        for (int j = 0; j < 4; j++) 
        {
            if (((a[j][0] == 'O' || a[j][0] == 'T') && 
                 (a[j][1] == 'O' || a[j][1] == 'T') && 
                 (a[j][2] == 'O' || a[j][2] == 'T') && 
                 (a[j][3] == 'O' || a[j][3] == 'T')) ||
                ((a[0][j] == 'O' || a[0][j] == 'T') && 
                 (a[1][j] == 'O' || a[1][j] == 'T') && 
                 (a[2][j] == 'O' || a[2][j] == 'T') && 
                 (a[3][j] == 'O' || a[3][j] == 'T')))
            {
                printf("Case #%d: O won\n", i); ok = true;
                goto L1;        
            }
        }
        
        if (((a[0][0] == 'O' || a[0][0] == 'T') && 
             (a[1][1] == 'O' || a[1][1] == 'T') && 
             (a[2][2] == 'O' || a[2][2] == 'T') && 
             (a[3][3] == 'O' || a[3][3] == 'T')) ||
            ((a[0][3] == 'O' || a[0][3] == 'T') && 
             (a[1][2] == 'O' || a[1][2] == 'T') && 
             (a[2][1] == 'O' || a[2][1] == 'T') && 
             (a[3][0] == 'O' || a[3][0] == 'T')))
        {
            printf("Case #%d: O won\n", i); ok = true;
            goto L1;        
        }
        
        ///////////////////////////////////////////////////////////////////////////////
        
        for (int j = 0; j < 4; j++) 
        {
            if (((a[j][0] == 'X' || a[j][0] == 'T') && 
                 (a[j][1] == 'X' || a[j][1] == 'T') && 
                 (a[j][2] == 'X' || a[j][2] == 'T') && 
                 (a[j][3] == 'X' || a[j][3] == 'T')) ||
                ((a[0][j] == 'X' || a[0][j] == 'T') && 
                 (a[1][j] == 'X' || a[1][j] == 'T') && 
                 (a[2][j] == 'X' || a[2][j] == 'T') && 
                 (a[3][j] == 'X' || a[3][j] == 'T')))
            {
                printf("Case #%d: X won\n", i); ok = true;
                goto L1;        
            }
        }
        
        if (((a[0][0] == 'X' || a[0][0] == 'T') && 
             (a[1][1] == 'X' || a[1][1] == 'T') && 
             (a[2][2] == 'X' || a[2][2] == 'T') && 
             (a[3][3] == 'X' || a[3][3] == 'T')) ||
            ((a[0][3] == 'X' || a[0][3] == 'T') && 
             (a[1][2] == 'X' || a[1][2] == 'T') && 
             (a[2][1] == 'X' || a[2][1] == 'T') && 
             (a[3][0] == 'X' || a[3][0] == 'T')))
        {
            printf("Case #%d: X won\n", i); ok = true;
            goto L1;        
        }
        
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
            {
                if (a[j][k] == '.') 
                {
                    printf("Case #%d: Game has not completed\n", i); ok = true;
                    goto L1;        
                }
            }
		}
        
        L1:
            
        if (!ok)
        {
            printf("Case #%d: Draw\n", i);        
        }       
    }    
}
