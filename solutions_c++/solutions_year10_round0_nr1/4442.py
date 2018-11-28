#include <iostream.h>
#include <fstream.h>

int status[30], pwr = 0;

void toggle()
{
    int i = 0;
    for ( i = 0 ; i <= pwr ; i++ )
    {
        status[i]++;
        status[i] %= 2;
    }
    i = 0;
    while ( status[i] )
    {
        i++;
    }
    pwr = i;
}

int main()
{
    ifstream inputFile("A-small-attempt1.in", ios::in);
    ofstream outputFile("A-small-attempt1.out", ios::out);

    int n = 0, t = 0, i = 0, j = 0, p = 0, b = 0;
    long k = 0;

    inputFile >> t;

    for ( i = 1 ; i <= t ; i++ )
    {
        inputFile >> n >> k;
        pwr = 0;
        for ( j = 0 ; j < n ; j++ )
        {
            status[j] = 0;
        }

        for ( p = 1 ; p <= k ; p++ )
        {
            toggle();
        }

        outputFile << "Case #" << i << ": ";
        for ( b = 0 ; status[b] && b < n; b++ );
        if ( b < n )
        {
            outputFile << "OFF";
        }
        else
        {
            outputFile << "ON";
        }
        outputFile << "\n";
    }

    inputFile.close();
    outputFile.close();
}
