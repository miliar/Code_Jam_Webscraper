#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<fstream>

using namespace std;

int main( void ){
    ifstream inFile("data.in");
    ofstream outFile("data.out");
    int i,j,k,m,n,t,r,c;
    char a[500][500];
    inFile >> t;
    for( int q = 0 ; q < t ; q++ ){
        inFile >> r >> c;
        bool flag = false;
        outFile << "Case #" << q+1 << ":" << endl;
        for( i = 0 ; i < r ; i++ )
        for( j = 0 ; j < c ; j++ )
            inFile >> a[i][j];
        for( i = 0 ; i < r ; i++ ){
            for( j = 0 ; j < c ; j++ ){
                if( a[i][j] == '#' ){
                    if( i < r - 1 && j < c - 1 && a[i][j+1] == '#' && a[i+1][j] == '#' && a[i+1][j+1] == '#' ){
                        a[i][j] = '/' ;
                        a[i][j+1] = '\\' ;
                        a[i+1][j] = '\\' ;
                        a[i+1][j+1] = '/' ;
                    }else{
                        flag = true;
                        break;
                    }
                }
            }
        }
        if( flag ){
            outFile << "Impossible" << endl;
        }else{
            for( i = 0 ; i < r ; i++ ){
                for( j = 0 ; j < c ; j++ )
                    outFile << a[i][j];
                outFile << endl;
            }
        }
    }
    inFile.close();
    outFile.close();
    return 0;
}
