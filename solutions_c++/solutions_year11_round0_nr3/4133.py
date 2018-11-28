#include <iostream>
#include <fstream>

using namespace std;

int main ()
{

    fstream fin ("C-large.in", ios::in);
    fstream fout ("C-large.out", ios::out);
    
    int candy[1000], n, tests, tc, i;
    int sum = 0,min = 0, xr = 0;
    
    fin >> tests;
    
    for (tc=1;tc<=tests;tc++){
        fin >> n;
        sum = 0;
        xr = 0;
        min = 10000000;
        
        for ( i=0 ; i<n ; i++ )fin >> candy[i];        
        
        for ( i=0; i<n; i++ ){
            if ( min > candy[i] ) min = candy [i];
            xr = xr xor candy[i] ;
            sum += candy[i] ;
        }
        
        if (xr == 0){
            sum -= min ;
            fout << "Case #" << tc << ": " << sum << "\n";            
        } else {
            fout << "Case #" << tc << ": NO" << "\n";            
        }
    
    }        
    
    fin.close();    
    fout.close();

    return 0;
}
