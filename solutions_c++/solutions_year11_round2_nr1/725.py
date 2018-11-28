#include<stdio.h>
#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<string.h>
#include<math.h>

using namespace std;

int main( void ){
    ifstream inFile( "data.in" );
    ofstream outFile( "data.out" );
    char a[100][100];
    double wp[100] = {0},owp[100] = {0},oowp[100]={0};
    double rpi[100] = {0};
    int i,j,k,t,n,l;
    inFile >> t;
    for( int z = 0 ; z < t ; z++ ){
        inFile >> n;
        for( i = 0 ; i < n ; i++ ){
            for( j = 0 ; j < n ; j++ ){
                inFile >> a[i][j];
            }
        }
        for( i = 0 ; i < n ; i++ ){
            int win = 0,lose = 0;
            for( j = 0 ; j < n ; j++ ){
                if( a[i][j] == '1' )
                    win++;
                else if( a[i][j] == '0' )
                    lose++;
            }
            wp[i] = (double)win / ( win + lose );
        }
        for( i = 0 ; i < n ; i++ ){
            int count = 0;
            double sum = 0;
            for( j = 0 ; j < n ; j++ ){
                if( a[j][i] == '.' ) continue;
                int win = 0,lose = 0;
                for( k = 0 ; k < n ; k++ ){
                    if( k != i ){
                        if( a[j][k] == '1' )
                            win++;
                        else if( a[j][k] == '0' )
                            lose++;
                    }
                }
                sum += ( double ) win / ( win + lose );
                count++;
            }
            if( count == 0 ){
                owp[i] = 0;
                continue;
            }
            owp[i] = sum / count;
            /*
            for( j = 0 ; j < n ; j++ ){
                if( a[i][j] != '.' ){
                    sum += wp[j];
                    count ++;
                }
            }
            owp[i] = sum / count;
            */
        }
        for( i = 0 ; i < n ; i++ ){
            int count = 0;
            double sum = 0;
            for( j = 0 ; j < n ; j++ ){
                if( a[i][j] != '.' ){
                    sum += owp[j];
                    count ++;
                }
            }
            oowp[i] = sum / count;
        }
        for( i = 0 ; i < n ; i++ ){
            rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
        }
        outFile << "Case #" << z+1 << ":" << endl;
        for( i = 0 ; i < n ; i++ )
            outFile << rpi[i] << endl;
    }
    inFile.close();
    outFile.close();
    return 0;
}
