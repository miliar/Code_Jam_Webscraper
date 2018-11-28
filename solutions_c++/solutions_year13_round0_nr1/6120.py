#include <stdio.h>

int main (void)
{
    int n, contador = 0;
    scanf("%d", &n);
    
    char t[4][4];
    
    while (n > 0)
    {
        char aux;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
            {
                scanf("%c", &aux);
                (aux == '\n') ? j-- : t[i][j] = aux;
            }
        
        // Total de vitórias de X e O
        int vx = 0, vo = 0;              
        int n_t, n_x, n_o;
        bool p_existe = false;
        
        // Checa linhas
        for (int i = 0; i < 4; i++)
        {
            n_t = n_x = n_o = 0;
            for (int j = 0; j < 4; j++)
                switch (t[i][j])
                {
                    case 'X' : ++n_x; break;
                    case 'O' : ++n_o; break;
                    case 'T' : ++n_t; break;
                    case '.' : p_existe = true; break;                
                }
            if (n_x == 4 || (n_x == 3 && n_t == 1))
                vx++;
            else if (n_o == 4 || (n_o == 3 && n_t == 1))
                vo++;     
        }
        
        // Checa colunas
        for (int j = 0; j < 4; j++)
        {
            n_t = n_x = n_o = 0;
            for (int i = 0; i < 4; i++)
                switch (t[i][j])
                {
                    case 'X' : ++n_x; break;
                    case 'O' : ++n_o; break;
                    case 'T' : ++n_t; break;       
                }
            if (n_x == 4 || (n_x == 3 && n_t == 1))
                vx++;
            else if (n_o == 4 || (n_o == 3 && n_t == 1))
                vo++;     
        }
        
        // Checa diagonal que desce 
        n_t = n_x = n_o = 0;
        for (int i = 0; i < 4; i++)
            switch (t[i][i])
            {
                case 'X' : ++n_x; break;
                case 'O' : ++n_o; break;
                case 'T' : ++n_t; break;                
            }  
            
        if (n_x == 4 || (n_x == 3 && n_t == 1))
            vx++;
        else if (n_o == 4 || (n_o == 3 && n_t == 1))
            vo++; 
        
        // Checa diagonal que sobe
        n_t = n_x = n_o = 0;
        for (int i = 0; i < 4; i++)
            switch (t[i][3 - i])
            {
                case 'X' : ++n_x; break;
                case 'O' : ++n_o; break;
                case 'T' : ++n_t; break;                
            }  
            
        if (n_x == 4 || (n_x == 3 && n_t == 1))
            vx++;
        else if (n_o == 4 || (n_o == 3 && n_t == 1))
            vo++; 
        
		++contador;
        if (vx > vo)
            printf("Case #%d: X won\n", contador);
        else if (vo > vx)
            printf("Case #%d: O won\n", contador);
        else if (vo == vx && !p_existe)
            printf("Case #%d: Draw\n", contador);
        else if (vo == vx && p_existe)
            printf("Case #%d: Game has not completed\n", contador);
            
        n--;
    }
    
    return 0;
}