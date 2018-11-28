#include<stdio.h>
#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string.h>
#include<math.h>

#define MAX 2*100000000

int p[200],v[200];
int i,j,k,m,n,t,d;
double l,r,w;

using namespace std;

bool go( double time )
{
    double left = p[0] - time;
    for( int i = 0 ; i < n ; i++ ){
        for( int j = 0 ; j < v[i] ; j++ ){
            double tmp = left + d;
            if( p[i] + time < tmp ) return false;
            if( p[i] - time > tmp )
                tmp = p[i] - time;
            if( tmp > left + d )
                left = tmp;
            else
                left = left + d;
        }
    }
    return true;
}

int main( void ){
    ifstream inFile( "data.in" );
    ofstream outFile( "data.out" );
    
    inFile >> t;
    for( int z = 0 ; z < t ; z++ ){
        inFile >> n >> d;
        for( i = 0 ; i < n ; i++ )
            inFile >> p[i] >> v[i];
        for( i = 0 ; i < n - 1 ; i++ )
            for( j = 0 ; j < n - i - 1 ; j++ )
                if( p[j] > p[j+1] ){
                    int tmp = p[j];
                    p[j] = p[j+1];
                    p[j+1] = tmp;
                    tmp = v[j];
                    v[j] = v[j+1];
                    v[j+1] = tmp;
                }
        v[0]--;
        l = 0; r = MAX;
        while( r - l > 0.000001 ){
            w = ( l + r ) / 2;
            if( w < 2 ){
                
            }
            if( go( w ) )
                r = w;
            else
                l = w;
        }
        outFile << "Case #" << z+1 << ": " << w << endl;
    }
    inFile.close();
    outFile.close();
    return 0;
}
