#include<iostream>
#include<string.h>

using namespace std;

main()
{
    //freopen( "A-small.in", "r", stdin );
    //freopen( "A-small-attempt0.in", "r", stdin );
    //freopen( "A-small-attempt0.out", "w", stdout );
    freopen( "A-large.in", "r", stdin );
    freopen( "A-large.out", "w", stdout );
    int N, K, Cases, powN;
    cin>>Cases;
    for( int i = 0; i < Cases; ++i )
    {
        cin>>N>>K;
        powN = 1;
        for( int j = 0; j < N; ++j )
            powN = powN * 2;
        long int temp;
        int ctr = 0;
        do
        {
            temp = powN * ctr + powN - 1;
            ctr++;
        }while( temp < K );
        if( temp == K )
            cout<<"Case #"<<i+1<<": ON\n";
        else
            cout<<"Case #"<<i+1<<": OFF\n";
    }
}

