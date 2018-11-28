#include<iostream>
#include<fstream>

using namespace std;

int main( void ){
    int n,a,b,c,i,j,k,p,flag,z;
    char f[40][3],d[30][2],buf[200],t;
    ofstream outFile( "ans2.txt" );
    
    cin >> n;
    for( i = 0 ; i < n ; i++ ){
        cin >> a;
        for( j = 0 ; j < a ; j++ ){
            cin >> f[j][0] >> f[j][1] >> f[j][2];
        }
        cin >> b;
        for( j = 0 ; j < b ; j++ ){
            cin >> d[j][0] >> d[j][1];
        }
        cin >> c;
        p = 0;
        for( j = 0 ; j < c ; j++ ){
            cin >> t;
            buf[p] = t;
            while( p > 0 ){
                flag = 0;
                for( k = 0 ; k < a ; k++ ){
                    if( ( buf[p] == f[k][1] && buf[p-1] == f[k][0] ) || ( buf[p] == f[k][0] && buf[p-1] == f[k][1] ) ){
                        buf[--p] = f[k][2];
                        flag = 1;
                        break;
                    }
                }
                if( flag == 0 ) break;
            }
            flag = 0;
            for( k = 0 ; k < b ; k++ ){
                for( z = 0 ; z < p ; z++ ){
                    if( ( buf[p] == d[k][0] && buf[z] == d[k][1] ) || ( buf[p] == d[k][1] && buf[z] == d[k][0] ) ){
                        flag = 1;
                        p = -1;
                        break;
                    }
                }
                if( flag == 1 ) break;
            }
            p++;
        }
        outFile << "Case #" << i+1 << ": " << "[";
        for( j = 0 ; j < p ; j++ ){
            outFile << buf[j];
            if( j != p - 1 ) outFile << ", ";
        }
        outFile << "]" << endl;
    }
    return 0;
}
