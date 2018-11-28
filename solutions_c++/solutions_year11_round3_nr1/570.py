/*
 * Google code jam: square files
 * 
 * Author: Jim
 * Date: 2011-05-07 Sun.
 */

#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <string.h>

using namespace std;
  


void solve();

int main(void)
{
    int n;

    freopen("in_1.txt","r",stdin); 
    freopen("out_1.txt","w",stdout); 


    //Add Your Code Here
    cin >> n;
    for(int i=0; i<n; i++)
    {
        cout <<"Case #"<<i+1<<": "<< endl;
        solve();
    }


    fclose(stdin);
    fclose(stdout);

    return EXIT_SUCCESS;
}

void solve()
{
    int n = 0;
    int m = 0;
    
    int i = 0;
    int j = 0;
    
    cin >> m >> n;
    
    char **b=new char*[m];
                                                       
    for(i=0;i<m;i++)
         b[i]=new char[n+1];
         
    for(i=0; i<m; i++)
    {
        cin >> b[i];         
    }
    /*
    for(i=0; i<m; i++)
    {
        cout << b[i] << endl;         
    }
    */
    for(i=0; i<m; i++)
    {
        for(j=0; j<n; j++)
        {
            if(b[i][j] == '#')
            {
                 if(  (j+1<n && b[i][j+1] == '#')
                         &&
                       (i+1<m && b[i+1][j] == '#' && b[i+1][j+1] == '#') 
                    )
                    {
                        b[i][j] = '/';
                        b[i][j+1] = '\\';
                        b[i+1][j] = '\\';
                        b[i+1][j+1] = '/';          
                    }          
            }         
        }
    } 
    
    for(i=0; i<m; i++)
    {
        for(j=0; j<n; j++)
        {
            if(b[i][j] == '#')
            {
                cout << "Impossible" << endl;
                return;           
            }         
        }
    }    
    
    for(i=0; i<m; i++)
    {
        cout << b[i] << endl;         
    }
    
}


