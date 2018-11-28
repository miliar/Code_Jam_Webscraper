

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;




//----------------------------------------------------------------------
// theme park
int main(int argc, char** argv)
{
    if( argc != 2 )
    {
        return -1;
    }

    string filename = argv[1];



    ifstream fin( filename.c_str() );
    ofstream fout( "result.out" );


    if( fin.fail() )
    {
        return -1;
    }
    if( fout.fail() )
    {
        return -1;
    }



    unsigned int T;
    unsigned int R, k, N;

    unsigned int *Queue;
    unsigned int *posQueue;
    unsigned int *lastPos;

    unsigned int total = 0;
    unsigned int subTotal;


    fin >> T;


    for( unsigned int t = 1; t <= T; ++t )
    {
        fin >> R;
        fin >> k;
        fin >> N;

//cout << R << " " << k << " " << N << endl;
        
        Queue = new unsigned int[ N + 1 ];

        for( unsigned int n=0; n<N; ++n )
        {
            fin >> Queue[ n ];
//cout << Queue[ n ] << " ";
        }
//cout << endl;

        Queue[ N ] = -1;
        posQueue = &Queue[0];
        total = 0;


        for( unsigned int r = 0; r < R; ++r )
        {
//cout << r << " - " << endl;
            subTotal = 0;
            lastPos = posQueue;

            do
            {
                subTotal += *posQueue;

//cout << "     " << *posQueue << ",";

                ++posQueue;

                if( *posQueue == -1 )
                    posQueue = &Queue[0];

            } while( subTotal + *posQueue <= k &&
                     lastPos != posQueue );
//cout << endl;

            total += subTotal;
        }



        // RESULT..........

        fout << "Case #" << t << ": " << total << endl;


        delete [] Queue;
    }


    fin.close();
    fout.close();


    return 1;
}





///// Snapper:::
/*
int main(int argc, char** argv)
{
    if( argc != 2 )
    {
        return -1;
    }

    string filename = argv[1];



    ifstream fin( filename.c_str() );
    ofstream fout( "result.out" );


    if( fin.fail() )
    {
        cout << "ERROR al abrir el fichero de entrada" << endl;
        return -1;
    }
    if( fout.fail() )
    {
        cout << "ERROR al abrir el fichero de salida" << endl;
        return -1;
    }



    int T;
    int N;
    unsigned long long K;
    bool *Snapper;


    fin >> T;


    for( int i = 1; i <= T; ++i )
    {
        fin >> N;
        fin >> K;

//        cout << N << " " << K << endl;


        Snapper = new bool[ N ];

//        cout << "- ";
        for( int n = 0; n < N; ++n )
        {
            Snapper[n] = false;
//            cout << Snapper[n];
        }
//        cout << endl;



        for( int k = 0; k < K; ++k )
        {
            Snapper[0] = ! Snapper[0];

//            cout << k << " " << Snapper[0];

            for( int n = 1; n < N; ++n )
            {
                if( ! Snapper[n-1] )
                {
                    Snapper[n] = ! Snapper[n];
//                    cout << Snapper[n];
                }
                else
                {
  //                  for(; n < N; ++n )
    //                    cout << Snapper[n];
                    break;
                }
            }

//            cout << endl;
        }





        fout << "Case #" << i << ": ";

        bool isOn = true;
        for( int n = 0; n < N; ++n )
        {
            if( ! Snapper[n] )
            {
                isOn = false;
                break;
            }
        }

        if( isOn == false )
            fout << "OFF" << endl;
        else
            fout << "ON" << endl;


        delete [] Snapper;
    }


    fin.close();
    fout.close();


    return 1;
}*/