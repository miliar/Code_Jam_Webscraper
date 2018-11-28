
#include <iostream>
#include <vector>
#include <list>
#include <map>

char **pic;
int r, c;
bool pintar( int i, int j)
{
    if(pic[i][j]!='#')
    {
        if(j+1 == c)
        {
            ++i;
            if(i == r)
            {
                return true;
            }
        }
        j = ((j + 1) % c);
        return pintar(i, j);
    }
    else
    {   
        if(j+1 == c || pic[i][j+1]!='#')
        {
            return false;
        }
        if(i+1 == r|| pic[i][j+1]!='#' ||  pic[i+1][j]!='#' || pic[i+1][j+1]!='#')
        {
            return false;
        }
        pic[i][j] = '/';
        pic[i][j+1] = '\\';
        pic[i+1][j] = '\\';
        pic[i+1][j+1] = '/';
        ++j;
        return pintar(i,j);
    }
}
using namespace std;
//~ for(int i = 0; i < n; ++i)
int main()
{
    int t;
    cin >> t;
    for(int i =0 ; i < t; ++i)
    {
        cin >> r >> c;
        pic = new char *[r];
        for(int j=0; j < r; ++j)
        {
            pic[j] = new char[c];
        } 
        for(int j=0; j < r; ++j)
        {
            for(int k =0; k < c; ++k)
            {
                cin >> pic[j][k];
            }
        }
        cout << "Case #" << i +1 << ":" << endl;
        if(pintar(0,0))
        {
            
            for(int j=0; j < r; ++j)
            {
                for(int k =0; k < c; ++k)
                {
                    cout << pic[j][k];
                }
                cout << endl;
            }
        }
        else
        {
            cout << "Impossible" << endl;
             
        }
        
        for(int j=0; j < r; ++j)
        {
            delete [] pic[j];
        }
        delete [] pic; 
    }
    
    
    return 0;
}
