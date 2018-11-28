#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <iostream>
#include <math.h>

using namespace std;

fstream inputFile;
ofstream outputFile;

bool GetNumberofCases(int *TotalNoCases)
{
    string s1;
    inputFile.getline((char*)s1.c_str(),80);
    *TotalNoCases = atoi(s1.c_str());
    return true;
}

void main(int argc, char*argv[])
{
    int TotalNoCases = 0;
    int Alphabets[1000];
    long TotalKeyPress = 0 ;
    int IKeyPress = 0;
    int temp = 0;
    int P, K, L ;

    inputFile.open(argv[1]);
    GetNumberofCases(&TotalNoCases);
    printf("Total # Test Cases = %d\n",TotalNoCases);

    outputFile.open(argv[2]);

    for(int TC = 1; TC <= TotalNoCases; TC++ )
    {
// maximum number of letters to place on a key (P), 
// the number of keys available (K) 
// and the number of letters in our alphabet (L) 
        inputFile >> P >> K >> L ;

        for(int i = 0; i < L; i ++)
        {
            inputFile >> Alphabets[i] ;
        }

        for(int i = 0; i < L - 1 ; i++)
        {
            for(int j = i + 1  ; j < L  ; j++)
            {
                if(Alphabets[i] < Alphabets[j] )
                {
                    temp = Alphabets[i] ;
                    Alphabets[i] = Alphabets[j];
                    Alphabets[j] = temp;
                }
            }
        }

        IKeyPress = 0 ;
        TotalKeyPress = 0;
        for(int i = 0 ; i < L ; i+= K )
        {
            IKeyPress++ ;
            for(int j = 0; j < K; j++)
            {
                if( ( i + j ) >= L )
                {
                    break ;
                }
                TotalKeyPress += Alphabets[i+j]*IKeyPress ;
            }
        }

        cout << "Case #" << TotalKeyPress << endl ;

        outputFile << "Case #" << TC << ": " << TotalKeyPress << endl ;
/*        if(IKeyPress <= P)
        {
            outputFile << "Case #" << TC << ": " << TotalKeyPress << endl ;
        }
        else
        {
            outputFile << "Case #" << TC << ": " << TotalKeyPress << endl ;
        }
*/
    }

    inputFile.close();
    outputFile.close();

}