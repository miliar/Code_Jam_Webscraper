#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in;
    in.open("A-large.in");
    
    ofstream out;
    out.open("output.txt");
    
    int noc=0;
    in >> noc;
    
    
    for (int z=0; z<noc; z++)
    {
        out << "Case #" << z+1 << ":\n" ;
        
        int r=0, c=0;
        in >> r >> c;
        
        char arr[r][c];
        for (int i=0; i<r; i++)
        {
            for (int j=0; j<c; j++)
            {
                in >> arr[i][j];    
            }    
        }
        
        for (int i=0; i<r; i++)
        {
            for (int j=0; j<c; j++)
            {
                if (arr[i][j]=='#' && (arr[i][j+1]=='#' && j+1<=c) && (arr[i+1][j]=='#' && i+1<=r) && arr[i+1][j+1]=='#')
                {
                   arr[i][j]='/';
                   arr[i][j+1]='\\';
                   arr[i+1][j]='\\';
                   arr[i+1][j+1]='/';
                }
            }    
        }
        
        bool found = false;
        
        for (int i=0; i<r; i++)
        {
            for (int j=0; j<c; j++)
            {
                if (arr[i][j] == '#')
                {
                   found = true;
                   break;              
                }
            }
            if (found == true)
               break;
        }
        
        if (found == true)
        {
           out << "Impossible\n" ;          
        }
        else
        {
            for (int i=0; i<r; i++)
            {
                for (int j=0; j<c; j++)
                {
                    out << arr[i][j];    
                }
                out << "\n" ;
            }
        }
    }

    //system("pause");
    return 0;
}
