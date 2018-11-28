#include <iostream>
#include <fstream>
#include <stdio.h>
#include <sstream>
#include <string>

using namespace std;
int MAX_L = 20;
int MAX_N = 500;
int MAX_D = 5000;

int main(){
    ifstream fin("A-large.in",ios::in);
    ofstream fout("A-large.out", ios::out);
    int L,D,N;
    char c;
    fin>>L>>D>>N;
    char buffer[1000];
    fin.getline( buffer,1000,'\n');
    
    cout<<L<<D<<N;
    //system("pause");
    
    char word[MAX_D][MAX_L];
    for ( int i = 0 ; i < D ; i++ ){
        cout<<i<<endl;
        fin.getline(buffer,MAX_L);
        for ( int j = 0 ; j < L ; j++ ) word[i][j] = buffer[j];
        for ( int j = 0 ; j < L ; j++ ) cout<<word[i][j];
        cout<<endl;
        //system("pause");
    }
    
    char receiptWord[MAX_N][MAX_L][100];
    for ( int i = 0 ; i < N ; i++ ){
        fin.getline(buffer,MAX_L*100);
        int k = 0;
        for ( int j = 0 ; j < strlen(buffer) ; j++ ){
            if ( (char)buffer[j] == '(' ){
                 j++;
                 int t = 0;
                 while ( (char)buffer[j] != ')' ) {
                       receiptWord[i][k][t] = buffer[j];
                       t++;
                       j++;
                       }
            } else {
                   receiptWord[i][k][0] = buffer[j];
                   //cout<<i<<" "<<k<<" "<<receiptWord[i][k][0]<<endl;
            }
            k++;
        }
    }
    
    for ( int i = 0 ; i < N ; i++ ) {
        int count = 0;
            for ( int j = 0 ; j < D ; j++ )  {
                bool d = false;
                for ( int k = 0 ; k < L ; k ++)  {
                    bool c = false;
                    for ( int t = 0 ; t < strlen(receiptWord[i][k]); t++ ) if ( word[j][k] == receiptWord[i][k][t] ) {
                        c = true;
                        break;
                        }
                    if ( !c ) break;
                    if ( k == L - 1 ) d = true;
                }
                if ( d ) count++;
            }
        fout<<"Case #"<<i+1<<": "<<count<<endl;
        }
    system("pause");
    }
