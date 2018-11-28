#include <iostream>
#include <string>
#include <stdlib.h>

int row(char array[][4]);
int col(char array[][4]);
int diag(char array[][4]);
int blank (char array[][4]);

int main()
{
    char array[4][4];
    int tot;
    std::cin >> tot;
    int i = 0;
    int j = 0;
    int counter = 0;
    int X = 0;
    int O = 0;
    int N = 0;

    for(i=0; i<4; i++)
        for(j = 0; j<4; j++)
            array[i][j] = '.';

    i = 0;
    while(counter<tot)
    {
        X = 0;
        O = 0;
        N = 0;
        i = 0;
        j = 0;
        for(i=0; i<4; i++)
            for(j = 0; j<4; j++)
                std::cin >> array[i][j];

  /*      for(i=0; i<4; i++)
        {
            for(j = 0; j<4; j++)
                std::cout << array[i][j];
            std::cout << "\n";
        }*/
        i = 0;
        j = 0;
        if(row(array) == 2 || col(array) == 2 || diag(array) == 2)
        {
            std::cout << "Case #" << counter+1 << ": X won";
            X = 1;
        }
        if(row(array) == 1 || col(array) == 1 || diag(array) == 1)
        {
            std::cout << "Case #" << counter+1 << ": O won";
            O = 1;
        }
        if(blank(array) == 1 && X == 0 && O == 0)
        {
            std::cout << "Case #" << counter+1 << ": Game has not completed";
            N = 1;
        }
        if(X == 0 && O == 0 && N == 0)
        {
            std::cout << "Case #" << counter+1 << ": Draw";
        }

        std::cout << "\n";
        i = 0;
        j = 0;

        for(i=0; i<4; i++)
            for(j = 0; j<4; j++)
                array[i][j] = '.';
        counter++;
   //     std::cout << "here";
    }

    return 0;
}

int row(char array[][4])
{
    int i = 0;
    int j = 0;

    while(i<4)
    {
        while(j<4)
        {
            if((array[i][j] == 'T' || array[i][j] == 'X') && array[i][(j+1)%4] == 'X' && array[i][(j+2)%4] == 'X' && array[i][(j+3)%4] == 'X')
                return 2;
            j++;
        }
        i++;
        j = 0;
    }

    i = 0;
    j = 0;
//std::cout << "HERE";
    while(i<4)
    {
        while(j<4)
        {
            if((array[i][j] == 'T' || array[i][j] == 'O') && array[i][(j+1)%4] == 'O' && array[i][(j+2)%4] == 'O' && array[i][(j+3)%4] == 'O')
                return 1;
            j++;
        }
        i++;
        j = 0;
    }
    return 0;
}

int col(char array[][4])
{
    int i = 0;
    int j = 0;

    while(j<4)
    {
        while(i<4)
        {
            if((array[i][j] == 'T' || array[i][j] == 'X') && array[(i+1)%4][j] == 'X' && array[(i+2)%4][j] == 'X' && array[(i+3)%4][j] == 'X')
                return 2;
            i++;
        }
        j++;
        i = 0;
    }

    i = 0;
    j = 0;

    while(j<4)
    {
        while(i<4)
        {
            if((array[i][j] == 'T' || array[i][j] == 'O') && array[(i+1)%4][j] == 'O' && array[(i+2)%4][j] == 'O' && array[(i+3)%4][j] == 'O')
                return 1;
            i++;
        }
        j++;
        i = 0;
    }
    return 0;
}

int diag(char array[][4])
{
    int i = 0;

  /*      while(i<4)
        {
            if((array[i][i] == 'T' || array[i][i] == 'X') && array[(i+1)%4][(i+1)%4] == 'X' && array[(i+2)%4][(i+2)%4] == 'X' && array[(i+3)%4][(i+3)%4] == 'X')
                return 2;
            i++;
        }*/
    i = 0;
    if(array[0][0] == 'X' && array[1][1] == 'X' && array[2][2] == 'X' && array[3][3] == 'X')
        return 2;
    if(array[0][0] == 'T' && array[1][1] == 'X' && array[2][2] == 'X' && array[3][3] == 'X')
        return 2;
    if(array[0][0] == 'X' && array[1][1] == 'T' && array[2][2] == 'X' && array[3][3] == 'X')
        return 2;
    if(array[0][0] == 'X' && array[1][1] == 'X' && array[2][2] == 'T' && array[3][3] == 'X')
        return 2;
    if(array[0][0] == 'X' && array[1][1] == 'X' && array[2][2] == 'X' && array[3][3] == 'T')
        return 2;

    if(array[0][3] == 'X' && array[1][2] == 'X' && array[2][1] == 'X' && array[3][0] == 'X')
        return 2;
    if(array[0][3] == 'T' && array[1][2] == 'X' && array[2][1] == 'X' && array[3][0] == 'X')
        return 2;
    if(array[0][3] == 'X' && array[1][2] == 'T' && array[2][1] == 'X' && array[3][0] == 'X')
        return 2;
    if(array[0][3] == 'X' && array[1][2] == 'X' && array[2][1] == 'T' && array[3][0] == 'X')
        return 2;
    if(array[0][3] == 'X' && array[1][2] == 'X' && array[2][1] == 'X' && array[3][0] == 'T')
        return 2;

    if(array[0][0] == 'O' && array[1][1] == 'O' && array[2][2] == 'O' && array[3][3] == 'O')
        return 1;
    if(array[0][0] == 'T' && array[1][1] == 'O' && array[2][2] == 'O' && array[3][3] == 'O')
        return 1;
    if(array[0][0] == 'O' && array[1][1] == 'T' && array[2][2] == 'O' && array[3][3] == 'O')
        return 1;
    if(array[0][0] == 'O' && array[1][1] == 'O' && array[2][2] == 'T' && array[3][3] == 'O')
        return 1;
    if(array[0][0] == 'O' && array[1][1] == 'O' && array[2][2] == 'O' && array[3][3] == 'T')
        return 1;

    if(array[0][3] == 'O' && array[1][2] == 'O' && array[2][1] == 'O' && array[3][0] == 'O')
        return 1;
    if(array[0][3] == 'T' && array[1][2] == 'O' && array[2][1] == 'O' && array[3][0] == 'O')
        return 1;
    if(array[0][3] == 'O' && array[1][2] == 'T' && array[2][1] == 'O' && array[3][0] == 'O')
        return 1;
    if(array[0][3] == 'O' && array[1][2] == 'O' && array[2][1] == 'T' && array[3][0] == 'O')
        return 1;
    if(array[0][3] == 'O' && array[1][2] == 'O' && array[2][1] == 'O' && array[3][0] == 'T')
        return 1;

 /*   while(i<4)
    {
        if((array[i][3-i] == 'T' || array[i][3-i] == 'X') && array[(i+1)%4][(2-i)%4] == 'X' && array[(i+2)%4][(1-i)%4] == 'X' && array[(i+3)%4][(-i)%4] == 'X')
            return 2;
        i++;
    }

    i = 0;

        while(i<4)
        {
            if((array[i][i] == 'T' || array[i][i] == 'O') && array[(i+1)%4][(i+1)%4] == 'O' && array[(i+2)%4][(i+2)%4] == 'O' && array[(i+3)%4][(i+3)%4] == 'O')
                return 1;
            i++;
        }

    i = 0;
    while(i<4)
    {
        if((array[i][3-i] == 'T' || array[i][3-i] == 'O') && array[(i+1)%4][(2-i)%4] == 'O' && array[(i+2)%4][(1-i)%4] == 'O' && array[(i+3)%4][(-i)%4] == 'O')
            return 1;
        i++;
    }
*/


    return 0;
}

int blank(char array[][4])
{
    int i = 0;
    int j = 0;
    for(i = 0; i<4; i++)
        for(j = 0; j<4; j++)
            if(array[i][j] == '.')
                return 1;

}

