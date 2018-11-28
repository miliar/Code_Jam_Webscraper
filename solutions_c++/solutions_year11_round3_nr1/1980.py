/*
ID: dhxav
PROG: b
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

int main()
{
    ofstream fout ("A-small-attempt0.out");
    ifstream fin ("A-small-attempt0.in");
    
    int T;
    int R, C;
    char tile[50][50];
    int check;
    
    fin >> T;

    for (int i=0; i<T; i++)
    {
        fin >> R >> C;
        
        check = 1;
        
        for (int j=0; j<R; j++)
            fin >> tile[j];
            
        for (int j=0; j<R; j++)
        {
            if (check==0)
               break;
            for (int k=0; k<C; k++)
            {
                if (tile[j][k]=='#')
                {
                   if (j==R-1 || k==C-1)
                   {
                      check = 0;
                      break;
                   }
                   else if (tile[j][k+1]=='#' && tile[j+1][k]=='#' && tile[j+1][k+1]=='#')
                   {
                        tile[j][k] = '/';
                        tile[j][k+1] = '\\';
                        tile[j+1][k] = '\\';
                        tile[j+1][k+1] = '/';
                   }
                   else
                   {
                       check = 0;
                       break;
                   }
                }
            }
        }
                         
        fout << "Case #" << i+1 << ":" << endl;
        if (check==0)
           fout << "Impossible" << endl;
        else
        {
            for (int j=0; j<R; j++)
                fout << tile[j] << endl;
        }
    }
    
    return 0;
}
