#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <string>
using namespace std;


class Coord
{
    public:     
    long x, y;
    
    Coord(){}
    Coord( long xi, long yi )
    {
        this->x = xi;
        this->y = yi;
    }
};

int main()
{
	int nc;
	cin >> nc;
    
	for( int q=0; q<nc; q++ )
    {
        long long n, A, B, C, D, x0, y0, M;
        vector<Coord> v;
        vector<Coord>::iterator vi1, vi2, vi3, vi4, vi5;
        
        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
        
        long long X = x0;
        long long Y = y0;
        
        v.push_back( Coord( X, Y ) );
        
        for( long long i = 1; i < n ; i++ )
        {
            X = ( A * X + B ) % M;
            Y = ( C * Y + D ) % M;
            v.push_back( Coord( X, Y ) );
        }
              
        long long licznik = 0, k=0;
       
        /*for(vi1 = v.begin(); vi1 != v.end(); ++vi1)
        {     
            cout << "-- " << (*vi1).x << "   " << (*vi1).y << endl; 
        }*/
               
        for(vi1 = v.begin(); vi1 != v.end() - 2; ++vi1)
        {       
            for(vi2 = vi1+1; vi2 != v.end() - 1; ++vi2)
            {
                for(vi3 = vi2+1; vi3 != v.end(); ++vi3)
                {
                    long double nX = 0, nY = 0;
                    k++;
                    
                    //cout << "*" << (*vi1).x << " " << (*vi2).x << " " << (*vi3).x << endl;
                    //cout << "*" << (*vi1).y << " " << (*vi2).y << " " << (*vi3).y << endl;
                    
                    nX = ( (*vi1).x + (*vi2).x + (*vi3).x ) / 3.0;
                    nY = ( (*vi1).y + (*vi2).y + (*vi3).y ) / 3.0; 
                    
                    //cout << nX << "  " << nY << endl;  
                    
                    if( nX == (long long)nX && nY == (long long)nY ) 
                    {
                        licznik++;
                    }
     
                }
            }
            
        }
        
        //cout << "{" << k << "}" << endl;
        
	    cout << "Case #" << q+1 << ": " << licznik << endl;
    }
    
	return 0;
}
