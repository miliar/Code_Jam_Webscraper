#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <algorithm>
#include <utility>

using namespace std;

typedef char t_grille[4][4] ;


int verification_ligne (t_grille& Grille, int Ligne) // 0 si aucun , 1 si X , 2 si O
{
    int i ;
    if (Grille[Ligne][0] == '.' )
    {
        return 0;
    }
    else
    {
        if (Grille[Ligne][0] != 'T' )
        {
            for (i=1;i<4;i++)
            {
                if (Grille[Ligne][i] != Grille[Ligne][0] && Grille[Ligne][i] != 'T')
                {
                    return 0;
                }
            }
            if (Grille[Ligne][0] == 'O' )
            {
            return 2 ;
            }
            else
            {
            return 1 ;
            }
        }
        else  // si la 1ere case est un T
        {
        if (Grille[Ligne][1] == '.')
          {
              return 0 ;
          }
            for (i=2;i<4;i++)
            {
                if (Grille[Ligne][i] != Grille[Ligne][1] )
                {
                    return 0;
                }
            }
            if (Grille[Ligne][1] == 'O' )
                {
                return 2 ;
                }
            else
                {
                return 1 ;
                }
        }
    }
}

int verification_colonne (t_grille& Grille, int Col) // 0 si aucun , 1 si X , 2 si O
{
    int i  ;
    if (Grille[0][Col] == '.' )
    {
        return 0;
    }
    else
    {
        if (Grille[0][Col] != 'T' )
        {
            for (i=1;i<4;i++)
            {
                if (Grille[i][Col] != Grille[0][Col] && Grille[i][Col] != 'T')
                {
                    return 0;
                }
            }
            if (Grille[0][Col] == 'O' )
            {
            return 2 ;
            }
            else
            {
            return 1 ;
            }
        }
        else  // si la 1ere case est un T
        {
          if (Grille[1][Col] == '.')
          {
              return 0 ;
          }
          else
          {
            for (i=2;i<4;i++)
            {
                if (Grille[i][Col] != Grille[1][Col] )
                {
                    return 0;
                }
            }
            if (Grille[1][Col] == 'O' )
                {
                return 2 ;
                }
            else
                {
                return 1 ;
                }
           }
        }
    }
}

int verification_diagonale_gauche (t_grille& Grille)
{
    int i ;
    if (Grille[0][0] == '.')
    {
        return 0 ;
    }
    else
    {
        if (Grille[0][0] != 'T')
        {
            for (i=1;i<4;i++)
            {
                if (Grille[i][i] != Grille[0][0] && Grille [i][i] != 'T')
                {
                    return 0;
                }
            }
            if (Grille[0][0] == 'O')
            {
                return 2 ;
            }
            else
            {
                return 1 ;
            }
        }
        else
        {
            if (Grille[1][1] == '.')
            {
                return 0 ;
            }
            for (i=2;i<4;i++)
            {
                if (Grille[i][i] != Grille[1][1] && Grille [i][i] != 'T')
                {
                    return 0;
                }
            }
            if (Grille[1][1] == 'O')
            {
                return 2 ;
            }
            else
            {
                return 1 ;
            }
        }
    }
}

int verification_diagonale_droite (t_grille& Grille)
{
    int i ;
    if (Grille[0][3] == '.')
    {
        return 0 ;
    }
    else
    {
        if (Grille[0][3] != 'T')
        {
            for (i=1;i<4;i++)
            {
                if (Grille[i][3-i] != Grille[0][3] && Grille [i][3-i] != 'T')
                {
                    return 0;
                }
            }
            if (Grille[0][3] == 'O')
            {
                return 2 ;
            }
            else
            {
                return 1 ;
            }
        }
        else
        {
            if (Grille[1][2] == '.')
            {
                return 0 ;
            }
            for (i=2;i<4;i++)
            {
                if (Grille[i][3-i] != Grille[1][2] && Grille [i][3-i] != 'T')
                {
                    return 0;
                }
            }
            if (Grille[1][2] == 'O')
            {
                return 2 ;
            }
            else
            {
                return 1 ;
            }
        }
    }
}

int verification_grille (t_grille& Grille)
{
    int temp,i;
    temp = verification_diagonale_droite (Grille) ;
    if (temp != 0)
    {
        return temp ;
    }
    temp = verification_diagonale_gauche (Grille) ;
    if (temp != 0)
    {
        return temp ;
    }
    for (i=0;i<4;i++)
    {
        temp = verification_colonne (Grille,i);
        if (temp != 0)
        {
            return temp ;
        }
        temp = verification_ligne (Grille,i);
        if (temp != 0)
        {
            return temp ;
        }
    }
    return temp ;
}

int grille_complete (t_grille& Grille) //retourne 0 si pas complete
{
    int i,j ;
    for (i=0;i<4;i++)
    {
        for (j=0;j<4;j++)
        {
            if (Grille[i][j] == '.')
            {
                return 0;
            }
        }
    }
    return 1;
}



int main ()
{
    t_grille Grille ;

ifstream file("A-large.in", ifstream::in);
ofstream file2("out.txt", ofstream::out);

int nb;
file >> nb;

for(int i = 0; i < nb; ++i)
{
    char c;
    for(int j=0;j < 4; ++j)
    {
        for (int k=0;k<4;++k)
        {
            file >> c;
            Grille [j][k] = c ;
        }
    }

    int temp ;
    temp = verification_grille (Grille) ;
    if (temp == 1)
    {
        file2 << "Case #" << i+1 << ": X won" << std::endl;
    }
    else if ( temp == 2)
    {
        file2 << "Case #" << i+1 << ": O won" << std::endl;
    }
    else if (grille_complete(Grille) == 0)
    {
         file2 << "Case #" << i+1 << ": Game has not completed" << std::endl;
    }
    else
    {
         file2 << "Case #" << i+1 << ": Draw" << std::endl;
    }
}
    return 0;

}

